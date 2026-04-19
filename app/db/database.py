import os
from sqlalchemy import event
from sqlalchemy import create_engine
from typing import Generator
from sqlalchemy.orm import sessionmaker, Session
from app.db.models import Base

ENV = os.getenv("ENV", "development")
if ENV == "development":
    DB_URL = os.getenv("DATABASE_URL_LOCAL") or "sqlite:///./ai_knowledge_assistant.db"
else:
    DB_URL = os.getenv("DATABASE_URL")

if not DB_URL:
    raise ValueError("DATABASE_URL is not set")
engine = create_engine(DB_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)

# Registrar el tipo pgvector solo si estamos usando PostgreSQL
if DB_URL.startswith("postgres"):
    from pgvector.psycopg2 import register_vector

    @event.listens_for(engine, "connect")
    def _register_vector(dbapi_connection, connection_record):
        register_vector(dbapi_connection)

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
  

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


