#Modelo de SumaDigitos
def Sumadigitos(n, B, VS):
  PrimeraEtapa=n*(n+1)/2
  while n>=1:
    SegundaEtapa = n/PrimeraEtapa
    n=n-1
    Aplicar_Formula= SegundaEtapa*(B-VS)
  return Aplicar_Formula
