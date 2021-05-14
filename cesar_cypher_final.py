#Este es un programa realizado en mi periodo de estudio del lenguaje Python
#El fin de este programa es cifrar cualquier ingreso del usuario usando el "Cifrado Cesar"
#El cifrado propone trasladar tantas posiciones como se indique las letras de una palabra en el abecedario
#EJ codificacion: bebe con 5 de desplazamiento (shift) seria "gjgj" 
#De la misma manera el programa puede descifrar las palabras ingresadas si se posee el numero de desplazamientos correctos.
#EJ decodificacion: "gjgj" con desplazamiento 5 (shift) seria "bebe".

from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #si el usuario ingresa un simbolo, numero o espacio lo deja tal cual como lo ingreso.
    if char not in alphabet:
      end_text += char
    #si ingresa letras lo procesa con cifrado
    else:  
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#pregunta al usuario si desea continuar cifrando/descifrando o prefiere terminar el programa.
continuar = True
while continuar == True:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26 #sin importar cuan grande sea el numero ingresado lo lleva a las 26 letras del alfabeto.

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("\nDo you want to restart the program? (Yes or No) : ").lower()
  if restart == "no":
    continuar = False
    print("Goodbye")