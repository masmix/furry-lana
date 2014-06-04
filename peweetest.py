import peewee
import find_sections
from peewee import *

db = MySQLDatabase('baza_test_python', user='bazek',passwd='ve7128')

class Info(peewee.Model):
    data = DateField(db_column='Data')
    godz = CharField(max_length=10, db_column='Godz')
    kod = CharField(max_length=10, db_column='Kod')
    kodowanie = TextField(db_column='Kodowanie')
    konto = TextField(db_column='Konto')
    miasto = TextField(db_column='Miasto')
    nazwa = TextField(db_column='Nazwa')
    nip = CharField(max_length=20, db_column='Nip')
    program = TextField(db_column='Program')
    id = BigIntegerField(primary_key=True)

    class Meta:
        database = db

#Info.create_table()
fields = find_sections.returnDictFromFile()
#fields={'godz': ' 9:05:00', 'konto': '', 'program': 'SMALL BUSINESS 5.1.3021.4980', 'nazwa': 'RZEPKA Pruszowice ul.Sloneczna 13          tel.071 31 54 603, e-mail: wkn@wp.pl', 'nip': '911-167-70-58', 'data': '14.04.24', 'kod': '51-217', 'kodowanie': 'Windows 1250', 'miasto': 'Pruszowice'}


sq = Info.insert_many([fields])
sq.execute()
print fields
#iq = InsertQuery(Info, fields)
#iq.execute()

#info = Info(program="SMALL", kodowanie="Windows")
#info.save()
#for info in Info.filter(program="SMALL BUSINESS 5.1.3021.4980"):
#	print info.Kodowanie


#Book.create_table()
#book = Book(author="me", title='Peewee is cool')
#book.save()
#for book in Book.filter(author="me"):
#    print book.title


