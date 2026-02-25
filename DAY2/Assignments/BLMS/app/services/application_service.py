from fastapi import HTTPException

class ApplicationService:

    def __init__(self, repo, product_repo):

        self.repo = repo

        self.product_repo = product_repo


    def create(self, db, data):

        product = self.product_repo.get(db, data.product_id)

        if not product:

            raise HTTPException(404, "Product not found")

        if data.requested_amount > product.max_amount:

            raise HTTPException(400, "Amount exceeds product limit")

        return self.repo.create(db, data)


    def update_status(self, db, id, status, amount):

        app = self.repo.get(db, id)

        if not app:

            raise HTTPException(404, "Application not found")

        app.status = status

        app.approved_amount = amount

        return self.repo.update(db, app)