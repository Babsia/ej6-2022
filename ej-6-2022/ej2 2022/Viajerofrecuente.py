class viajeroFrecuente:
    __num=0
    __dni=""
    __nombre=""
    __apellido=""
    __millasacum=""
    def __init__(self,numero,dni='',nombre='',apellido='',millas=0):
        self.__num=numero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millasacum=millas
    def getmillas(self):
        return self.__millasacum
    def acumularmillas(self,millas):
        self.__millasacum=self.__millasacum+millas
        return self.__millasacum
    def canje(self,millasc):
        if millasc<=self.__millasacum:
            self.__millasacum=self.__millasacum-millasc
        else:
            print("error en la operacion")
        return(self.__millasacum)
    def getnum(self):
        return self.__num
    def __add__(self,millas):
        otroviajero=viajeroFrecuente(self.getnum(),self.getdni(),self.getnom(),self.getape(),self.getmillas()+millas)
        return otroviajero
    def __sub__(self,millas):
        otroviajero=self.getmillas()+millas
        return (otroviajero)
    def getdni(self):
        return self.__dni
    def getnom(self):
        return self.__nombre
    def getape(self):
        return self.__apellido
    
