from ..models.repositories.trips_repository import TripsRepository

class TripConfirmer:
    def __init__(self, trips_repository: TripsRepository) -> None:
        self.__trips_repository = trips_repository

    def confirm(self, trip_id) -> dict:
        try:
            self.__trips_repository.update_trip_status(trip_id)
            return { "body": None, "status_code": 204 }
        except Exception as error:
            return {
                "body": { "error": "Bad Request", "message": str(error) },
                "status_code": 400
            }