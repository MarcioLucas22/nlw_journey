from ..models.repositories.trips_repository import TripsRepository

class TripFinder:
    def __init__(self, trips_repository: TripsRepository) -> None:
        self.__trips_repository = trips_repository
    
    def find_trip_details(self, trip_id) -> dict:
        try:
            trip = self.__trips_repository.find_trip_by_id(trip_id)

            if not trip: raise Exception('No Trip Found.')

            return {
                "body": {
                    "trip": {
                        "id": trip[0],
                        "destination": trip[1],
                        "starts_at": trip[2],
                        "ends_at": trip[3],
                        "status": trip[6],
                    }
                },
                "status_code": 200,
            }
        except Exception as error:
            return {
                "body": { "error": "Bad Request", "message": str(error) },
                "status_code": 400
            }
