from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.company_repositories import CompanyRepository
from app.schemas.company_schema import (
    CompanyCreate,
    CompanyUpdate,
    CompanyResponse,
)

class CompanyService:

    def __init__(self, db: Session):
        self.db = db
        self.company_repo = CompanyRepository(db)

    # CREATE COMPANY
    def create_company(self, payload: CompanyCreate) -> CompanyResponse:
        existing_company = self.company_repo.get_company_by_name(payload.name)
        if existing_company:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Company already registered"
            )
        company = self.company_repo.create_company(payload.model_dump())

        return CompanyResponse.model_validate(company)


    # GET COMPANY BY ID
    def get_company_by_id(self, company_id: int) -> CompanyResponse:
        company = self.company_repo.get_company_by_id(company_id)

        if not company:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Company not found"
            )

        return CompanyResponse.model_validate(company)


    # UPDATE COMPANY (BY ID)
    def update_company(self, company_id: int, payload: CompanyUpdate) -> CompanyResponse:
        company = self.company_repo.get_company_by_id(company_id)

        if not company:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Company not found"
            )

        update_data = payload.model_dump(exclude_unset=True)

        updated_company = self.company_repo.update_company(company, update_data)

        return CompanyResponse.model_validate(updated_company)


    # DELETE COMPANY (BY ID)
    def delete_company(self, company_id: int):
        company = self.company_repo.get_company_by_id(company_id)

        if not company:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Company not found"
            )

        self.company_repo.delete_company(company)

        return {"message": "Company deleted successfully"}