from fastapi import APIRouter, Request, HTTPException, Response
import httpx
from app.core.config import settings
import os

router = APIRouter()

SERVICE_MAP = {
    "application": os.getenv("APPLICATION_SERVICE_URL", "http://application-service:8004"),
    "job": os.getenv("JOB_SERVICE_URL", "http://job-service:8005"),
    "user": os.getenv("USER_SERVICE_URL", "http://user-service:8002"),
    "auth": os.getenv("AUTH_SERVICE_URL", "http://auth-service:8001"),
    "company": os.getenv("COMPANY_SERVICE_URL", "http://company-service:8003")
}

@router.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy(service: str, request: Request, path: str):
    if service not in SERVICE_MAP:
        raise HTTPException(status_code=404, detail="Service not found")
    
    target_url = f"{SERVICE_MAP[service]}/{path}"
    
    # Exclude the host header from the request to the microservice
    headers = dict(request.headers)
    headers.pop("host", None)
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method=request.method,
                url=target_url,
                headers=headers,
                params=request.query_params,
                content=await request.body(),
                follow_redirects=True,
                timeout=30.0
            )
            
            # Return a Response with the same content, status code and headers
            return Response(
                content=response.content,
                status_code=response.status_code,
                headers=dict(response.headers)
            )
        except httpx.RequestError as exc:
            raise HTTPException(status_code=503, detail=f"Service {service} is unreachable: {str(exc)}")