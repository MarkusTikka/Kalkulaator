class cal(): #klass 'cal'
    def __init__(self,a,b):
        self.a = a #salvestab argument a klassi atribuuti self.a
        self.b = b

    def liitmine(self): #
        return self.a + self.b #tagastab a ja b summa
    def lahutamine(self):
        return self.a - self.b #tagastab a ja b vahe
    def korrutamine(self):
        return self.a * self.b #tagastab a ja b korrutise
    def jagamine(self):
        return self.a / self.b #tagastab a ja b jagatise
    def jaak(self):
        return self.a % self.b #tagastab self.a ja self.b jäägi
    def ruutjuur(self):
        return self.a ** self.b
a = int(input("Sisesta esimene number: ")) #küsib kasutajalt esimest täisarvu
b = int(input("Sisesta teine number: ")) #küsib kasutajalt teist täisarvu

kalk = cal(a,b)
while True: #algatab lõpmatu tsükli
    def menu(): #menüü funktsioon
        x = ('1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Ruutjuure leidmine. ')
        print(x)#printib menüü valikud ekraanile
    menu()
    valik = int(input('Sisesta üks valikutest: ')) #küsib kasutajalt valiku numbrit
    if valik == 1:#Kui kasutaja valik on 1
        print("Vastus: ",kalk.liitmine()) #väljastab liitmise vastuse
        break
    elif valik == 2:
        print("Vastus: ",kalk.lahutamine()) #väljastab lahutamise vastuse
        break
    elif valik == 3:
        print("Vastus: ",kalk.korrutamine())#äljastab korrutamise vastuse
        break
    elif valik == 4:
        print("Vastus: ",kalk.jagamine())#väljastab jagamise vastuse
        break
    elif valik == 5:
        print("Vastus: ",kalk.jaak()) #Väljastab jäägi vastuse
        break
    elif valik == 6: #kui kasutaja valik on 6
        print("Vastus: ",kalk.ruutjuur())#väljastab ruutjuure vastuse
        break
    elif valik == 0:#kui kasutaja valik on 0
        print('Sisesta uuesti üks liitmise operaator') #väljastab teate et tuleb uuesti sisestada
        break#tsükkel lõppeb
