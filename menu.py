# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# List to keep track of the order
order = []

# Start interaction with the customer
print("Welcome to the variety food truck.")

# Main loop for ordering process
place_order = True
while place_order:
    # Prompt for menu category
    print("From which menu would you like to order? ")

    # Initialize a counter for menu items
    i = 1
    # Dictionary to link menu numbers to categories
    menu_items = {}

    # Display menu categories
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    # Get customer's menu category choice
    menu_category = input("Type menu number: ")

    # Validate input and proceed if valid
    if menu_category.isdigit():
        if int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            print(f"You selected {menu_category_name}")

            # Display items within the chosen category
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            
            # Ask for item number and validate
            menu_selection = input("Enter the item number you'd like to order: ")

            if menu_selection.isdigit():
                menu_selection = int(menu_selection)

                if menu_selection in menu_items.keys():
                    selected_item = menu_items[menu_selection]
                    print(f"You selected {selected_item['Item name']}")

                    # Ask for quantity and set default if necessary
                    quantity = input(f"How many {selected_item['Item name']} would you like? (Default is 1 if left blank): ")

                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        quantity = 1

                    # Add selected item to the order
                    order.append({
                        "Item name": selected_item['Item name'],
                        "Price": selected_item['Price'],
                        "Quantity": quantity
                    })
                else:
                    print("Invalid selection, please choose a valid item number.")
            else:
                print("Please enter a number.")

        else:
            print(f"{menu_category} was not a menu option.")
    else:
        print("You didn't select a number.")

    while True:
        # Prompt to continue or finish the order
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()

        if keep_ordering == 'y':
            break
        elif keep_ordering == 'n':
            place_order = False
            print("Thank you for your order!")
            break
        else:
            print("Please enter 'Y' or 'N'.")

# Display the final order
print("This is what we are preparing for you.\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# Loop through the order and print each item
for item in order:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]

    num_item_spaces = 24 - len(item_name)
    item_spaces = " " * num_item_spaces
    
    print(f"{item_name}{item_spaces} | ${price:.2f}  | {quantity}")

# Calculate and display the total cost
total_price = sum([item["Price"] * item["Quantity"] for item in order])
print(f"\nTotal price: ${total_price:.2f}")
