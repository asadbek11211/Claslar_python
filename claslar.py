# # class Davlatlar:
# #     """Davlatlar yaratish uchun class"""
# #     def __init__(self,nomi,poytaht,axoli,joylashuv,maydoni,til):
# #         self.nomi = nomi
# #         self.poytaht = poytaht
# #         self.axoli = axoli
# #         self.joylashuv = joylashuv
# #         self.maydoni = maydoni
# #         self.til = til

# #     def get_nomi(self):
# #         return f"{self.nomi.title()}"
# #     def Info(self):
# #         return f"{self.nomi.title()} davlatining poyhaxti {self.poytaht} shaxri {self.axoli} nafar axoliga ega "
# #     def get_joylashuv(self):
# #         return f"{self.nomi.title() } davlati {self.joylashuv} da joylashgan"

# #     def get_maydoni(self):
# #         return f"{self.nomi.title()}ning maydoni {self.maydoni} km kvga teng"
# #     def get_tili(self):
# #         print( f"{self.nomi.title()}ning davlat tili {self.til} tili hisoblanadi")

# # Uzb = Davlatlar('uzb','toshkent',38000000,'markaziy osiyo',448978,'uzbek')
# # Rus = Davlatlar('rassiya','moskva',14400000,'yevro oyiyo',17098242,'rus')

# # Uzb.get_tili()



# class Shaxs:
#     def __init__(self,ism,familya,tyil):
#         self.name = ism
#         self.surname =familya
#         self.age = tyil
#     def get_info(self):
#         return f"{self.name.title()} {self.surname.title()} {self.age} yilda tugilgan"
#     def get_name(self):
#         return self.name.title()

# # inson = Shaxs('kamoltoy','murodov',24)
# # print(inson.get_info())


# class Talaba(Shaxs):
#     def __init__(self,ism,familya,tyil,bosqich):
#         super().__init__(ism,familya,tyil)
#         self.bosqich = bosqich
#     def get_bosqich(self):
#         return f"{self.get_name()} {self.bosqich}-bosqich talabasi"


# class Fanlar(Talaba):
#     def __init__(self,ism,familya,tyil,bosqich,fan,ustoz):
#         super().__init__(ism,familya,tyil,bosqich)
#         self.fan = fan
#         self.ustoz = ustoz
#     def get_fan(self):
#         return f"{self.fan.title()}"
#     def get_ustoz(self):
#         return f"{self.ustoz}"
    
# talaba = Fanlar('murod','karimov',1998,4,'oliy matematika','Professor Atxam boburovich')

# print(talaba.get_info())






