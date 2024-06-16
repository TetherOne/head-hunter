# import os
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.pool import StaticPool
# from fastapi.testclient import TestClient
#
# from core.models import Base
# from main import hh_app
#
# SQLALCHEMY_DATABASE_URL = os.environ.get("DB_URL_TEST")
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={"check_same_thread": False},
#     poolclass=StaticPool,
# )
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#
# Base.metadata.create_all(bind=engine)
#
#
# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()
#
#
# hh_app.dependency_overrides[get_db] = override_get_db
#
# client = TestClient(hh_app)
