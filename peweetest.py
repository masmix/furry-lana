import peewee
#import find_sections
from peewee import *

db = MySQLDatabase('baza_test_python', user='bazek',passwd='ve7128')

class Start(peewee.Model):
    start = IntegerField(db_column='start')
    
    class Meta:
	database = db

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

class Okres(peewee.Model):
    poczatek = CharField(max_length=45, null=True, db_column='Poczatek')
    koniec = CharField(max_length=45, null=True, db_column='Koniec')

    class Meta:
	database = db


class Paragony(peewee.Model):
    rejestr = CharField(max_length=20, db_column='Rejestr')
    adreskontrahenta = CharField(max_length=100, db_column='AdresKontrahenta')
    bon = FloatField(db_column='Bon')
    brutto = FloatField(db_column='Brutto')
    czek = FloatField(db_column='Czek')
    czyparagon = IntegerField(db_column='CzyParagon')
    datasprzed = CharField(max_length=45, null=True, db_column='DataSprzed')
    datawyst = CharField(max_length=45, null=True, db_column='DataWyst')
    godzina = CharField(max_length=8, db_column='Godzina')
    gotowka = FloatField(db_column='Gotowka')
    identyfikatordok = CharField(max_length=30, db_column='IdentyfikatorDok')
    inicjaly = CharField(max_length=50, db_column='Inicjaly')
    karta = FloatField(db_column='Karta')
    nazwakontrahenta = CharField(max_length=100, db_column='NazwaKontrahenta')
    nazwiskoodbiorcy = CharField(max_length=50, db_column='NazwiskoOdbiorcy')
    netto = FloatField(db_column='Netto')
    nip = CharField(max_length=30, db_column='Nip')
    nrdok = CharField(max_length=20, db_column='NrDok')
    nrfilii = IntegerField(db_column='NrFilii')
    nrkontrahenta = IntegerField(db_column='NrKontrahenta')
    nrpar = CharField(max_length=30, db_column='NrPar')
    nrplatnosci = IntegerField(db_column='NrPlatnosci')
    sposobplatnosci = CharField(max_length=30, db_column='SposobPlatnosci')
    standok = IntegerField(db_column='standok')
    symbolkontrahenta = CharField(max_length=30, db_column='SymbolKontrahenta')
    termin = IntegerField(db_column='Termin')
    typdok = CharField(max_length=45, null=True, db_column='TypDok')
    uid = PrimaryKeyField(db_column='UID')
    uwagi = CharField(max_length=100, db_column='Uwagi')
    vat = FloatField(db_column='Vat')
    vat0_brutto = FloatField(db_column='Vat0_Brutto')
    vat0_bruttozakup = FloatField(db_column='Vat0_BruttoZakup')
    vat0_index = IntegerField(db_column='Vat0_Index')
    vat0_netto = FloatField(db_column='Vat0_Netto')
    vat0_nettozakup = FloatField(db_column='Vat0_NettoZakup')
    vat0_procent = IntegerField(db_column='Vat0_Procent')
    vat0_stawka = CharField(max_length=10, db_column='Vat0_Stawka')
    vat0_vat = FloatField(db_column='Vat0_Vat')
    vat0_vatzakup = FloatField(db_column='Vat0_VatZakup')
    vat1_brutto = FloatField(db_column='Vat1_Brutto')
    vat1_bruttozakup = FloatField(db_column='Vat1_BruttoZakup')
    vat1_index = IntegerField(db_column='Vat1_Index')
    vat1_netto = FloatField(db_column='Vat1_Netto')
    vat1_nettozakup = FloatField(db_column='Vat1_NettoZakup')
    vat1_procent = IntegerField(db_column='Vat1_Procent')
    vat1_stawka = CharField(max_length=10, db_column='Vat1_Stawka')
    vat1_vat = FloatField(db_column='Vat1_Vat')
    vat1_vatzakup = FloatField(db_column='Vat1_VatZakup')
    vat2_brutto = FloatField(db_column='Vat2_Brutto')
    vat2_bruttozakup = FloatField(db_column='Vat2_BruttoZakup')
    vat2_index = IntegerField(db_column='Vat2_Index')
    vat2_netto = FloatField(db_column='Vat2_Netto')
    vat2_nettozakup = FloatField(db_column='Vat2_NettoZakup')
    vat2_procent = IntegerField(db_column='Vat2_Procent')
    vat2_stawka = CharField(max_length=10, db_column='Vat2_Stawka')
    vat2_vat = FloatField(db_column='Vat2_Vat')
    vat2_vatzakup = FloatField(db_column='Vat2_VatZakup')
    vat3_brutto = FloatField(db_column='Vat3_Brutto')
    vat3_bruttozakup = FloatField(db_column='Vat3_BruttoZakup')
    vat3_index = IntegerField(db_column='Vat3_Index')
    vat3_netto = FloatField(db_column='Vat3_Netto')
    vat3_nettozakup = FloatField(db_column='Vat3_NettoZakup')
    vat3_procent = IntegerField(db_column='Vat3_Procent')
    vat3_stawka = CharField(max_length=10, db_column='Vat3_Stawka')
    vat3_vat = FloatField(db_column='Vat3_Vat')
    vat3_vatzakup = FloatField(db_column='Vat3_VatZakup')
    wartwcenachzakupunetto = FloatField(db_column='WartWCenachZakupuNetto')
    
    class Meta:
        database = db
	
