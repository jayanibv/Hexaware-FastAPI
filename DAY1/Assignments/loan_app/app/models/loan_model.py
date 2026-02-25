class Loan:
    def __init__(self, id, name, email, amount, annual_income, interest_rate, duration):
        self.id = id
        self.name = name
        self.email = email
        self.amount = amount
        self.annual_income = annual_income
        self.interest_rate = interest_rate
        self.duration = duration
        self.status = "PENDING"