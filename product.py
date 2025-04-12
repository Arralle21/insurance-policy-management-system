class Product:
    def __init__(self, id, name, coverage, premium, term):
        self.id = id
        self.name = name
        self.coverage = coverage
        self.premium = premium
        self.term = term
        self.status = "Active"
        
    def update(self, coverage=None, premium=None, term=None):
        if coverage:
            self.coverage = coverage
        if premium:
            self.premium = premium
        if term:
            self.term = term
        return f"Product {self.name} has been updated."
        
    def suspend(self):
        self.status = "Suspended"
        return f"Product {self.name} has been suspended."
        
    def reactivate(self):
        self.status = "Active"
        return f"Product {self.name} has been reactivated."
        
    def display_details(self):
        return f"Product ID: {self.id}, Name: {self.name}, Coverage: {self.coverage}, Premium: {self.premium}, Term: {self.term}, Status: {self.status}"
