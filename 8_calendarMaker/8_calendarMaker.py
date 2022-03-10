import datetime

Days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')

print("please input the year for the calendar:")
# get a year input from user
while True:
    year = input(">")
    if year.isdecimal() and int(year) > 0:
        year = int(year)
        break

    print("please input a numeric year,like 2023.")
    continue


print("please input the month for the calendar:")
# get a month input from user
while True:
    month = input(">")

    if month.isdecimal() and int(month) > 0 and int(month) <= 12:
        month = int(month)
        break

    print("please input a numeric and random in 1 to 12 month ,like 2.")
    continue


# get a calendar with inputing year and month
def getCalendar(year, month):
    calendarText = ''

    # put the month and year at the top of the calendar
    calendarText += " " * 34 + MONTHS[month-1] + " " + str(year) + "\n"

    # add the days of the week labels to the calendar
    calendarText += "...Monday....Tuesday...Wednesday...Thursday.... Friday....Saturday.....Sunday..\n"

    # the horizontal line string that separate weeks
    weekSeparator = ('+----------' * 7) + '+\n'

    # the blank rows have ten spaces in between the | day separators
    blankRow = ('|          ' * 7) + '|\n'

    # get the first date in the month
    currentDate = datetime.date(year,month,1)

    # Roll back currentDate until it is Sunday
    while currentDate.weekday() != 0:
        currentDate -= datetime.timedelta(days=1)

    while True:
        calendarText += weekSeparator

        dayNumberRow = ""
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += "|" + dayNumberLabel + (" " * 8)
            currentDate += datetime.timedelta(days=1)

        dayNumberRow += "|\n"

        calendarText += dayNumberRow
        for i in range(3):
            calendarText += blankRow

        if currentDate.month != month:
            break

    # add the horizontal line at the bottom of the calendar
    calendarText += weekSeparator


    return calendarText
# save the calendar to a text file
calendarText = getCalendar(year,month)
print(calendarText)

calendarFilename = f"calendar_{year}_{month}.txt"
with open(calendarFilename,"w") as fileObj:
    fileObj.write(calendarText)

print("Saved to " + calendarFilename)
