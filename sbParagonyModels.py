from peewee import *

database = MySQLDatabase('baza_test_python', **{'passwd': 've7128', 'host': 'localhost', 'user': 'bazek'})

class UnknownFieldType(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Book(BaseModel):
    author = CharField(max_length=255)
    title = TextField()

    class Meta:
        db_table = 'book'

class Info(BaseModel):
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
        db_table = 'info'

class Paragony(BaseModel):
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
    wartwcenachzakupunetto = FloatField(db_column='WartWCenachZakupuNetto')

    class Meta:
        db_table = 'paragony'

class Paragony_Zawartosc(BaseModel):
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
        db_table = 'paragony_zawartosc'

