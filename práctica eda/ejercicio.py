print("Este programa te dice el area y el perimetro de las siguientes figuras\n")
print("1.Triangulo\n2.Circulo\n3.Rectangulo\n4.trapecio\n")
print("El lado en casos correspondientes y el radio en el caso del Circulo es 3\n")
print("La altura en los casos correspondientes es 4\n")
#inicializamos los valores de la altura y del lado mas los lados adicionales
lado_radio_basemayor=3
altura=4
base_menor=2
lado_adicional=2
#realizamos las operaciones y las almacenamos en sus respectivas variables
peri_triangulo=lado_radio_basemayor*3
area_triangulo=(lado_radio_basemayor*altura)/2
peri_rectangulo=(lado_radio_basemayor*2)+(2*altura)
area_rectangulo=(lado_radio_basemayor*altura)
peri_circulo=3.1416*(2*lado_radio_basemayor)
area_circulo=3.1416*(lado_radio_basemayor*lado_radio_basemayor)
peri_trapecio=(lado_adicional*2)+lado_radio_basemayor+base_menor
area_trapecio=((lado_radio_basemayor+base_menor)*altura)/2
#Ahora imprimimos los valores obtenidos
print("\nTriangulo:  area=" +str(area_triangulo))
print("\nTriangulo:  perimetro=" +str(peri_triangulo))
print("\nRectangulo:  area=" +str(area_rectangulo))
print("\nCirculo:  area=" +str(area_circulo))
print("\nCirculo:  perimetro=" +str(peri_circulo))
print("\nTrapecio:  area=" +str(area_trapecio))
print("\nTrapecio:  perimetro=" +str(peri_trapecio))