class Paragony_Zawartosc(peewee.Model):
    cenabrutto = FloatField(db_column='CenaBrutto')
    cenanetto = FloatField(db_column='CenaNetto')
    cenazakupunetto = FloatField(db_column='CenaZakupuNetto')
    grupa = IntegerField(db_column='Grupa')
    grupanazwa = CharField(max_length=50, db_column='GrupaNazwa')
    identyfikatordok = BigIntegerField(db_column='IdentyfikatorDok')
    ilosc = IntegerField(db_column='Ilosc')
    indeks = IntegerField(db_column='Indeks')
    jm = CharField(max_length=10, db_column='Jm')
    mag = IntegerField(db_column='Mag')
    nazwa = CharField(max_length=100, db_column='Nazwa')
    nazwadlakasy = CharField(max_length=50, db_column='NazwaDlaKasy')
    nrceny = IntegerField(db_column='NrCeny')
    pkwiu = CharField(max_length=50, db_column='PKWIU')
    rabat = FloatField(db_column='Rabat')
    symbol = CharField(max_length=100, db_column='Symbol')
    symbolaktualny = IntegerField(db_column='SymbolAktualny')
    symboldostawcy = IntegerField(db_column='SymbolDostawcy')
    vat = CharField(max_length=10, db_column='Vat')
    wartoscbrutto = IntegerField(db_column='WartoscBrutto')
    wartoscnetto = FloatField(db_column='WartoscNetto')
    wartoscvat = FloatField(db_column='WartoscVat')
    wartosczakupuvat = FloatField(db_column='WartoscZakupuVat')
    id = BigIntegerField(primary_key=True)

    class Meta:
        database = db


def pushFieldToDatabase(name,field):
	print field
	print ';'
	print name
	sq = eval(name).insert_many([field])
	sq.execute() 
#Info.create_table()
#fields = find_sections.returnDictFromFile()
#fields={'godz': ' 9:05:00', 'konto': '', 'program': 'SMALL BUSINESS 5.1.3021.4980', 'nazwa': 'RZEPKA Pruszowice ul.Sloneczna 13          tel.071 31 54 603, e-mail: wkn@wp.pl', 'nip': '911-167-70-58', 'data': '14.04.24', 'kod': '51-217', 'kodowanie': 'Windows 1250', 'miasto': 'Pruszowice'}


#sq = Info.insert_many([fields])
#sq.execute()
#print fields
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


