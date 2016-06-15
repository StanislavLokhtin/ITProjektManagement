import plotly.plotly as py
import plotly.graph_objs as go
import csv

py.sign_in('stanislavL', '232232Py')

class User(object):
    id = 0
    firstName = ""
    lastName = ""
    email = ""

    def __init__(self, id, firstName, lastName, email):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.days = []
        self.week = []

with open('resources/csv/customer_data.csv') as csvFile:
    userReader = csv.reader(csvFile, delimiter=' ', quotechar='|')
    users = []
    rowsFromFile = []
    started = True
    for row in userReader:
        if not started:
            rowsFromFile.append(row[0])
        else:
            started = False

for row in rowsFromFile:
    columns = []
    [columns.append(x) for x in row.split(';')]
    newUser = User(columns[0],columns[1],columns[2],columns[3])
    users.append(newUser)

with open('resources/csv/smd_week1.csv') as csvFile:
    weekReader = csv.reader(csvFile, delimiter=' ', quotechar='|')
    weekData = []
    rowsFromFile = []
    started = True
    for row in weekReader:
        if not started:
            rowsFromFile.append(row[0])
        else:
            started = False
with open('resources/csv/smd_week2.csv') as csvFile:
    weekReader = csv.reader(csvFile, delimiter=' ', quotechar='|')
    weekData = []
    started = True
    for row in weekReader:
        if not started:
            rowsFromFile.append(row[0])
        else:
            started = False
with open('resources/csv/smd_week3.csv') as csvFile:
    weekReader = csv.reader(csvFile, delimiter=' ', quotechar='|')
    weekData = []
    started = True
    for row in weekReader:
        if not started:
            rowsFromFile.append(row[0])
        else:
            started = False
with open('resources/csv/smd_week4.csv') as csvFile:
    weekReader = csv.reader(csvFile, delimiter=' ', quotechar='|')
    weekData = []
    started = True
    for row in weekReader:
        if not started:
            rowsFromFile.append(row[0])
        else:
            started = False
with open('resources/csv/smd_week5.csv') as csvFile:
    weekReader = csv.reader(csvFile, delimiter=' ', quotechar='|')
    weekData = []
    started = True
    for row in weekReader:
        if not started:
            rowsFromFile.append(row[0])
        else:
            started = False

for row in rowsFromFile:
    columns = []
    [columns.append(x) for x in row.split(';')]
    for user in users:
        if columns[0] == '"' + user.id + '"':
            user.week.append(row)
            for day in range((len(user.week)-1)*7,len(user.week)*7):
                user.days.append([])
                dayOfTheWeek = day % 7
                for i in range(1+dayOfTheWeek*48,48+dayOfTheWeek*48):
                    user.days[day].append(columns[i])

for user in users:
    print('id: ' + user.id)
    print('name: ' + user.firstName + ' ' + user.lastName)
    print('email: ' + user.email)
    user.consumptionOnOneDay = [0, 0, 0, 0, 0, 0]
    for i in range(0, 5):
        print("week: " + str(i+1) + " - " + str(user.week[i]))
    for i in range(0, 35):
        #print("day: " + str(i+1) + " - " + str(user.days[i]))
        for t in range(0, len(user.days[i])):
            user.consumptionOnOneDay[i % 6] += float(user.days[i][t].replace(',','.'))
    for i in range(0, 6):
        print("average consumption from " + str(i*4) + " to " + str(i*4+4) + " : " + str(user.consumptionOnOneDay[i]))

timeOfTheDay = ['0 to 4', '4 to 8', '8 to 12', '12 to 16', '16 to 20', '20 to 24']

line1 = go.Scatter(
    x = timeOfTheDay,
    y = users[0].consumptionOnOneDay,
    mode = 'lines',
    name = users[0].firstName
)
line2 = go.Scatter(
    x = timeOfTheDay,
    y = users[1].consumptionOnOneDay,
    mode = 'lines',
    name = users[1].firstName
)
data = [line1, line2]

# Plot and embed in ipython notebook!
py.iplot(data, filename='consumptionDuringOneDay')