# Premisas
afirmacion_condicional = True # Si llueve, entonces la calle estará mojada
consecuencia_negada = False   # La calle no está mojada
# Inferencia Modus Tollens
if afirmacion_condicional and not consecuencia_negada:
    conclusion = "No está lloviendo"
else:
    conclusion = "La inferencia Modus Tollens no es válida"

# Imprimir la conclusión
print(conclusion)
