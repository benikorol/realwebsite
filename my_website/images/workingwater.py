import matplotlib.pyplot as pltw
import matplotlib.pyplot as pltp
import csv

x=[]
y=[]

with open('wc1.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[2]))

pltw.figure(1)
pltw.plot(x,y, marker='.')

pltw.title('Water Consumption of NY')

pltw.xlabel('Year')
pltw.ylabel('Water Consumption per day in Millions of Gallons')




x=[]
y=[]

with open('wc1.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))


pltp.figure(2)
pltp.plot(x,y, marker='o')

pltp.title('Population of NY')

pltp.xlabel('Year')
pltp.ylabel('Population')

pltp.show()
