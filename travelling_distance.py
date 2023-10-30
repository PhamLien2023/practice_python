'''Create a program that asks the user how far they want to travel.
If they want to travel less thanthree miles tell them to walk.
If they want to travel more than three miles, but less than
threehundred miles, tell them to drive. If they want to travel
three hundred miles or more tell them tofly.

Sample Output:How far would you like to travel in miles? 2500
I suggest flying to your destination.
'''
travel_distance = input('How far you want to travel by miles:' )

if int(travel_distance) <= 3:
    print ('I suggest walking to your destination')
elif int (travel_distance) > 3 and int (travel_distance) <= 300 :
    print ('I suggest driving to your destination')

else:
    print ('I suggest flying to your destination')
    
print ('Have a nice trip')
