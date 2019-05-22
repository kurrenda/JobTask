import csv

class CountGender:

    def average2(self):
        with open(self.filename, 'r', encoding='windows-1250') as csvfile:
            document = csv.DictReader(csvfile, delimiter=';')
            count = 0
            counter = 0
            if self.year <= 2018 and self.year >= 2010:
                for row in document:
                    if row['Płeć '] == self.gender:
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

    def percent2(self):
        with open(self.filename, 'r', encoding='windows-1250') as csvfile:
            document = csv.DictReader(csvfile, delimiter=';')
            countAll = 0
            countPassed = 0
            if self.year <= 2018 and self.year >= 2010:
                for row in document:
                    if row['Płeć '] == self.gender:
                        if self.province == row['Terytorium'] and self.province != 'Polska':
                            yearInt = int(''.join(map(str, row['Rok'])))
                            if yearInt <= self.year:
                                if row['Przystąpiło/zdało '] == 'przystąpiło':
                                    peopleIntAll = int(''.join(map(str, row['Liczba osób'])))
                                    countAll += peopleIntAll
                                if row['Przystąpiło/zdało '] == 'zdało':
                                    peopleIntPassed = int(''.join(map(str, row['Liczba osób'])))
                                    countPassed += peopleIntPassed

                if (countAll != 0):
                    result = (countPassed / countAll) * 100.0
                    print(self.year, "-", round(result))
            else:
                print("Podałeś zły rok lub złą nazwę województwa(zakres 2010-2018)")




