import calendar
import datetime
from datetime import datetime
from datetime import date
import pandas as pd

"""
This module provides with functions that, working together,
enables to choose and return a suitable date for the vaccination.
There are 3 functions that are then grouped
by calling the select_date function.
"""


def availability_days(y_ear, m_onth):
    """
    This function takes a year and a month as input
    and returns the available days
    of that month.
    It takes in to account up to 3 people
    booking the same date.
    If the entire month is booked it will return 42
    """

    frame = pd.DataFrame(pd.read_csv("people_vaccinated.csv"))
    lis_reader = []
    all_current_month_booked_days = []
    now = date.today()
    cal = calendar.Calendar()
    all_days = cal.monthdayscalendar(y_ear, m_onth)
    all_days_clean = []
    # this cycle will create a list (all_days_clean) of all the days
    # in the month given in input to the function
    for row in all_days:
        for i in row:
            if i != 0:
                # all the days in the month given in input to the function
                all_days_clean.append(i)

    for i in frame["Date First Shot"]:
        time_reader = datetime.strptime(i, "%d/%m/%Y")
        #  creates a list of datetime objects of all the booked dates
        lis_reader.append(time_reader)

    for i in lis_reader:
        if i.month == m_onth:
            # list of all the  month booked days
            all_current_month_booked_days.append(i.day)

    all_current_month_booked_days.sort()

    for booked_day in all_current_month_booked_days:
        counter = [
            i
            for i, day in enumerate(all_current_month_booked_days)
            if day == booked_day
        ]
        if booked_day in all_days_clean and len(counter) >= 3:
            # removing to all the days of the month only the ones that have
            # already been booked 3 times
            all_days_clean.remove(booked_day)

    # consider also current date, so to delete passed days to the availability
    if m_onth == now.month:
        for day in range(1, now.day + 1):
            # here check for passed fully booked days (3 times booked days)
            if day not in all_days_clean:
                continue
            all_days_clean.remove(day)

    if all_days_clean == []:
        return 42
    return all_days_clean


def availability_entire_year():
    """
    This function, through the usage of availability_days,
    checks the next available dates
    that are the closest to the current day
    and returns the available dates up to 2 months.
    If all the months are booked returns 42
    """
    now = date.today()
    year = now.year
    month = now.month
    # recall of availability_days
    control = availability_days(year, month)

    # this cycle is needed to check what months are fully booked
    while control == 42:
        month = month + 1

        control = availability_days(year, month)

        if month == 12 and control == 42:
            # if True means that while iterated
            # for all the month up to december
            # and that december is fully booked hence the entire year is booked
            return 42

    # list of the available days of the current/next not fully booked month
    availability_1 = availability_days(year, month)
    if month + 1 <= 12:
        # this if statement does not enable
        # to create availability_2 as it's not needed.
        # If True will cause errors and problems with the other code
        # list of the available days of the month after the ones we are
        # analyzing
        availability_2 = availability_days(year, month + 1)
    else:
        availability_2 = 42

    if availability_2 == 42 or month == 12:
        # if the next month is fully booked
        # or the month we are analyzing is september
        # return only the availability of the month we are analyzing
        days_available_1 = [date(year, month, day) for day in availability_1]

        return days_available_1

    days_available_2 = [date(year, month + 1, day)
                        for day in availability_2]
    days_available_1 = [date(year, month, day)
                        for day in availability_1]

    return days_available_1 + days_available_2


def select_date():
    """
    This function, through the use of availability_entire_year
    shows the available days to book and
    let the user choose one.
    If the entire year is booked
    it will show the available days  of January of the next year.
    If also January is completely booked
    it will print a message and returns 42
    """
    now = date.today()
    # recall of availability_entire_year
    date_reader = availability_entire_year()
    dates_available = []

    # this entire if statement does the appropriate checking if the entire
    # year is fully booked
    if date_reader == 42:
        print("the entire year has been booked")

        days_january_next_year = availability_days(now.year + 1, 1)
        # checks for january of the next year
        if days_january_next_year != 42:
            print("this are the available vaccination"
                  " days for january of the next year")
            for day in days_january_next_year:
                print(date(now.year + 1, 1, day).strftime("%d/%m/%Y"))
                dates_available.append(date(now.year + 1, 1, day))

            controller = 0
            # this cycle is iterated until the
            # user give as input one of the available dates previously given as
            # output
            while controller == 0:
                print("select one of the available vaccination date")
                year = int(input("input the year"))
                month = int(input("input the month"))
                day = int(input("input the day"))
                booking = date(year, month, day)
                if booking not in dates_available:
                    print(
                        "this date is not available for the moment "
                        "please select an available vaccination date"
                    )

                else:
                    controller = controller + 1
            return booking.strftime("%d/%m/%Y")


        print(
            "unfortunately also january of the next year"
            " has been booked completely "
            "please come back after christmas vacation")
        return 42

    # this is the part of the function that works if there are available dates
    # in the current year
    print("These are the available vaccination date")
    for day_reader in date_reader:
        print(day_reader.strftime("%d/%m/%Y"))
        dates_available.append(day_reader.strftime("%d/%m/%Y"))
    controller = 0
    # this cycle is iterated until the
    # user puts in input one of the available dates outputted
    while controller == 0:
        print("select one of the available vaccination dates")
        year = int(input("input the year "))
        month = int(input("input the month "))
        day = int(input("input the day "))

        booking = date(year, month, day)

        if booking not in date_reader:
            print(
                "This date is not available"
                "please select an available vaccination date"
            )

        else:
            controller = controller + 1
    return booking.strftime("%d/%m/%Y")
