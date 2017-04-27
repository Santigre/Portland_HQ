
from datetime import datetime, time
import pytz

z = datetime.now(pytz.utc)
t = datetime.now()
now_t = t.time()
now_z = z.time()

def portland_time():
    print('portland date and time: ')
    print(t)
    if now_t >= time(9,0) and now_t <= time(21,00):
        print('Its open!!')
    else:
        print('Closed! Come back between 9am and 9pm')
    newyork_time()


def newyork_time():
    ny = z.astimezone(pytz.timezone('US/Eastern'))
    print('New York date and time: ')
    print(ny)
    if now_z >= time(9,0) and now_z <= time(21,00):
        print('Its open!!')
    else:
        print('Closed! Come back between 9am and 9pm')
    london_time()

def london_time():
    lond = z.astimezone(pytz.timezone('Europe/London'))
    print('London date and time: ')
    print(lond)
    if now_z >= time(9,0) and now_z <= time(21,00):
        print('Its open!!')
    else:
        print('Closed! Come back between 9am and 9pm')


portland_time()


