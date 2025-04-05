from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
# from database import BaseSQLServer, BaseSQLite
from urllib.parse import quote_plus

# Connection string for SQL Server
username = "userscm"
password = quote_plus("zP@ssw0rd#2025")  # เข้ารหัสให้เหมาะกับ URL
server = "10.28.254.35"
database = "SCM"
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


# Session factory
SessionLocalSQLServer = sessionmaker(autocommit=False, autoflush=False, bind=engine_sql_server)
# SessionLocalSQLite = sessionmaker(autocommit=False, autoflush=False, bind=engine_sqlite)


# def init_db():
#     try:
#         print("Creating tables...")
#         BaseSQLServer.metadata.create_all(engine_sql_server)
#         # BaseSQLite.metadata.create_all(engine_sqlite)
#         print("Tables created successfully!")
#     except Exception as e:
#         print(f"Error creating tables: {e}")
#         raise 
        
def get_db_sql_server():
    db = SessionLocalSQLServer()
    try:
        yield db
    finally:
        db.close()


# def get_db_sql_lite():
#     db = SessionLocalSQLite()
#     try:
#         yield db
        
#     finally:
#         db.close()
        
