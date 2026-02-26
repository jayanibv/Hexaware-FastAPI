from app.services.leave_service import LeaveService

service = LeaveService()

def apply_leave(db, data):
    return service.apply_leave(db, data)