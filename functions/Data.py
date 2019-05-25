import csv


class Count:

    def __init__(self,filename):
        self.filename = filename


    def average(self, year, province):
        with open(self.filename, 'r', encoding='windows-1250') as csvfile:
            document = csv.DictReader(csvfile, delimiter=';')
            count = 0
            counter = 0
            if year <= 2018 and year >= 2010:
                for row in document:
                    if row['Terytorium'] == province:
                        if row['Przystąpiło/zdało '] == 'przystąpiło':
                            yearInt = float(''.join(map(str, row['Rok'])))
                            if yearInt <= year:
                                peopleInt = float(''.join(map(str, row['Liczba osób'])))
                                counter += 1
                                count += peopleInt
                if counter != 0:
                    result = count / counter
                    print(year, "-", round(result))
                    return round(result)
            else:
                print("Podałeś zły rok lub złą nazwę województwa(zakres 2010-2018)")


    def percent(self,year,province):
        with open(self.filename, 'r', encoding='windows-1250') as csvfile:
            document = csv.DictReader(csvfile, delimiter=';')
            countAll = 0
            countPassed = 0
            if year <= 2018 and year >= 2010:
                for row in document:
                    if province == row['Terytorium'] and province != 'Polska':
                        yearInt = float(''.join(map(str, row['Rok'])))
                        if year == yearInt:
                            if row['Przystąpiło/zdało '] == 'przystąpiło':
                                peopleIntAll = float(''.join(map(str, row['Liczba osób'])))
                                countAll += peopleIntAll
                            if row['Przystąpiło/zdało '] == 'zdało':
                                peopleIntPassed = float(''.join(map(str, row['Liczba osób'])))
                                countPassed += peopleIntPassed

                if(countAll != 0):
                    result = float((countPassed/countAll) * 100.0)
                    return round(result)
            return 0

    def percentPrint(self, year, province):
        with open(self.filename, 'r', encoding='windows-1250') as csvfile:
            document = csv.DictReader(csvfile, delimiter=';')
            countAll = 0
            countPassed = 0
            if year <= 2018 and year >= 2010:
                for row in document:
                    if province == row['Terytorium'] and province != 'Polska':
                        yearInt = float(''.join(map(str, row['Rok'])))
                        if year == yearInt:
                            if row['Przystąpiło/zdało '] == 'przystąpiło':
                                peopleIntAll = float(''.join(map(str, row['Liczba osób'])))
                                countAll += peopleIntAll
                            if row['Przystąpiło/zdało '] == 'zdało':
                                peopleIntPassed = float(''.join(map(str, row['Liczba osób'])))
                                countPassed += peopleIntPassed

                if (countAll != 0):
                    result = float((countPassed / countAll) * 100.0)
                    print(year,"-",round(result),"%")
            else:
                print("Syntax Error")



    def bestPass(self, year):
        with open(self.filename, 'r', encoding='windows-1250') as csvfile:
            document = csv.DictReader(csvfile, delimiter=';')
            result = 0
            if year <= 2018 and year >= 2010:
                for row in document:
                    province = row['Terytorium']
                    temp = self.percent(year, province)
                    if temp > result:
                        provinceResult = province
                        result = temp
                print(provinceResult,result)
                return(result)

    def bestProvince(self):
        with open(self.filename, 'r', encoding='windows-1250') as csvfile:
            document = csv.DictReader(csvfile, delimiter=';')
            data = list(document)
            provincesList = []
            for y in data:
                if y["Terytorium"] != "Polska":
                    provinces = y["Terytorium"]
                    provincesList.append(provinces)

            dataSet = set(provincesList)
            listdataSet = list(dataSet) #lista wszystkich województw

            for i in listdataSet:
                tempList = {}
                for y in range(2010, 2019):
                    passed = 0
                    attended = 0
                    for x in data:
                        if x["Rok"] == str(y):
                            if x["Terytorium"] == str(i):
                                if x["Przystąpiło/zdało "] == "zdało":
                                    passedInt = float(x["Liczba osób"])
                                    passed += passedInt

                                if x["Przystąpiło/zdało "] == "przystąpiło":
                                    attendedInt = float(x["Liczba osób"])
                                    attended += attendedInt


                    result = round((passed/attended) * 100)
                    tempList[y] = result

                print(i)
                for z in range(2010,2018):
                    if tempList[z] > tempList[z+1]:
                        print(z,"-", tempList[z],"%", ">", (z + 1), "=", tempList[z + 1],"%")




    def compareProvince(self, province1, province2):
        with open(self.filename, 'r', encoding='windows-1250') as csvfile:
            document = csv.DictReader(csvfile, delimiter=';')
            data = list(document)
            for y in range(2010,2019):
                accededAll = 0
                passed = 0
                accededAll2 = 0
                passed2 = 0
                for x in data:
                    if x["Rok"] == str(y):
                        if x["Terytorium"] == str(province1):
                            if x["Przystąpiło/zdało "] == "przystąpiło":
                                accededIntAll = int(x["Liczba osób"])
                                accededAll += accededIntAll
                            if x["Przystąpiło/zdało "] == "zdało":
                                passedInt = int(x["Liczba osób"])
                                passed += passedInt
                        if x["Terytorium"] == str(province2):
                            if x["Przystąpiło/zdało "] == "przystąpiło":
                                accededIntAll2 = int(x["Liczba osób"])
                                accededAll2 += accededIntAll2
                            if x["Przystąpiło/zdało "] == "zdało":
                                passedInt2 = int(x["Liczba osób"])
                                passed2 += passedInt2
                if accededAll != 0 and accededAll2 != 0:
                    result = round((passed/accededAll) * 100)
                    result2 = round((passed2 / accededAll2) * 100)
                    if result > result2:
                        print(y,province1)
                    elif result < result2:
                        print(y,province2)
                    else:
                        print(y,"Oba mają taki sam wynik",province1, result,"%", province2, result2 ,"%" )







