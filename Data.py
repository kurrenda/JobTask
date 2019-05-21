import csv


class data:

    def exercise1(self,filename,year):
        with open(filename, 'r', encoding='windows-1250') as csvfile:
            document = csv.DictReader(csvfile, delimiter=';')
            count = 0
            if year <= 2018 and year >= 2010:
                counter = 0
                for row in document:
                    yearInt = int(''.join(map(str, row['Rok'])))
                    if yearInt <= year:
                        peopleInt = int(''.join(map(str, row['Liczba osób'])))
                        counter += 1
                        count += peopleInt
                        result = count/counter
                print(year,"-", result)
            else:
                print("Podaj poprawny rok. Zakres 2010 - 2018")





d = data()
d.exercise1('dane.csv',2013)
