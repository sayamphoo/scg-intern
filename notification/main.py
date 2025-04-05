from database.database import get_db_sql_server
from sqlalchemy import text

db = next(get_db_sql_server())

result = db.execute(text("SELECT u.* FROM [SCM].[dbo].[Users] AS u"))
print(f"✅ SQL Server Connected! Current datetime: {result}")