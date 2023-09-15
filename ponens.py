def inferencia_de_ponens(p, q):
    if p:
        if p is True:
            print("P es verdadero.")
            if q:
                if q is True:
                    print("Q también es verdadero.")
                    print("La inferencia de Ponens se cumple.")
                else:
                    print("Q es falso. La inferencia de Ponens no se cumple.")
            else:
                print("Q es desconocido. La inferencia de Ponens no se cumple.")
        else:
            print("P es falso. La inferencia de Ponens no se cumple.")
    else:
        print("P es desconocido. La inferencia de Ponens no se cumple.")

# Define los valores de P y Q (verdadero o falso)
p = bool(input("P="))
q = bool(input("Q="))

# Llama a la función de inferencia de Ponens
inferencia_de_ponens(p, q)
