from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

DATABASE_URL = f"postgresql://{settings.postgre_usr}:{settings.postgre_pwd}@{settings.postgre_host}:{settings.postgre_port}/{settings.database_name}"

engine = create_engine(DATABASE_URL)

local_session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
base = declarative_base()

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()



# while True:
#     try:
#         conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="qw34.rhju780!", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         break
#     except Exception as error:
#         print("Error while connection database:\n", error)
#         time.sleep(2)
