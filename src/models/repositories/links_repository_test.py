import pytest
import uuid
from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = '0b73dd9f-560d-462d-91c1-0326a97dbcd2'

@pytest.mark.skip(reason='Interação com o banco')
def test_registry_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": 'somelink.com',
        "title": 'Hotel',
    }

    links_repository.registry_link(links_infos)

@pytest.mark.skip(reason='Interação com o banco')
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    response = links_repository.find_links_from_trip(trip_id)

    assert isinstance(response, list)
    assert isinstance(response[0], tuple)
    print(response)