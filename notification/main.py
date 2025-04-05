from database.database import get_db_sql_server
from sqlalchemy import text
import pandas as pd
from services.send_notify import send_alarm
import models.alarm_message as alarm

# Function to fetch data from SQL Server
def fetch_data_from_sql():
    db = next(get_db_sql_server())
    sql_text = text("""
        SELECT TOP (1)
            [Time], 
            Machine, 
            Product, 
            Material, 
            Pallet, 
            Width_AVG, 
            Length_AVG, 
            Thickness_AVG, 
            Rz, 
            Wz, 
            US_AVG, 
            IS_PAR_AVG, 
            IS_PER_AVG, 
            code, 
            ThickUp, 
            ThickLow, 
            WidthUp, 
            WidthLow, 
            LenUp, 
            LenLow, 
            [IS PAR], 
            [US AVG R2], 
            ThickUp_มอก, 
            ThickLow_มอก 
        FROM pvdb.dbo.qc_notify
        ORDER BY [Time] DESC;
    """)
    df = pd.read_sql(sql_text, db.get_bind())
    return df.fillna(-1)

# Function to perform checks on the data
def check_data(df):
    message = ""

    if not df.empty:
        first_row = df.iloc[0]

        # 1. Rz >= 13.4
        if float(first_row["Rz"]) != -1 and float(first_row["Rz"]) <= 13.4:
            message += alarm.rz_alert(
                actual=first_row["Rz"],
                machine=first_row["Machine"],
                product=first_row["Product"]
            )

        # 2. Wz >= 1.4
        if float(first_row["Wz"]) != -1 and float(first_row["Wz"]) <= 1.4:
            message += alarm.wz_alert(
                actual=first_row["Wz"],
                machine=first_row["Machine"],
                product=first_row["Product"]
            )

        # 3. US < Product in table
        if float(first_row["US_AVG"]) != -1 and float(first_row["US_AVG"]) <= float(first_row["US AVG R2"]):
            message += alarm.us_alert(
                actual=first_row["US_AVG"],
                limit=first_row["US AVG R2"],
                machine=first_row["Machine"],
                product=first_row["Product"]
            )

        # 4. IS < Product in table
        if float(first_row["IS_PAR_AVG"]) != -1 and float(first_row["IS_PAR_AVG"]) <= float(first_row["IS PAR"]):
            message += alarm.is_alert(
                actual=first_row["IS_PAR_AVG"],
                limit=first_row["IS PAR"],
                machine=first_row["Machine"],
                product=first_row["Product"]
            )

        # 5. Width, Length, Thickness within Product range in table
        if (first_row["WidthLow"] != -1 and first_row["WidthUp"] != -1 and first_row["Width_AVG"] != -1 and
            first_row["LenLow"] != -1 and first_row["LenUp"] != -1 and first_row["Length_AVG"] != -1 and
            first_row["ThickLow"] != -1 and first_row["ThickUp"] != -1 and first_row["Thickness_AVG"] != -1) and not (
            float(first_row["WidthLow"]) < float(first_row["Width_AVG"]) < float(first_row["WidthUp"]) or
            float(first_row["LenLow"]) < float(first_row["Length_AVG"]) < float(first_row["LenUp"]) or
            float(first_row["ThickLow"]) < float(first_row["Thickness_AVG"]) < float(first_row["ThickUp"])
        ):
            message += alarm.dimension_alert(
                width=first_row["Width_AVG"],
                length=first_row["Length_AVG"],
                thickness=first_row["Thickness_AVG"],
                width_limit=[first_row["WidthLow"], first_row["WidthUp"]],
                length_limit=[first_row["LenLow"], first_row["LenUp"]],
                thickness_limit=[first_row["ThickLow"], first_row["ThickUp"]],
                machine=first_row["Machine"],
                product=first_row["Product"]
            )

    return message


# Main execution
if __name__ == "__main__":
    
    data = fetch_data_from_sql()
    message = check_data(data)
    print(message)
    print("Message length:", len(message))
    if message:
        send_alarm(message)
