import csv
import re

arg1 = input("search by string: ")

text = ""
booklist = []
prevbook = "Book Name"
books = ""

with open("kjv.csv", mode='r', encoding="UTF-8") as f:
    mycsv = csv.reader(f)

    if arg1 != "books":
        for row in mycsv:

            if re.search(arg1, row[5]):
                print(f"{row[1]} {row[3]}:{row[4]} {row[5]}")