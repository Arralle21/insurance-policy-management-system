from policyholder import Policyholder
from product import Product
from payment import Payment
from policy import Policy

def main():
    # Create products
    health_insurance = Product(101, "Health Insurance", "Medical coverage", 500, "1 year")
    car_insurance = Product(102, "Car Insurance", "Vehicle coverage", 300, "6 months")
    
    # Create policyholders
    john = Policyholder(1, "John Smith", "123 Main St", "555-1234")
    alice = Policyholder(2, "Alice Johnson", "456 Oak Ave", "555-5678")
    
    # Create policies
    john_health_policy = Policy(1001, john, health_insurance, "2025-01-01", "2026-01-01")
    alice_car_policy = Policy(1002, alice, car_insurance, "2025-01-15", "2025-07-15")
    
    # Add policies to policyholders
    john.add_policy(john_health_policy)
    alice.add_policy(alice_car_policy)
    
    # Process payments
    john_payment = Payment(10001, john_health_policy, 500, "2025-01-01")
    alice_payment = Payment(10002, alice_car_policy, 300, "2025-01-15")
    
    john_payment.process()
    alice_payment.process()
    
    john_health_policy.add_payment(john_payment)
    alice_car_policy.add_payment(alice_payment)
    
    # Display policyholder details
    print("=== Policyholder Details ===")
    print(john.display_details())
    print("\n")
    print(alice.display_details())
    
if __name__ == "__main__":
    main()
