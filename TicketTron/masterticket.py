SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

# Create the calculate_price_function. It takes number of tickets and returns num_tickets * TICKETS_PRICE
def calculate_price(number_of_tickets):
    # Create a new constant for the 2 dolar service charge
    return (number_of_tickets * TICKETS_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining".format(tickets_remaining))
    name = input("What is your name?  ")
    num_tickets = input("How many tickets would you like, {}?  ".format(name))
    #Expect a ValueError to happen and handle it apporpriately...remember to test it out!
    try:
        num_tickets = int(num_tickets)
        # Raise a ValueError if the request is for more tickets than are available
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {}".format(tickets_remaining))
    except ValueError as err:
        print("Oh no we ran into an issue. {}. Please try again".format(err))
    else:
        total_price = calculate_price(num_tickets)
        print("Your total price will be ${}".format(total_price))
        should_proceed = input("Do you want to proceed?  ")
        if should_proceed.lower() == "y":
            # TODO: Gather credit card information and process it.
            print("SOLD!")
            tickets_remaining = tickets_remaining - num_tickets
        else:
            print("Thank you for your purchase {}".format(name))
print("Sorry we are sold out :( ")