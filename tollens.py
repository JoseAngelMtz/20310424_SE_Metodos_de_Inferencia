def inferencia_de_tollens(premisa1, premisa2, negacion_consecuencia):
  antecedente1, consecuencia1 = premisa1.split()
  antecedente2, consecuencia2 = premisa2.split()
    
  if consecuencia1 == negacion_consecuencia and antecedente1 == f"~{antecedente2}":
    return f"Por inferencia de Tollens, ~{antecedente1} es verdadero."
  else:
      return "La inferencia de Tollens no es aplicable a estas premisas."

# Ejemplo de uso
premisa1 = "0 1"
premisa2 = "1 0"
negacion_consecuencia = "0"

resultado = inferencia_de_tollens(premisa1, premisa2, negacion_consecuencia)
print(resultado)
