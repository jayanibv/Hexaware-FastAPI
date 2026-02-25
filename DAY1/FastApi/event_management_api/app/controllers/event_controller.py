from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from app.dependency.service_dependency import get_event_service
from app.services.event_service import EventService
from app.schemas.event_schema import EventCreate, EventResponse

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("", response_model=EventResponse)
def create_event(event: EventCreate, event_service: EventService = Depends(get_event_service)):
    return event_service.create_event(event)

@router.get("", response_model=List[EventResponse])
def get_events(
    location: Optional[str] = Query(None), 
    event_service: EventService = Depends(get_event_service)
):
    return event_service.get_all_events(location)

@router.get("/{event_id}", response_model=EventResponse)
def get_event(event_id: int, event_service: EventService = Depends(get_event_service)):
    return event_service.get_event_by_id(event_id)
