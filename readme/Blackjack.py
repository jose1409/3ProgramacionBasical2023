dinero_temporal = 500
from random import random
print('INSTRUCCIONES\n'
      'El objetivo de cualquier mano de blackjack es derrotar a la banca\n'
      'Puedes ganar con una puntuación inferior a 22 cuando la mano de la banca supera los 21 puntos\n'
      'Cuando el valor total de tu mano es de 22 o más, esto se conoce comúnmente como "bancarrota", y automáticamente perderás cualquier dinero apostado\n'
      '\n'
      'LIGAR:\n' 
      '      Puedes solicitar cartas extra para mejorar tu mano. Las cartas se pueden pedir de a una hasta que el valor total de la mano sea 21 o superior\n'
      'PLANTARSE:\n' 
      '          Cuando el valor total de tu mano sea 21 o inferior, puedes elegir plantarte y no arriesgar las posibilidades de que tu mano supere los 21 en valor total\n'
      'DIVIDIR:\n'
      '        Cuando tus primeras dos cartas tienen el mismo valor (ocho-ocho, jota-diez, etc.), puedes realizar apuestas adicionales\n' 
      '        (igual a la apuesta inicial) y crear una segunda mano con la que jugar contra la banca\n'
      'DOBLAR:\n' 
      '       Puedes colocar una apuesta extra, igual a la apuesta inicial, a cambio de una sola carta más para tu mano, después de la cual te plantarás automáticamente\n')

numeros = [1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],{1,2,3,4,5,6,7,8,9,10}

j=random.randint(0,9)
i=random.randint(0,3)
print(f"El i es: {i}")     #Revisar
print(f"El j es: {j}")     #Revisar

if(i==0):
    print(f"{numeros[i][j]} de Corazon")
elif(i==1):
    print(f"{numeros[i][j]} de Trebol")
elif(i==2):
    print(f"{numeros[i][j]} de Picas")
else:
    print(f"{numeros[i][j]} de Diamante")
#hola como esta