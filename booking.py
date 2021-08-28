import calendar
import datetime
import pandas as pd

def make_appointment(y, m, d):
    booking = datetime.date(y, m, d)

    df = pd.DataFrame(pd.read_csv('cal.csv'))
    now = datetime.date.today()
    lis_reader = []
    counter=0

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
        for i in df.appointment:
            time_reader = datetime.datetime.strptime(i, '%Y-%m-%d')
            lis_reader.append(time_reader)

        for i in lis_reader:
            if y == i.year and m == i.month and d == i.day:
                counter=counter+1
        if counter == 3:
            print('you cannot select this date')
            return 1# checking for already selected date



        else:
            df2 = pd.DataFrame({'appointment': [str(booking)]})
            df = df.append(df2, ignore_index=True)

            df.to_csv('cal.csv', index=False)
            print('you have booked')

def avaiability_days(y, m):
    df = pd.DataFrame(pd.read_csv('cal.csv'))
    lis_reader = []
    all_current_month_booked_days = []

    cal = calendar.Calendar()
    all_days = cal.monthdayscalendar(y, m)
    all_days_clean = []

    for row in all_days:
        for i in row:
            if i != 0:
                all_days_clean.append(i)  # all the days in month given in input to the function

    for i in df.appointment:
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

    if all_days_clean == []:
        return 42
    return all_days_clean


def avaiability_entire_year(year, month):
    control = avaiability_days(year,
                               month)  ### completare la funzione tenendo in conto la situa di quando tutti i mesi sono booked e quindi cambi anno

    while control == 42:
        month = month + 1

        control = avaiability_days(year, month)

        if month == 12 and control == 42:
            return 42
            break

    return month, avaiability_days(year, month)