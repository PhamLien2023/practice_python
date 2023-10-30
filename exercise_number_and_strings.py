'''
Building on the previous example, let's also assume that you have saved
$918 to fund your newadventure. You wonder how many days you can keep one
server running before your moneyruns out. Of course, you hope your social
network becomes popular and requires 20 servers tokeep up with the demand.
How much will it cost to operate at that point?Write a Python program that
displays the answers to the following questions:
How much does it cost to
operate one server per day?
How much does it cost to operate one server per month?
exercise_number_and_strings per day?
How much does it cost to operate twenty servers per month?
How many days can I operate one server with $918?
'''
cost_per_day = 24* 0.51
cost_per_month = 30 * cost_per_day

cost_per_day_of_20_servers = 20* cost_per_day
cost_per_month_of_20_servers = 20* cost_per_month
budget = 918 
operational_budget = budget/cost_per_day
budget = 918 

print (" The cost to operate one server per day: $ {:.2f}.". format (cost_per_day ))
print (" The cost to operate one server per month: $ {:.2f}.". format (cost_per_month))
print (" The cost to operate 20 servers per day: $ {:.2f}.". format (cost_per_day_of_20_servers))
print (" The cost to operate 20 servers per month: $ {:.2f}.". format(cost_per_month_of_20_servers))
print (" The amount of days that I operate one server with % {0} is:{1:.0f} days.".format (budget, operational_budget))
