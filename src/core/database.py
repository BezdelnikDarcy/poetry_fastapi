from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.account.models.user import Base
from src.core.config import settings




sync_engine = create_engine(settings.db.db_sync_url, echo=False)
sync_session_maker = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)


def get_sync_session():
    with Session(sync_engine) as session:
        return session


Base.metadata.create_all(sync_engine)