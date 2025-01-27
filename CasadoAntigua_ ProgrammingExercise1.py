#program that deals with the purchase of tickets
def buying_tickets(availableTickets, ticketMax):
    #initializing variables
    buyerAmount = 0
    desiredTickets = 0

    #loop for each buyer to buy tickets
    while availableTickets > 0:

        #ask how many tickets buyer wants
        try:
            desiredTickets = int(input("How many tickets would you like? (4 per buyer) "))
        except Exception as x:
            print(f"Error: {x}")
            continue


        #input validation
        if desiredTickets <= 0:
            print("Error: Must buy at least 1 ticket")
            continue
        else:
            pass

        #input validation
        if desiredTickets <= ticketMax:
            availableTickets = availableTickets - desiredTickets
            if availableTickets < 0:
                print("Error: Attempt to buy more tickets than available")

                #have to undo the operation
                availableTickets = availableTickets + desiredTickets
                continue
            else:
                print(f" Remaining tickets: {availableTickets}")
        else:
            print("Error: No more than 4 tickets per buyer")
            continue

        buyerAmount += 1

    return buyerAmount


def main():
    #initializing variables
    availableTickets = 20
    ticketMax = 4

    #running function and getting the totalBuyers from it
    totalBuyers = buying_tickets(availableTickets, ticketMax)

    print(f"Amount of buyers: {totalBuyers}")

main()