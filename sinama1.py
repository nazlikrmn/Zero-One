class sinama1:
    #siyah0 beyaz1
    def __init__(self):
        self.sayi=int(input("Sayi giriniz"))
        self.KacFarkli()
    def KacFarkli(self):
        self.Ekle(0,"0","")
        self.Ekle(0,"1","")
    def Ekle(self,basamak,eklenecek,bir_onceki):
        if basamak is not self.sayi:#yeni basamak ekle
            yeni=bir_onceki+eklenecek
            if eklenecek is not "0":
                self.Ekle(basamak+1,"0",yeni)
                self.Ekle(basamak + 1, "1", yeni)
            elif eklenecek is "0":
                self.Ekle(basamak+1,"1",yeni)
        if basamak is self.sayi-1:#yaz
            print(yeni)
sinama1()