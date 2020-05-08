#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    my_hash = {}
    route = []
    for ticket in tickets:
        my_hash[ticket.source] = ticket.destination

    current_ticket = my_hash["NONE"]

    while True:
        route.append(current_ticket)
        
        if current_ticket == "NONE":
            break

        current_ticket = my_hash[current_ticket]
        


    return route
