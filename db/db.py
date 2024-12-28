from sqlalchemy import create_engine

CIXOOT_DATABASE_URL = "sqlite:///./sql_app.db"


engine = create_engine(
    CIXOOT_DATABASE_URL, connect_args={"check_same_thread": False}
)