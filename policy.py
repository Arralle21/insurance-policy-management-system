class Policy:
    def __init__(self, id, policyholder, product, start_date, end_date):
        self.id = id
        self.policyholder = policyholder
        self.product = product
        self.start_date = start_date
        self.end_date = end_date
        self.status = "Active"
        self.payments = []
        
    def suspend(self):
        self.status = "Suspended"
        return f"Policy {self.id} has been suspended."
        
    def reactivate(self):
        self.status = "Active"
        return f"Policy {self.id} has been reactivated."
        
    def add_payment(self, payment):
        self.payments.append(payment)
        
    def send_payment_reminder(self):
        return f"Payment reminder sent to {self.policyholder.name} for policy {self.id}."
        
    def apply_penalty(self, penalty_amount):
        penalty = f"Penalty of {penalty_amount} applied to policy {self.id} for late payment."
        return penalty
