from app.repositories.event_repository import EventRepository
from app.repositories.participant_repository import ParticipantRepository
from app.services.event_service import EventService
from app.services.participant_service import ParticipantService

# Singleton instances for repositories
event_repo = EventRepository()
participant_repo = ParticipantRepository()

def get_event_service():
    return EventService(event_repo)

def get_participant_service():
    return ParticipantService(participant_repo, event_repo)