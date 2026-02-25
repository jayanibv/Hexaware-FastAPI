class UserNotFoundException(Exception):

    def __init__(self, user_id: int):

        self.user_id = user_id

        self.message = f"User with id {user_id} not found"

        super().__init__(self.message)


class JobNotFoundException(Exception):

    def __init__(self, job_id: int):

        self.job_id = job_id

        self.message = f"Job with id {job_id} not found"

        super().__init__(self.message)


class ApplicationNotFoundException(Exception):

    def __init__(self, application_id: int):

        self.application_id = application_id

        self.message = f"Application with id {application_id} not found"

        super().__init__(self.message)


class DuplicateUserException(Exception):

    def __init__(self, email: str):

        self.message = f"User with email {email} already exists"

        super().__init__(self.message)