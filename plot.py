import matplotlib.pyplot as plt

listHour = [0] * 24
list10They = [0] * 24
list10Us = [0] * 24
count = 0

with open("1") as fN:
    for lineN in fN:
        a = lineN.split(",")
        if(a[0] != 'Hour'):
            print a
            listHour[count] = int(a[0])
            list10They[count] = int(a[2])
            list10Us[count] = int(a[3])
            count = count +1
fN.close();

plt.plot(listHour, list10They)
plt.plot(listHour, list10Us)
plt.ylabel('some numbers')
plt.show()