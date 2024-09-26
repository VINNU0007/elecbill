class ElectricityBill:
    def __init__(self, customer_name, previous_reading, current_reading):
        self.customer_name = customer_name
        self.previous_reading = previous_reading
        self.current_reading = current_reading
        self.usage = self.calculate_usage()

    def calculate_usage(self):
        return self.current_reading - self.previous_reading

    def calculate_bill(self):
        # Simple rate structure
        if self.usage <= 100:
            rate = 0.5  # $0.50 per kWh
        elif self.usage <= 300:
            rate = 0.75  # $0.75 per kWh
        else:
            rate = 1.0  # $1.00 per kWh
        
        return self.usage * rate

    def generate_bill(self):
        bill_amount = self.calculate_bill()
        return f"""
        Electricity Bill
        ----------------------
        Customer Name: {self.customer_name}
        Previous Reading: {self.previous_reading} kWh
        Current Reading: {self.current_reading} kWh
        Usage: {self.usage} kWh
        Total Bill: ${bill_amount:.2f}
        ----------------------
        """

def main():
    print("Welcome to the Electricity Bill Generator")
    
    customer_name = input("Enter customer name: ")
    previous_reading = float(input("Enter previous meter reading (in kWh): "))
    current_reading = float(input("Enter current meter reading (in kWh): "))

    if current_reading < previous_reading:
        print("Error: Current reading must be greater than or equal to previous reading.")
        return

    bill = ElectricityBill(customer_name, previous_reading, current_reading)
    print(bill.generate_bill())

if __name__ == "__main__":
    main()
