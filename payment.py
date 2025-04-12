class Payment:
    def __init__(self, id, policy, amount, date):
        self.id = id
        self.policy = policy
        self.amount = amount
        self.date = date
        self.status = "Pending"
        
    def process(self):
        self.status = "Processed"
        return f"Payment {self.id} has been processed."
        
    def generate_receipt(self):
        receipt = f"Receipt for Payment ID: {self.id}\n"
        receipt += f"Policy ID: {self.policy.id}\n"
        receipt += f"Policyholder: {self.policy.policyholder.name}\n"
        receipt += f"Product: {self.policy.product.name}\n"
        receipt += f"Amount: {self.amount}\n"
        receipt += f"Date: {self.date}\n"
        receipt += f"Status: {self.status}\n"
        return receipt
