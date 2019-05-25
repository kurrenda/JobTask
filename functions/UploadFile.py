import sqlite3, csv


def upload():
    con = sqlite3.connect("my.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE t ('Terytorium','Przystąpiło/zdało ','Płeć ','Rok','Liczba osób');")

    with open('daneApi.csv','r',encoding='windows-1250') as fin:

        dr = csv.DictReader(fin,delimiter=';')
        to_db = [(i['Terytorium'], i['Przystąpiło/zdało '], i['Płeć '], i['Rok'], i['Liczba osób']) for i in dr]

    cur.executemany("INSERT INTO t ('Terytorium','Przystąpiło/zdało ','Płeć ','Rok','Liczba osób') VALUES (?, ?, ?, ?, ?);", to_db)
    con.commit()
    con.close()
    return 1