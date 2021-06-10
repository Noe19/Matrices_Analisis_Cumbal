import numpy
import sys

r1=0
r2=0
c1=0
c2=0
print("\n~~~~~~~~~~~~Este programa es de multiplicaciones~~~~~~~~~~~~~\n\n")

while True :
  
  try:
    r1=int(input('*Ingrese las filas de la primera matriz :')) 
    break

  except ValueError:
    print("\n\n*****************************************\n\n")
    print("Error, el sistema solo admite numeros  ")
    print("\n\n*****************************************\n\n")
    
while True:
  try:
    c1=int(input('*Ingrese las colunmas de la primera matriz:'))
    break
  except ValueError:
    print("\n\n*****************************************\n\n")
    print("Error, el sistema solo admite numeros  ")
    print("\n\n*****************************************\n\n")
while True:    
  try:
     r2=int(input('*Ingrese las filas de la segunda matriz:'))
     break
  except ValueError:
    print("\n\n*****************************************\n\n")
    print("Error, el sistema solo admite numeros  ")
    print("\n\n*****************************************\n\n")
while True:   
  try: 
    c2=int(input('*Ingrese las colunmas de la segunda matriz:'));
    break
  except ValueError:
    print("\n\n*****************************************\n\n")
    print("Error, el sistema solo admite numeros  ")
    print("\n\n*****************************************\n\n")
    
  
  
  
#Verificacion de entrada d valores del tamaño de las matrices 
 
while (c1>c2) or (c1<c2) or (r1>r2) or (r1<r2):
  print ("\n[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]][[[[[[[[[[[[[[[[[[[[\n")
  print("Datos inconrrectos , o el tamaño de las matrices son diferentes \n  Por favor vuelve a ingresarlos!!!!!!!!!\n")
  print (" \n[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]\n")

  while True :
  
   try:
    r1=int(input('-Ingrese las filas de la primera matriz :')) 
    break

   except ValueError:
    print ("\n\n*****************************************\n\n")
    print("Error, el sistema solo admite numeros  ")
    print("\n\n*****************************************\n\n")
    
  while True:
   try:
    c1=int(input('-Ingrese las colunmas de la primera matriz:'))
    break
   except ValueError:
    print ("\n\n*****************************************\n\n")
    print("Error, el sistema solo admite numeros  ")
    print("\n\n*****************************************\n\n")
  while True:    
   try:
     r2=int(input('-Ingrese las filas de la segunda matriz:'))
     break
   except ValueError:
    print ("\n\n*****************************************\n\n")
    print("Error, el sistema solo admite numeros  ")
    print("\n\n*****************************************\n\n")
  while True:   
   try: 
    c2=int(input('-Ingrese las colunmas de la segunda matriz:'));
    break
   except ValueError:
    print ("\n\n*****************************************\n\n")
    print("Error, el sistema solo admite numeros  ")
    print("\n\n*****************************************\n\n")
    
  

 
print ("\n\nIngreso correctamente el tamaño de las matrices:")

matriz1=numpy.zeros((r1,c1))
matriz2=numpy.zeros((r2,c2))
matrizr=numpy.zeros((r1,c2))

print("introduzca los valores de la 1 matriz")
for r in range (0,r1):
 for c in range (0,c1):
   while True:
     try:
      matriz1[r,c] =(input ("Elemento a [" +str(r+1 )+str(c+1)+"]" ))
      break
     except ValueError:
       print ("\n\n*****************************************\n\n")
       print("Error, el sistema solo admite numeros  ")
       print("\n\n*****************************************\n\n")

print("\nintroduzca los valores de la 2 matriz")
for r in range (0,r2):
  for c in range (0,c2):
    while True:
      try:
       matriz2[r,c] =input ("Elemento a [" +str(r+1 )+str(c+1)+"]" )
       break
      except ValueError:
       print ("\n\n*****************************************\n\n")
       print("Error, el sistema solo admite numeros  ")
       print("\n\n*****************************************\n\n")


 #procedimiento de la multiplicacion
for r in range (0,r1):
 for c in range (0,c2):
   for k in range(0,r1):
     matrizr[r,c]+=matriz1[r,k]*matriz2[k,c]
print ("\n\n El resultado es : \n")
print (matrizr)
#print(matriz1)
#print(matriz2)