print_info = "The print function allows you to print words into a terminal. Print is used like this: print("") Now you try."
lists_info = "The list function allows you to put variables in a list. To make a list first you need a variable to store the list.Lists are used like this:list=[a, b, c, d, e]Now you try."
def_info = "The def function allows you to create functions. def is formatted like this: def (function name ) def is used like this: def name(): Now you try."
variable_info = "The variable function allows you to create variables. Variables are used like this: {variable name} = {want you want to store}"
info_storage = [print_info, lists_info, def_info, variable_info]
running = True
while running:
    def print_desc():
        print(print_info)
        code1 = input("print("")")
        varx=code1
        print(" If you were actually coding you would have to type it like this:*('print{code1}')* #take out the asterisks or your code will not work")
        print("You just did a print. Good Job!")
    print_desc()
    continue1 = input("do you want to continue: (type no to quit) (type yes to continue) ")
    if continue1 == "no":
     running = False    
    else:
        running = True
        
    def variable_desc():
        print(variable_info)
        var = input("what will you call your variable:")
        code2 = input(f"{var} = ")
        print(f"You just made the variable {var} = {code2}. Good Job!")
    if running == True:
        variable_desc
    else:
        break
    continue1 = input("do you want to continue: (type no to quit) (type yes to continue) ")
    if continue1 == "no":
        break
    else:
        running = True
    def list_desc():
        print(lists_info)
        listname1 = input("what will you call your list:")
        var1 = input("what will you call your first variable:")
        var2 = input("what will you call your second variable:")
        var3 = input("what will you call your third variable:")
        list1 = [var1, var2, var3]
        print(list1)
        print(f"You just gave the list {listname1} the items {var1}, {var2}, {var3}. Good Job!")
        
    if running == True:
        list_desc
    else:
        break
    continue1 = input("do you want to continue: (type no to quit) (type yes to continue) ")
    if continue1 == "no":
        break
    else:
        running = True
        
    def def_desc():
        print(def_info)
        func_name = input("What will you call your function: ")
        def1 =(f"def {func_name}:")
        print(f"{def1} now once you're at this step you can press enter and the new line will be indented. the indented lines will be the only lines of code in the function.")
        print("You just learned how to define a function. Great job!")
    if running == True:
        def_desc
    else:
        break
    print("You have completed all 4 lessons and learned basic python. Good for you!")
    def redo():
        redo = int(input("if you want to redo a lesson input the number that coresponds to the order they were in. If you are finished press 0."))
        if redo == 0:
            running = False
        elif redo == 1:
            print_desc()
        elif redo == 2:
            variable_desc()
        elif redo == 3:
            list_desc()
        elif redo == 4:
            def_desc()
    redo()         
    
