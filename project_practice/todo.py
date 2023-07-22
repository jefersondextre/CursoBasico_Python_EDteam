import os 

# Todo List
runProgram = True
todolist = []
#  funcion para mostrar las opciones del menu
def showMenuOptions():
    print("")
    print("Por favor seleccione una opción: ")
    print("1. Crear una tarea")
    print("2. Marcar como realizada una tarea")
    print("3. Borrar una tarea")
    print("4. Salir")
        
#Muestra todas las tareas
def showTodoList():
    global todolist
    
    print("")
    print("*"*12,"Tareas","*"*12)
    print("*"*32)
    for todo in todolist:
        print(f"{todolist.index(todo)+1}. {todo}")
    print("*"*32)
    print("*"*32)
    

# Funcion para guardar tareas en la variable "todolist"
def createTodo():
    os.system("cls")  #mack clear
    global todolist
    print("Crear una nueva tarea")
    todo = input("Por favor ingrese la descripcion de la tarea: ")
    todolist.append(todo)
    # Mostrar la lista de tareas
    showTodoList()

# Funcion para marcar una tarea como realizada
def updateTodo():
    global todolist
    print("")
    print("Esta actualizando una tarea..")
    todoId = int(input("Ingrese el numero de la tarea que desea marcar como hecha: "))

    todolist[todoId-1]=todolist[todoId-1]+"  ✅"
    showTodoList()

def deleteTodo():
    global todolist
    print("")
    print("Eliminando una tarea..")
    todoId = int(input("Ingrese el numero de la tarea a eliminar."))
    del todolist[todoId-1]
    showTodoList()

def main():
    global runProgram
    print(".: WELCOME TO A PYTHON TO DO LIST:.")        
    while runProgram :
        showMenuOptions()
        option = int(input("Ingresa el número de la opción: "))
        
        match option:
            case 1:
                createTodo()
            case 2 : 
                updateTodo()
            case 3 :
                deleteTodo()
            case 4:
                runProgram = False
                print("Hasta luego")
            case _ :
                print("Opción ingresada no reconocida. Ingrese una opción válida.")    

                
if __name__=="__main__":
    main()