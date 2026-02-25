class ParticipantRepository:
    def __init__(self):
        self._participants = []
        self._counter = 1

    def save(self, participant_data: dict):
        participant_data["id"] = self._counter
        self._participants.append(participant_data)
        self._counter += 1
        return participant_data

    def find_all(self):
        return self._participants

    def find_by_id(self, participant_id: int):
        return next((p for p in self._participants if p["id"] == participant_id), None)

    def find_by_email(self, email: str):
        return next((p for p in self._participants if p["email"].lower() == email.lower()), None)

    def count_by_event_id(self, event_id: int):
        return sum(1 for p in self._participants if p["event_id"] == event_id)