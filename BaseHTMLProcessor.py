#-*- coding: utf-8 -*-
 
u"""Klasa bazowa do tworzenia modułów przetwarzających HTML
 
Klasa ta została zaprojektowana tak, aby przyjmowała HTML 
 
Klasa ta została zaprojektowana tak, że przyjmuje HTML jako wejście
i wypluwa taki sam dokument HTML. Samo w sobie nie jest to za bardzo
interesujące. Z tej klasy tworzymy klasy pochodne i dostarczamy do niej
metod, które potrzebujemy do przekształcania HTML-a.
 
Ten program jest częścią książki "Zanurkuj w Pythonie", podręcznika
o Pythonie dla doświadczonych programistów. Najnowszą wersję można
znaleźć tu: http://pl.wikibooks.org/wiki/Zanurkuj_w_Pythonie.
 
Program ten został oparty na przykładach zawartych w książce
"Dive Into Python", a dostępnej stąd: http://www.diveintopython.org.
"""
 
__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 1.2 $"
__date__ = "$Date: 2004/05/05 21:57:19 $"
__copyright__ = "Copyright (c) 2001 Mark Pilgrim"
__license__ = "Python"
 
from sgmllib import SGMLParser
import htmlentitydefs
 
class BaseHTMLProcessor(SGMLParser):
    def reset(self):
        # dodatek (wywoływane przez SGMLParser.__init__)
        self.pieces = []
        SGMLParser.reset(self)
 
    def unknown_starttag(self, tag, attrs):
        # wywoływane dla każdego początkowego znacznika
        # attrs jest listą krotek (atrybut, wartość)
        # np. dla <pre class="screen"> będziemy mieli tag="pre", attrs=[("class", "screen")]
        # Chcielibyśmy zrekonstruować oryginalne znaczniki i atrybuty, ale
        # może się zdarzyć, że umieścimy w cudzysłowach wartości, które nie były zacytowane
        # w źródle dokumentu, a także możemy zmienić rodzaj cudzysłowi w wartości danego atrybutu
        # (pojedyncze cudzysłowy lub podwójne).
        # Dodajmy, że niepoprawnie osadzony kod nie-HTML-owy (np. kod JavaScript)
        # może zostać źle sparsowany przez klasę bazową, a to spowoduje błąd wykonania skryptu.
        # Cały nie-HTML musi być umieszczony w komentarzu HTML-a (<!-- kod -->),
        # aby parser zostawił ten niezmieniony (korzystając z handle_comment).
        strattrs = "".join([' %s="%s"' % (key, value) for key, value in attrs])
        self.pieces.append("<%(tag)s%(strattrs)s>" % locals())
 
    def unknown_endtag(self, tag):
        # wywoływane dla każdego znacznika końcowego np. dla </pre>, tag będzie równy "pre"
        # Rekonstruuje oryginalny znacznik końcowy w wyjściowym dokumencie
        self.pieces.append("</%(tag)s>" % locals())
 
    def handle_charref(self, ref):
        # wywoływane jest dla każdego odwołania znakowego np. dla "&#160;", ref będzie równe "160"
        # Rekonstruuje oryginalne odwołanie znakowe.
        self.pieces.append("&#%(ref)s;" % locals())
 
    def handle_entityref(self, ref):
        # wywoływane jest dla każdego odwołania do encji np. dla "&copy;", ref będzie równe "copy"
        # Rekonstruuje oryginalne odwołanie do encji.
        self.pieces.append("&%(ref)s" % locals())
        # standardowe encje HTML-a są zakończone średnikiem; pozostałe encje (encje spoza HTML-a) nie są
        if htmlentitydefs.entitydefs.has_key(ref):
            self.pieces.append(";")
 
    def handle_data(self, text):
        # wywoływane dla każdego bloku czystego teksu np. dla danych spoza dowolnego
        #znacznika, w których nie występują żadne odwołania znakowe, czy odwołania do encji.
        # Przechowuje dosłownie oryginalny tekst.
        self.pieces.append(text)
 
    def handle_comment(self, text):
        # wywoływane dla każdego komentarza np. <!-- wpis kod JavaScript w tym miejscu -->
        # Rekonstruuje oryginalny komentarz.
        # Jest to szczególnie ważne, gdy dokument zawiera kod przeznaczony
        # dla przeglądarki (np. kod Javascript) wewnątrz komentarza, dzięki temu
        # parser może przejść przez ten kod bez zakłóceń;
        # więcej szczegółów w komentarzu metody unknown_starttag.
        self.pieces.append("<!--%(text)s-->" % locals())
 
    def handle_pi(self, text):
        # wywoływane dla każdej instrukcji przetwarzania np. <?instruction>
        # Rekonstruuje oryginalną instrukcję przetwarzania
        self.pieces.append("<?%(text)s>" % locals())
 
    def handle_decl(self, text):
        # wywoływane dla deklaracji typu dokumentu, jeśli występuje, np.
        # <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        #     "http://www.w3.org/TR/html4/loose.dtd">
        # Rekonstruuje oryginalną deklarację typu dokumentu
        self.pieces.append("<!%(text)s>" % locals())
 
    def output(self):
        u"""Zwraca przetworzony HTML jako pojedynczy łańcuch znaków"""
        return "".join(self.pieces)
 
if __name__ == "__main__":
    for k, v in globals().items():
        print k, "=", v

