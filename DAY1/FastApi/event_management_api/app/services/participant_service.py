from app.repositories.participant_repository import ParticipantRepository
from app.repositories.event_repository import EventRepository
from app.schemas.participant_schema import ParticipantCreate
from fastapi import HTTPException

class ParticipantService:
    def __init__(self, participant_repository: ParticipantRepository, event_repository: EventRepository):
        self.participant_repository = participant_repository
        self.event_repository = event_repository

    def register_participant(self, participant_in: ParticipantCreate):
        # 1. Event must exist
        event = self.event_repository.find_by_id(participant_in.event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        
        # 2. Event must not exceed capacity
        current_count = self.participant_repository.count_by_event_id(participant_in.event_id)
        if current_count >= event["capacity"]:
            raise HTTPException(status_code=400, detail="Event capacity exceeded")
        
        # 3. Email must be unique
        if self.participant_repository.find_by_email(participant_in.email):
            raise HTTPException(status_code=400, detail="Email already registered")
            
        return self.participant_repository.save(participant_in.model_dump())

    def get_participant_by_id(self, participant_id: int):
        participant = self.participant_repository.find_by_id(participant_id)
        if not participant:
            raise HTTPException(status_code=404, detail="Participant not found")
        return participant