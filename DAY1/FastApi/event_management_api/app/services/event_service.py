from app.repositories.event_repository import EventRepository
from app.schemas.event_schema import EventCreate
from fastapi import HTTPException

class EventService:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def create_event(self, event_in: EventCreate):
        if self.event_repository.find_by_name(event_in.name):
            raise HTTPException(status_code=400, detail="Event name already exists")
        return self.event_repository.save(event_in.model_dump())

    def get_all_events(self, location: str = None):
        if location:
            return self.event_repository.find_by_location(location)
        return self.event_repository.find_all()

    def get_event_by_id(self, event_id: int):
        event = self.event_repository.find_by_id(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return event