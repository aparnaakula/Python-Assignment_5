class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parkingSpaces = list(range(1, total_parking_spaces + 1))
        self.currentTicket = {}

    def takeTicket(self):
        if not self.parkingSpaces:
            print("Sorry, the parking is full. No available spaces.")
            return

        ticket = self.tickets.pop(0)
        space = self.parkingSpaces.pop(0)
        self.currentTicket = {'ticket': ticket, 'space': space, 'paid': False}
        print(f"Ticket {ticket} issued. Park in space {space}.")

    def payForParking(self):
        if not self.currentTicket:
            print("No ticket taken. Please take a ticket first.")
            return

        amount = input("Enter the amount to pay: ")
        if amount:
            self.currentTicket['paid'] = True
            print("Ticket has been paid. You have 15 minutes to leave.")

    def leaveGarage(self):
        if not self.currentTicket:
            print("No ticket taken. Please take a ticket first.")
            return

        if self.currentTicket['paid']:
            print("Thank you, have a nice day!")
        else:
            amount = input("Your ticket has not been paid. Please enter the payment amount: ")
            if amount:
                print("Thank you, have a nice day! (Ticket paid)")

        self.parkingSpaces.append(self.currentTicket['space'])
        self.tickets.append(self.currentTicket['ticket'])
        self.currentTicket = {}

garage = ParkingGarage(2, 2)

def run():
    while True:
        response = input('Please enter: Take ticket/ Pay for parking/ Leave garage: ')
        if response.lower() == 'take ticket':
            garage.takeTicket()
        elif response.lower() == 'pay for parking':
            garage.payForParking()
        elif response.lower() == 'leave garage':
            garage.leaveGarage()
            break

run()


# Example usage:
# garage = ParkingGarage(total_tickets=2, total_parking_spaces=2)

# for _ in range(2):
# garage.takeTicket()

# Attempting to take a ticket when parking is full
# garage.takeTicket()
