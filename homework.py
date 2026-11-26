class user:
    """Foydalanuchi nomli klass yaratamiz"""


    def __init__(self,ism,familya,email,tyil,bosqich,yoshi):
      self.ism = ism
      self.familya = familya
      self.email = email
      self.tyil = tyil
      self.__bosqich = bosqich
      self.__yoshi = yoshi

    def get_info(self):
          return f"{self.ism} {self.familya} {self.email} {self.tyil}"
    def get_bosqich(self):
        return self.__bosqich
    def get_yoshi(self):
        return self.__yoshi


foydalanuvchi = user("Ma'rifat",'Bazarboyeva','@marifatbozorboyeva717gmail.com',2011,9,15)
print(foydalanuvchi.get_info())
print(foydalanuvchi.get_bosqich())
print((foydalanuvchi.get_yoshi() ))

