from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from urllib.parse import quote_plus

# Connection string for SQL Server
username = "userai"
password = quote_plus("useraiP@ssw0rd")  # เข้ารหัสให้เหมาะกับ URL
server = "10.28.254.35"
database = "pvdb"
driver = "ODBC Driver 17 for SQL Server"

# สร้าง connection string
SQL_SERVER_URL = (
    f"mssql+pyodbc://{username}:{password}@{server}/{database}"
    f"?driver={quote_plus(driver)}"
)

engine_sql_server  = create_engine(
    SQL_SERVER_URL,
    echo=True,
    poolclass=QueuePool,  # ใช้ QueuePool สำหรับ Connection Pooling
    pool_size=10,          # จำนวน connection ใน pool
    max_overflow=10,      # จำนวน connection ที่อนุญาตให้สร้างเกิน pool_size
    pool_timeout=30       # ระยะเวลารอการเชื่อมต่อ
)

SessionLocalSQLServer = sessionmaker(autocommit=False, autoflush=False, bind=engine_sql_server)

def get_db_sql_server():
    db = SessionLocalSQLServer()
    try:
        yield db
    finally:
        db.close()
