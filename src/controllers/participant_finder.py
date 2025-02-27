from src.models.repositories.participants_repository import ParticipantsRepository

class ParticipantFinder:
    def __init__(self, participants_repository: ParticipantsRepository) -> None:
        self.__participants_repository = participants_repository

    def find_participants_from_trip(self, trip_id: str) -> dict:
        try:
            participants = self.__participants_repository.find_participants_from_trip(trip_id)

            participants_infos = []
            for participant in participants:
                participants_infos.append({
                    'id': participant[0],
                    'name': participant[1],
                    'is_confirmed': participant[2],
                    'email': participant[3],
                })

            return {
                'body': {'participants': participants_infos},
                'status_code': 200,
            }
        except Exception as error:
            return {
                "body": { "error": "Bad Request", "message": str(error) },
                "status_code": 400
            }