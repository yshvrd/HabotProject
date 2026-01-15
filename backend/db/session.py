# Creates and manages a db session 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://habot:habot@localhost:5432/habot-db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


'''
from project root, run a docker conatiner

docker run -d \
  --name habot-db \
  -e POSTGRES_USER=habot \
  -e POSTGRES_PASSWORD=habot \
  -e POSTGRES_DB=habot-db \
  -p 5432:5432 \
  postgres:16

'''

'''
optional verify inside container 

docker exec -it <id> bash

psql -h localhost -U habot -d habot-db

\dt -> list tables 
\du -> list users

SELECT * FROM employees; -> to verify table structure
'''

