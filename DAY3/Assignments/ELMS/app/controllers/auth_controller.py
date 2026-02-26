from app.services.auth_service import AuthService

service = AuthService()

def login(db, email, password):
    return service.login(db, email, password)