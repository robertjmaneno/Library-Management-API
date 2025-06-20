from sqlmodel import create_engine, SQLModel, Session
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)  # echo=True for SQL logging during development

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.create_all(engine)