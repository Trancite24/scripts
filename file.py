a = 4218
file = open(str(a)+".csv", "w")

file.write("Hour")
file.write(",")
file.write("pm2.5They")
file.write(",")
file.write("pm10They")
file.write(",")
file.write("pm10Us")
file.write(",")
file.write("pm2.5Us")
file.write("\n")

for x in range(0, 24):
    check = 0
    count1 = 0
    count2 = 0
    pm10 = 0
    pm25 = 0

    with open("N.csv") as fN:

        for lineN in fN:

            strNN = lineN.split(" ")

            Ndate = strNN[0].split("/")
            dN = int(str(int(Ndate[0])) + str(int(Ndate[1])) + str(18))
            if check == 0:
                if dN == a:

                    Ntime = strNN[1].split(",")[0].split(":")[0]
                    NNtime = int(Ntime)

                    if NNtime == x+1:
                        check = 1

                        file.write(str(x))
                        file.write(",")
                        file.write(str(strNN[1].split(",")[11]))
                        file.write(",")
                        file.write(str(strNN[1].split(",")[13]))
                        file.write(",")

    fN.close()

    if check == 0 :
        file.write(str(x))
        file.write(",")
        file.write(str(0))
        file.write(",")
        file.write(str(0))
        file.write(",")

    with open("data.csv") as f:
        for line in f:
            strN = line.split(",")

            dateTime = strN[6].split("T")

            dateValue = dateTime[1]

            b = dateValue.split(":")
            c = b[0] + b[1] + b[2]
            d = int(c)

            if d == a:
                timeVal = dateTime[0].split(":")[0]
                timeV = int(timeVal)

                if timeV == x:
                    pm10_local = int(strN[4])
                    pm25_local = int(strN[5])
                    if pm10_local <= 250 :
                        pm25 = pm25 + pm25_local
                        count1 = count1 + 1
                    if pm25_local <= 250:
                        pm10 = pm10 + pm10_local
                        count2 = count2 + 1
        f.close()

        if pm10 == 0:
            file.write(str(0))
            file.write(",")
        else:
            file.write(str(pm10 / count2))
            file.write(",")

        if pm25 == 0:
            file.write(str(0))
            file.write("\n")

        else:
            file.write(str(pm25 / count1))
            file.write("\n")

file.close()
