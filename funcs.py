from turtle import *


def Multi_input1():
    Who = int(input("Who: "))
    Who2 = int(input("Who2: "))
    Who3 = int(input("Who3: "))
    Who4 = int(input("Who4: "))
    playing = True
    if playing == True:
        while True:
            forward(Who)
            right(Who2)
            left(Who3)
            right(Who4)
            return Multi_input1
        
def Multi_input2():
    Flo = float(input("Flo: "))
    Flo2 = float(input("Flo2: "))
    Flo3 = float(input("Flo3: "))
    Flo4 = float(input("Flo4: "))
    playing = True
    if playing == True:
        while True:
            forward(Flo)
            right(Flo2)
            left(Flo3)
            right(Flo4)
            return Multi_input2
