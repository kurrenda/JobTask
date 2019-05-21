import Data


def main():

    name = input("Podaj nazwę swojego pliku: ")
    start = 1

    while start >= 0:
        genderMode = 0
        if genderMode == 0:
            question = 0
            if question == 0:
                print("Wróciłeś do menu, napisz co chcesz zrobić 1,2,3: ")
                answer= int(input())
                question = answer
            if question == 1:
                getYear = int(input("Proszę podaj Rok: "))
                getProvince = input("Proszę podaj województwo:  ")
                answer = Data.Count(name,getYear,getProvince)
                answer.average()
                question = 0
            if question == 3:
                gender = int(input("Proszę wybierz płeć (mężczyźni/kobiety/wszyscy): "))
                if gender == 1:
                    genderMode = 1

        if genderMode == 1:
            question = 0
            if question == 0:
                print("Filtr kobiet włączony, napisz co chcesz zrobić 1,2,3: ")
                answer = int(input())
                question = answer
            if question == 1:
                getYear = int(input("Proszę podaj Rok: "))
                getProvince = input("Proszę podaj województwo:  ")
                answer = Data.Count(name, getYear, getProvince)
                answer.average()
                question = 0
            if question == 3:
                gender = input("Proszę wybierz płeć (mężczyźni/kobiety/wszyscy): ")
                genderMode = 1



if __name__=="__main__":
    main()