import pandas as pd

def check_avaiability():
    
# this function looks if in the column bookings and see if there are some 0 values
# if there are 0 values means that that place is avaible to book a vaccine
    
    df = pd.DataFrame(pd.read_csv('calendar.csv'))
    lis=df.bookings == 0
    for i,s in enumerate(lis.values):
        if s:
            print('september',df.September[i],'is avaible')
            # the output is a print for now, but I can easly change it to output the index
            # of the column 
            return i
           


def book(i):

# this function wants an index and at that indez changes the value in column 
# booking to 1 to create the appointment
    
    df = pd.DataFrame(pd.read_csv('calendar.csv'))
    df.bookings[i]=1
    print('you have booked for semptember',df.September[i])
    df.to_csv('calendar.csv',index=False)
    
