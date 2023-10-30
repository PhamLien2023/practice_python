'''
Let's assume you are planning to use your Python skills to build a social networking service.
You decide to host your application on servers running in the cloud. You pick a hosting provider
that charges $0.51 per hour. You will launch your service using one server and want to know
how much it will cost to operate per day and per month.
Write a Python programme that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per month?
'''
print (" The cost to operate one server per day:$ {:.2f}.".format (0.51* 24))
print ('The cost to operate one server per year: $ {:.2f}. '.format (0.51*24*365))
