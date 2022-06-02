#!/usr/bin/env python
# coding: utf-8

# In[3]:


class parkingGarage():
    
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        
    def takeTicket(self):
        print("Please enter. NOTE-When leaving, payment is required to exit.")
        del self.tickets[0]
        del self.parkingSpaces[0]
        
    def payForParking(self):
        while self.currentTicket['paid'] == False:
            payment = input("Please select the pay option to exit: Pay/Other. ")
            if payment.lower() == 'pay':
                print("Ticket has been paid, you have 15 minutes to leave. ")
                self.currentTicket['paid'] == True
                break
            else:
                print("Error, please select the pay option to exit. ")
            
    def leaveGarage(self):
        self.currentTicket['paid'] == True
        print("Thank you, have a nice day!")
        self.tickets.append('ticket')
        self.parkingSpaces.append('parking_space')
        self.payForParking()
            


# In[4]:


parking_deck = parkingGarage(['ticket', 'ticket', 'ticket', 'ticket', 'ticket'] , ['ticket', 'ticket', 'ticket', 'ticket', 'ticket'], {'paid':False})

def run():
    while True:
        response = input("Please select one of the following options: Enter/Pay/Leave/Quit ")
        
        if response.lower() == 'enter':
            parking_deck.takeTicket()
        elif response.lower() == 'pay':
            parking_deck.payForParking()
        elif response.lower() == 'leave':
            parking_deck.leaveGarage()
        elif response.lower() == 'quit':
            break
        else:
            print("Please select one of the listed options. ")

run()


# In[ ]:




