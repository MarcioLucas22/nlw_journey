import uuid
from src.drivers.email_sender import send_email
from ..models.repositories.trips_repository import TripsRepository
from ..models.repositories.emails_to_invite_repository import EmailsToInviteRepository

class TripCreator:
    def __init__(self, trip_repository: TripsRepository, emails_repository: EmailsToInviteRepository) -> None:
        self.__trip_repository = trip_repository
        self.__emails_repository = emails_repository

    def create(self, body) -> dict:
        try:
            emails = body.get("emails_to_invite")

            trip_id = str(uuid.uuid4())
            trip_infos = {**body, "id": trip_id} # **body pega todas as informações do dicionário "body" e coloca nesse novo dicionário q no caso é o "trips_infos" adicionando novas informações

            self.__trip_repository.create_trip(trip_infos)        

            if emails:
                for email in emails:
                    self.__emails_repository.registry_email({
                        "email": email,
                        "trip_id": trip_id,
                        "id": str(uuid.uuid4()),
                    })
            
            send_email([
                body['owner_email']], 
                f'http://localhost:3000/trips/{trip_id}/confirm'       
            )
            
            return {
                "body": {"id": trip_id},
                "status_code": 201,
            }
        except Exception as error:
            return {
                "body": { "error": "Bad Request", "message": str(error) },
                "status_code": 400
            }