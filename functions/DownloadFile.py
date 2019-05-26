#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sqlite3


def download():
    conn = sqlite3.connect('my.db')

    cursor = conn.cursor()

    cursor.execute("select * from t;")
    with open("daneDownload.csv", "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description]) # write headers
        csv_writer.writerows(cursor)

    print("Plik pomyślnie został pobrany!")