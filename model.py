import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

# Базовый класс
Base = declarative_base()

# Модель
class Feature(Base):
    __tablename__ = 'features'

    id = Column(Integer, primary_key=True)
    country = Column(String)
    network = Column(String)
    mcc_mnc = Column(String)
    vendor = Column(String)
    vendor_product = Column(String)
    necessary_information = Column(String)
    features = Column(String)
    primary_contact = Column(String)
    additional_contact = Column(String)
    eta_for_registration = Column(String)
    registration_window = Column(String)
    am_to_confirm_notify = Column(String)
    fees_for_client = Column(String)
    fees_for_us = Column(String)
    necessary_tag = Column(String)
    is_active = Column(Boolean, default=True)

# Функция для создания базы данных
def init_db():
    try:
        os.makedirs(os.path.join(os.getcwd(), 'data'), exist_ok=True)
        db_path = os.path.join(os.getcwd(), 'data', 'test_database.db')  # Путь до базы данных
        db_url = f'sqlite:///{db_path}'
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        print(f"Database created at: {db_path}")
        return engine
    except Exception as e:
        print(f"An error occurred: {e}")