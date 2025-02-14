# The DunnDelivery class demonstrates core OOP concepts:
# - Encapsulation: Data (menu, prices) and methods are bundled in the class
# - Abstraction: Complex delivery logic is hidden behind simple method calls

class DunnDelivery:
    def __init__(self):
        # Class attributes demonstrate encapsulation 
        # by keeping related data together

        # Menu Attribute - menu of items you can order to be delivered
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Latte", "Cappuccino", "Peppermint Hot Mocha", "Caramel Macchiato", "Iced Shaken Espresso"],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus & Pita", "Chicken Wrap"]
        }
        
        # Prices encapsulated within the class
        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappuccino": 4.99, "Peppermint Hot Mocha" : 4.99, "Caramel Macchiato" : 3.99, "Iced Shaken Espresso" : 5.99,
            "Bagel": 2.99, "Muffin": 2.99, "Scone": 2.99,
            "Falafel Wrap": 8.99, "Hummus & Pita": 7.99, "Chicken Wrap": 8.99,        
        }
        
        # Delivery locations and number of minutes to deliver to that location
        self.delivery_locations = {
            "Library": 10,  # minutes
            "Academic Success Center": 8,
            "ITEC Computer Lab": 5
        }
    
    # Show the menu of items available for delivery
    def show_menu(self, category=None):
        if category:
            print(f"\n=== {category} ===")
            # Loop through the items in that specific category on the menu
            # and display them to the user
            for item in self.menu[category]:
                print(f"{item}: ${self.prices[item]:.2f}")
        else:
            # Show the entire menu
            for category in self.menu:
                print(f"\n=== {category} ===")
                for item in self.menu[category]:
                    print(f"{item}: ${self.prices[item]:.2f}")
    
    # Method to calculate the total cost of the order
    def calculate_total(self, items, has_student_id=False, priority_delivery=False):
        # Calculate the total
        total = sum(self.prices[item] for item in items)

        #Calculate the student discount based on the student ID
        if has_student_id and total > 10:
            total *= 0.9

        # Add priority delivery charge , costs $2 extra
        if priority_delivery:
            total += 2.00

        #This method returns the total cost of the order to the code that
        # called the method
        return total
    
    # Method to calculate the delivery time based on location and time of day
    def estimate_delivery(self, location, current_hour, priority_delivery=False):
        #Calculate the base time
        base_time = self.delivery_locations[location]

        # Calculate the delivery time based on the time of day ( adjust for busy times of day)
        if (9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            return base_time + 5

        # Reduce time if priority delivery is selected 
        if priority_delivery:
            base_time = max(1, base_time - 3)  # This ensures that the minimum delivery time is at least 1 minute
        
        # If they aren't ordering during a busy time, return the base time with no adjustment
        return base_time

    # Method that prints the order (receipt)
    def print_order(self, location, items, current_hour, has_student_id=False, priority_delivery=False):
        if not all(item in self.prices for item in items):
            print("One or more items are not available. Please check the menu.")
            return

        # Display the order information
        print("\n=== Order Summary ===")
        print(f"Delivery to: {location}")
        print("\nItems ordered:")

        # Loop through the list of menu items they ordered
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")
        
        # Call the methods to get the total cost and the delivery time
        total = self.calculate_total(items, has_student_id, priority_delivery)
        delivery_time = self.estimate_delivery(location, current_hour, priority_delivery)
        
        # Display the subtotal
        print(f"\nSubtotal: ${sum(self.prices[item] for item in items):.2f}")

        # Calculate the total with the discount if the customer has a student id
        if has_student_id and total < sum(self.prices[item] for item in items):
            print("Student Discount Applied!")

        # Notify customer if priority delivery was selected
        if priority_delivery:
            print("Priority Delivery Selected! (Additional $2, reduces time by 3 minutes)")
        
        # Display total after discount & estimated delivery time
        print(f"Total after discount: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")
    
    # Method that lets customers rate their delivery experience ( 1-5 stars)
    def rate_delivery(self):
        # While loop ensures customer provides valid input
        while True: 
            try:
                # Prompt the customer to enter a rating and convert input to an integer
                rating = int(input("Please rate your delivery ( 1 - 5 stars): "))
                
                #Check if the rating is within the valid range from 1 to 5
                if 1 <= rating <=5:
                    print(f"Thank you for your feedback! You rated us {rating} stars")
                    break # Exit the loop after receiving valid input
                else: 
                    print("Please enter a valid rating between 1 and 5")
            # Handle cases where input is not a valid integer
            except ValueError:
                print("Invalid input. Please enter a number from 1 and 5")


    # Method that searches for menu items below a specific price
    def search_items_by_price(self, max_price):
        print(f"\nItems under ${max_price:.2f}:")
        # Use list to find items that cost less than or equal to max_price
        found_items = [item for item, price in self.prices.items() if price <= max_price]
        
        # Check if any items were found within the given price range
        if found_items:
            # Loop through and display each item with its price
            for item in found_items:
                print(f"- {item}: ${self.prices[item]:.2f}")
        else:
            # If no items are found, print a message
            print("No items found within that price range.")


# Main method is executed as soon as the program runs
def main():
    # Create a new delivery object - instantiating a new object
    delivery = DunnDelivery()
    # Show menu
    delivery.show_menu("Coffee Drinks")
    
    while True:
        location = input("\nEnter your delivery location (Library, Academic Success Center, ITEC Computer Lab): ")
        if location in delivery.delivery_locations:
            break
        print("Invalid location. Please enter a valid option.")

    current_hour = int(input("Enter current hour (24-hour format): "))
    has_student_id = input("Do you have a student ID? (yes/no): ").strip().lower() == "yes"
    priority_delivery = input("Would you like priority delivery for an extra $2? (yes/no): ").strip().lower() == "yes"
    
    print("\nEnter items to order (type 'done' when finished):")
    order = []
    while True:
        item = input("> ").strip()
        if item.lower() == "done":
            break
        if item in delivery.prices:
            order.append(item)
        else:
            print(f"'{item}' is not available. Please choose from the menu.")

    if order:
        delivery.print_order(location, order, current_hour, has_student_id, priority_delivery)
        delivery.rate_delivery()
          
    
    # Allow user to search for affordable items
    budget = float(input("\nEnter a maximum price to search for affordable items: "))
    delivery.search_items_by_price(budget)

    # Sample order at 9:30 AM (peak morning hour)
    #order = ["Latte", "Bagel"]
    
    # Display receipt for the order
    #delivery.print_order("ITEC Computer Lab", order, 9, has_student_id=True)

if __name__ == "__main__":
    main()