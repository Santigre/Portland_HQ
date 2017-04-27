from datetime import datetime, time
import pytz

t = datetime.now() # Datetime.now gets the current time and date makes it equal to t
z = datetime.now(pytz.utc) # pyts allows me to access other time zones.
now_t = t.time() # Gets the current time of t
now_z = z.time() # Gets the current time of z
work_day = datetime.today().weekday() # Gets the day of the week and assigns it a value(0-6)
#monday = 0 sunday = 6


def weekday():
    if work_day in range(0,4): #Checks if the day is between monday and friday
        print('Its a work day')#If its true then it prints the message and calls next function
        portland_time()
    else: 
        print('Its not a work day. Take a break')

        
def portland_time():
    print('portland date and time: ')
    print(t)
    if now_t >= time(9,0) and now_t <= time(21,00): # Checks if the current time is between 9am and 9pm
        print('Its open!!')
    else:
        print('Closed! Come back between 9am and 9pm')
    newyork_time()


def newyork_time():
    ny = z.astimezone(pytz.timezone('US/Eastern')) # Gets the current time of the timezone US/Eastern
    print('New York date and time: ')
    print(ny)
    if now_z >= time(9,0) and now_z <= time(21,00): # Checks if the current time is between 9am and 9pm
        print('Its open!!')
    else:
        print('Closed! Come back between 9am and 9pm')
    london_time()
                    
def london_time(): # London has two diffrent time zones depending on day light savings. Only went with one for now
    lond = z.astimezone(pytz.timezone('Europe/London')) # Gets the current time of the timezone Europe/London
    print('London date and time: ')
    print(lond)
    if now_z >= time(9,0) and now_z <= time(21,00): # Checks if the current time is between 9am and 9pm
        print('Its open!!')
    else:
        print('Closed! Come back between 9am and 9pm')


weekday() # Calls the first function to visualize it in the shell


