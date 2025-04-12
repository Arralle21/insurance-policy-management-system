class Policyholder:
    def __init__(self, id, name, address, contact_number):
        self.id = id
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.status = "Active"
        self.policies = []
        
    def suspend(self):
        self.status = "Suspended"
        return f"Policyholder {self.name} has been suspended."
        
    def reactivate(self):
        self.status = "Active"
        return f"Policyholder {self.name} has been reactivated."
        
    def add_policy(self, policy):
        self.policies.append(policy)
        
    def display_details(self):
        details = f"Policyholder ID: {self.id}\n"
        details += f"Name: {self.name}\n"
        details += f"Address: {self.address}\n"
        details += f"Contact: {self.contact_number}\n"
        details += f"Status: {self.status}\n"
        details += f"Policies:\n"
        
        if not self.policies:
            details += "  No policies registered\n"
        else:
            for policy in self.policies:
                details += f"  - Policy ID: {policy.id}, Product: {policy.product.name}, Status: {policy.status}\n"
                
        return details
