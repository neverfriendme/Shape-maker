from turtle import *
__name__ == "__main__"

print("Shape maker v3")
print("Quit\nForm\nlistfunc.[function]")
WF = input("")


if WF == "Form.circ":
    import funcs
    funcs.Form_cric()
elif WF == "Form.octa":
    import funcs
    funcs.Form_octa()
elif WF == "Form.nona":
    import funcs
    funcs.Form_nona()  
elif WF == "Quit":
    print("Quitting")
    quit()
else:
    print("Invalid")
    quit()




