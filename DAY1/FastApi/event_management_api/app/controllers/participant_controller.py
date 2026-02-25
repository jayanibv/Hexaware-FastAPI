from fastapi import APIRouter, Depends
from app.dependency.service_dependency import get_participant_service
from app.services.participant_service import ParticipantService
from app.schemas.participant_schema import ParticipantCreate, ParticipantResponse

router = APIRouter(prefix="/participants", tags=["Participants"])

@router.post("", response_model=ParticipantResponse)
def register_participant(
    participant: ParticipantCreate, 
    participant_service: ParticipantService = Depends(get_participant_service)
):
    return participant_service.register_participant(participant)

@router.get("/{id}", response_model=ParticipantResponse)
def get_participant(id: int, participant_service: ParticipantService = Depends(get_participant_service)):
    return participant_service.get_participant_by_id(id)