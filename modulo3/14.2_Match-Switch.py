'''
Switch - Match => Sirve para evaluar un dato
y con base a ello realizar una acción.
Evalua un valor y escoge de ciertos casos

'''
status = "solido otro"
match status:
    case "solido" | "liquido" | "gaseoso":
        print("El estados es solido o liquido o gaseoso")
    case "plasmatico" | "otro":
        if status == "plasmatico" and status == "otro":
            print("El estado es plasmatico")
    case _:
        print("El estado no existe")
