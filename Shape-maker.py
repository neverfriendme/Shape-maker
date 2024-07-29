from turtle import *
__name__ == "__main__"

print("Shape maker v3")
print("Whole\nFloat\nMulti-input.w\nMulti\nQuit")
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
elif WF == "Multi-input.w":
    import funcs
    funcs.Multi_input1()
elif WF == "Multi-input.f":
    import funcs
    funcs.Multi_input2()  
elif WF == "Quit":
    print("Quiting")
    quit()
else:
    print("Invalid")
    quit()




