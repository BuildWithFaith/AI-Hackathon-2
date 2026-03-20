import os
from sqlmodel import create_engine, Session, select
from models import Task

database_url = "postgresql://neondb_owner:npg_is0UzWVT6apN@ep-dry-moon-a1038qtl-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"
engine = create_engine(database_url)

with Session(engine) as session:
    tasks = session.exec(select(Task)).all()
    for t in tasks:
        print(t)
