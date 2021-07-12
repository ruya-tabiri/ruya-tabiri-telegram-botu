import sqlite3


def cevap(gelen):
    gelen = gelen.lower() # küçük harf yapıyoruz
    gelendizi = gelen.split(",") # virgüllere göre rüya terimlerini ayırıyoruz
    cumle=""
    vt = sqlite3.connect("ruyatabiri.db")
    imlec = vt.cursor()
    for terim in gelendizi:
        cekilenveri = imlec.execute("""SELECT baslik,icerik FROM tabir WHERE baslik like "% {}%" """.format(terim))
        veriler = cekilenveri.fetchall()
        for veri in veriler:
            cumle+=veri[1]+"\n" 
        
    return cumle


