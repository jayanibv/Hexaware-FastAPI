from app.services.leave_service import LeaveService

service = LeaveService()

def approve_leave(db, leave_id, manager_id):
    return service.approve_leave(db, leave_id, manager_id)