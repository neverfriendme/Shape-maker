from turtle import *
print("Shape maker v2 pre-release")
WF = input("Whole numbers or Float numbers: ")

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
if WF == "Float":
    Flo = float(input("Flo: "))
    Flo2 = float(input("Flo2: "))
    playing = True
    if playing == True:
        while True:
            forward(Flo)
            right(Flo2)
            left(Flo)
            right(Flo2)
else:
    print("Invalid")
    quit()
