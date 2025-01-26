
line_code = input("Enter the line of code: ")

#Valido si inicia con la palabra reservada print
if not line_code.startswith("print"):
    print("Error: print statement not found")
    exit()
else:
    line_code = line_code[6:]

    #Valido si inicia con un parentesis
    if not line_code.startswith("("):
        print("Error: '(' not found")
        exit()
    else:
        line_code = line_code[1:]

        #Valido si termina con un parentesis
        if not line_code.endswith(")"):
            print("Error: ')' not found")
            exit()
        else:
            line_code = line_code[:-1]

            #Valido si inicia con comillas
            if not line_code.startswith('"'):
                if not line_code.endswith('"'):

                    #En el caso que no inicie con comillas, valido si hay un espacio
                    if not line_code.find(" "):
                        print("Validation successful")
                        exit()
                    else:
                        print("Error: not space permitted")
                        exit()

                else:
                    print("Error: ' \" ' not found")
                    exit()
            else:
                line_code = line_code[1:]

                #Valido si termina con comillas
                if not line_code.endswith('"'):
                    print("Error: ' \" ' not found")
                    exit()
                else:
                    print("Validation successful")
                    exit()
    

    

    