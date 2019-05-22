import csv


class Count:

    def __init__(self,filename):
        self.filename = filename


    def average(self):
        with open(self.filename, 'r', encoding='windows-1250') as csvfile:
            document = csv.DictReader(csvfile, delimiter=';')
            count = 0
            counter = 0
            if self.year <= 2018 and self.year >= 2010:
                for row in document:
                    if row['Terytorium'] == self.province:
                        if row['Przystąpiło/zdało '] == 'przystąpiło':
                            yearInt = int(''.join(map(str, row['Rok'])))
                            if yearInt <= self.year:
                                peopleInt = int(''.join(map(str, row['Liczba osób'])))
                                counter += 1
                                count += peopleInt
                if counter != 0:
                    result = count / counter
                    print(self.year, "-", round(result))
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
                        yearInt = int(''.join(map(str, row['Rok'])))
                        if year == yearInt:
                            if row['Przystąpiło/zdało '] == 'przystąpiło':
                                peopleIntAll = int(''.join(map(str, row['Liczba osób'])))
                                countAll += peopleIntAll
                            if row['Przystąpiło/zdało '] == 'zdało':
                                peopleIntPassed = int(''.join(map(str, row['Liczba osób'])))
                                countPassed += peopleIntPassed


                if(countAll != 0):
                    result = int((countPassed/countAll) * 100.0)
                    return result
            return 0

    def bestPass(self, year):
        with open(self.filename, 'r', encoding='windows-1250') as csvfile:
            document = csv.DictReader(csvfile, delimiter=';')
            result = 0
            if year <= 2018 and year >= 2010:
                for row in document:
                    province = row['Terytorium']
                    a = self.percent(year, province)
                    if a > result:
                        provinceResult = province
                        result = a
                print(provinceResult,result)


d = Count('dane.csv')
print(d.percent(2013, 'Małopolskie'))
d.bestPass(2013)



















