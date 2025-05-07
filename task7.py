import csv
csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_NONE, quotechar='%')
# with open('test_csv.csv', 'w') as csvfile:
#     csvfile.write("Ivan,Petrow,30\n")
#     csvfile.write("Petr,Ivanow,35\n")
#     csvfile.write("Petya,Govnnov,33\n")

# with open('test_csv.csv', 'r') as csvfile:
#     csv_body = csvfile.read()
#     rows = csv_body.split('\n')
#     for i in rows:
#         print(i.split(','))


# with open('test_csv1.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, myDialect)
#     writer.writerow(["Ivan","Petrow","30,6"])

# with open('test_csv1.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
#     for row in reader:
#         print(row)
#
# print(csv.list_dialects())

# with open('test_csv2.csv', 'w') as csvfile:
#     headers = ['name', "second", 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=headers)
#     writer.writeheader()
#     writer.writerow({'name': "Ivan", "second": "Petrow", 'age': "30,6"})

with open('test_csv2.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)


with open('test_csv2.csv', 'r') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read())
    print(dialect.delimiter)
    print(dialect.quotechar)
    print(dialect.quoting)
