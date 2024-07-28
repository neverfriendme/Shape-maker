from turtle import *
print("Shape maker v2")
print("Whole\nFloat\nMulti-input")
WF = input("")

if WF == "Whole":
    Who = int(input("Who: "))
    Who2 = int(input("Who2: "))
    playing = True
    if playing == True:
        while True:
            forward(Who)
            right(Who2)
            left(Who)
            right(Who2)
elif WF == "Float":
    Flo = float(input("Flo: "))
    Flo2 = float(input("Flo2: "))
    playing = True
    if playing == True:
        while True:
            forward(Flo)
            right(Flo2)
            left(Flo)
            right(Flo2)
elif WF == "Multi-input":
    Who3 = int(input("Who: "))
    Who4 = int(input("Who2: "))
    Flo3 = float(input("Flo: "))
    Flo4 = float(input("Flo2: "))
playing = True
if playing == True:
        while True:
            forward(Who3)
            right(Who4)
            left(Flo3)
            right(Flo4)
else:
    print("Invalid")
    quit()
