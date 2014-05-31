import peewee
from peewee import *

db = MySQLDatabase('baza_test_python', user='bazek',passwd='ve7128')

#class Book(peewee.Model):
#    author = peewee.CharField()
#    title = peewee.TextField()

 #   class Meta:
  #      database = db

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

info = Info(program="SMALL", kodowanie="Windows")
info.save()
for info in Info.filter(program="SMALL BUSINESS 5.1.3021.4980"):
	print info.Kodowanie


#Book.create_table()
#book = Book(author="me", title='Peewee is cool')
#book.save()
#for book in Book.filter(author="me"):
#    print book.title


