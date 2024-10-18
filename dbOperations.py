from model import Feature, init_db
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Инициализация базы данных
engine = init_db()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для получения сессии
@contextmanager
def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# Функция для добавления записи
def add_feature(data):
    with get_db_session() as session:
        new_feature = Feature(
            country=data['country'],
            network=data['network'],
            mcc_mnc=data['mcc_mnc'],
            vendor=data['vendor'],
            vendor_product=data['vendor_product'],
            necessary_information=data['necessary_information'],
            features=data['features'],
            primary_contact=data['primary_contact'],
            additional_contact=data['additional_contact'],
            eta_for_registration=data['eta_for_registration'],
            registration_window=data['registration_window'],
            am_to_confirm_notify=data['am_to_confirm_notify'],
            fees_for_client=data['fees_for_client'],
            fees_for_us=data['fees_for_us'],
            necessary_tag=data['necessary_tag'],
            is_active=data['is_active']
        )
        session.add(new_feature)
        session.commit()
        print(f"Feature added with ID: {new_feature.id}")

# Функция для получения записи по стране
def get_features_by_country(country_):
    with get_db_session() as session:
        results = session.query(Feature).filter(Feature.country.like(f"%{country_}%")).all()
        return results

# Функция для удаления записи по ID
def delete_feature_by_id(feature_id):
    with get_db_session() as session:
        feature = session.query(Feature).get(feature_id)
        if feature:
            session.delete(feature)
            session.commit()
            print(f"Feature with ID {feature_id} deleted.")
        else:
            print(f"Feature with ID {feature_id} not found.")

# Функция для редактирования флага актуальности записи
def update_feature_active_status(feature_id, is_active):
    with get_db_session() as session:
        feature = session.query(Feature).get(feature_id)
        if feature:
            feature.is_active = is_active
            session.commit()
            status = "active" if is_active else "inactive"
            print(f"Feature with ID {feature_id} is now {status}.")
        else:
            print(f"Feature with ID {feature_id} not found.")