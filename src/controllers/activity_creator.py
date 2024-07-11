import uuid
from src.models.repositories.activities_repository import ActivitiesRepository

class ActivityCreator:
    def __init__(self, activities_repository: ActivitiesRepository) -> None:
        self.__activities_repository = activities_repository
    
    def create(self, body, trip_id: str) -> dict:
        try:
            id = str(uuid.uuid4())
            activities_infos = {
                'id': id,
                'trip_id': trip_id,
                'title': body['title'],
                'occurs_at': body['occurs_at']
            }
            self.__activities_repository.registry_activity(activities_infos)

            return {
                'body': { 'activity_id': id },
                'status_code': 201
            }
        except Exception as error:
            return {
                "body": { "error": "Bad Request", "message": str(error) },
                "status_code": 400
            }