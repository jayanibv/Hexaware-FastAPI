from app.services.user_service import UserService
from app.services.department_service import DepartmentService

user_service = UserService()
dept_service = DepartmentService()


def create_user(db, data):
    return user_service.create_user(db, data)

def get_users(db):
    return user_service.get_all_users(db)

def create_department(db, data):
    return dept_service.create_department(db, data)

def get_departments(db):
    return dept_service.get_all_departments(db)