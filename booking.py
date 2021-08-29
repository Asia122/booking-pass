import calendar
import datetime
import pandas as pd

'''
This module enables to book an appointment for a ... 
and to check the available dates to book
'''



def make_appointment(y, m, d):
    '''
    This function takes as input the year,the month and the day, and tries to book
    an appointment for that date, if that date is not available for any reason it will return 1.
    If the date is available then it will modify the csv and add the selected date in the column appointment
    '''

    booking = datetime.date(y, m, d)

    df = pd.DataFrame(pd.read_csv('people_vaccinated.csv'))
    now = datetime.date.today()
    lis_reader = []
    counter=0
    # 
    if y < now.year:
        print('you cannot select previous years')
        return 1
    elif m < now.month:
        print('you cannot select previous month')
        return 1
    elif d < now.day:
        print('you cannot select previous days')  ## checking for previous date
        return 1
    elif y == now.year and m == now.month and d == now.day:  # checking for current date
        print('you cannot select current date')
        return 1
    else:
        for i in df["Date First Shot"]:
            time_reader = datetime.datetime.strptime(i, '%Y-%m-%d')
            lis_reader.append(time_reader)

        for i in lis_reader:
            if y == i.year and m == i.month and d == i.day:
                counter=counter+1
        if counter == 3:
            print('you cannot select this date')
            return 1# checking for already selected date



        else:
            df2 = pd.DataFrame({'Date First Shot': [str(booking)]})
            df = df.append(df2, ignore_index=True)

            df.to_csv('people_vaccinated.csv', index=False)
            print('you have booked')

def avaiability_days(y, m):

    '''
    This function takes a year and a month as input and returns the available days
    of that month. It takes in to account up to 3 people booking the same date.
    If the entire month is booked it will return 42
    '''

    df = pd.DataFrame(pd.read_csv('people_vaccinated.csv'))
    lis_reader = []
    all_current_month_booked_days = []
    now=datetime.date.today()
    cal = calendar.Calendar()
    all_days = cal.monthdayscalendar(y, m)
    all_days_clean = []

    for row in all_days:
        for i in row:
            if i != 0:
                all_days_clean.append(i)  # all the days in month given in input to the function

    for i in df["Date First Shot"]:
        time_reader = datetime.datetime.strptime(i, '%Y-%m-%d')
        lis_reader.append(time_reader)  # creates a list of datetime object of all the booked date

    for i in lis_reader:
        if i.month == m:
            all_current_month_booked_days.append(i.day)  # list of all the  month booked days

    all_current_month_booked_days.sort()



    for booked_day in all_current_month_booked_days:
        counter = [i for i, day in enumerate(all_current_month_booked_days) if day == booked_day]  # => [1, 3]
        if booked_day in all_days_clean and len(counter) >= 3:
            all_days_clean.remove(booked_day)

    if m == now.month:   # consider also current date
        for day in range(1,now.day+1):
            if day not in all_days_clean:
                continue
            all_days_clean.remove(day)

    if all_days_clean == []:
        return 42
    return all_days_clean


def avaiability_entire_year(year, month):

    '''
    This function takes a year and a month as input and checks the next available date
    that are the closest to that month. If all the months are booked returns 42
    '''

    control = avaiability_days(year,
                               month)  ### completare la funzione tenendo in conto la situa di quando tutti i mesi sono booked e quindi cambi anno

    while control == 42:
        month = month + 1

        control = avaiability_days(year, month)

        if month == 12 and control == 42:
            return 42
            break

    return month, avaiability_days(year, month)

print(avaiability_days(2021,8))
