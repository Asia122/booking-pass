import datetime
import pandas as pd

y = 2021  # int(input('inserisci anno'))
m = 8  # int(input('inserisci mese'))
d = 30  # int(input('inserisci giorno'))


def make_appointment(y, m, d):
    booking = datetime.date(y, m, d)

    df = pd.DataFrame(pd.read_csv('cal.csv'))
    now = datetime.date.today()
    lis_reader = []

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
            if y == i.year and m == i.month and d == i.day:  # checking for already selected date
                print('you cannot select this date')
                return 1

        else:
            df2 = pd.DataFrame({'appointment': [str(booking)]})
            df = df.append(df2, ignore_index=True)

            df.to_csv('cal.csv', index=False)
            print('you have booked')
