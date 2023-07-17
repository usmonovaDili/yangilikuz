class odam:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.fam = familiya

    def get_info(self):
        return f'{self.ism} {self.fam}'


# a = odam('dilorom', 'usmonova')
# print(a.get_info())

#
#
# class shaxs(odam):
#     def __init__(self, ism, familiya, yosh):
#         super().__init__(ism, familiya)
#         self.yosh = yosh
#
#     def get(self):
#         return f'{self.ism} {self.fam} {self.yosh}'
#
# s=shaxs('dilorom','usmonova',20)
# print(s.get())
#
# class Manzil:
#
#     def __init__(self, tuman, viloyat, kucha, uy):
#         self.tuman = tuman
#         self.viloyat = viloyat
#         self.kucha = kucha
#         self.uy = uy
#
#     def get_info(self):
#         manzil = f'{self.viloyat} {self.tuman} {self.kucha} {self.uy}'
#         return manzil
#
# m=Manzil('chiroqchi','qashqadaryo','olmazor',64)
# class shaxs(odam):
#
#     def __init__(self, ism, familiya,yosh, manzil):
#         super().__init__(ism, familiya)
#         self.yosh=yosh
#         self.manzil = manzil
#
#     def get(self):
#         return f'{self.ism} {self.fam} {self.yosh} {self.manzil}'
#
# asa=shaxs('dilorom','familiya','12',m.get_info())
# print(asa.get())

from uuid import uuid4


class auto:
    __num_auto = 0

    def __init__(self, model, yil, rangi, km=0):
        self.model = model
        self.yil = yil
        self.rang = rangi
        self.__km = km
        self.__id = uuid4()
        auto.__num_auto += 1

    def add_km(self, km):
        if km >= 0:
            self.__km += km

        else:
            return 'km pasaytrib bulmaydi'

    def get_info(self):
        return f' {self.__id} {self.model} {self.yil} {self.rang}'

    @classmethod
    def auvto_num(cls):
        return cls.__num_auto


p = auto('kia', 1200, 'oq', 1234)
print(p.get_info())
print(p.auvto_num())
