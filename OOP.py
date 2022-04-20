class Lop:
    lop=0
    def __init__(self,tengi,maytuoi,odau):
        self.ten= tengi
        self.tuoi= maytuoi
        self.noio= odau
    def getname(self):
        return "Tôi tên là: " +self.ten
    def getage(self):
        return self.tuoi + " tuoi"
    def getlive(self):
        return 'Sống ở ' +self.noio

#name=input()
#age= input()
#live= input()
Lop_12B1=Lop("name","age","live")
#Lop.lop=2
Lop_12B1.lop=11
print(Lop.lop)
print(Lop_12B1.lop)


#print(Lop_12B1.getname())
#print(Lop_12B1.getage())
#print(Lop_12B1.getlive())