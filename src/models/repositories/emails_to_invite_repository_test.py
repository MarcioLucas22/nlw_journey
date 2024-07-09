import pytest
import uuid
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = '49384909-29d6-4b26-bdb3-065d77aa1353'

@pytest.mark.skip(reason='Interação com o banco')
def test_registry_email():
    conn = db_connection_handler.get_connection()
    trips_repository = EmailsToInviteRepository(conn)

    emails_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": 'Esse é um email de teste',
    }

    trips_repository.registry_email(emails_infos)

@pytest.mark.skip(reason='Interação com o banco')
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = EmailsToInviteRepository(conn)

    emails = trips_repository.find_emails_from_trip(trip_id)
    print(emails)