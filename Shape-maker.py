from turtle import *
__name__ == "__main__"

print("Shape maker v4 pre-release")
print("Quit\nForm\nlistfunc.[function]\nhelp")
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
elif WF == "listfunc.[Form]":
    import funcs
    funcs.listfunc_form()
elif WF == "help" or "?h":
    import funcs
    funcs.help()
else:
    print("Invalid")
    quit()








