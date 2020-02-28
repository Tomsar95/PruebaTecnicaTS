
#---------------------------------------------------------------------------------------------
# #1.     Iterar un array e imprimir sólo números pares.
# array1 = [3, 2, 5, 6, 5, 3, 3, 8]
# for i in range(0,len(array1)):
# 	if array1[i] % 2 == 0:
# 		print(array1[i])

#---------------------------------------------------------------------------------------------
# #2.     Iterar un array e imprimir sólo números impares.
# array1 = [3, 2, 5, 6, 5, 3, 3, 8]
# for i in range(0,len(array1)):
# 	if array1[i] % 2 != 0:
# 		print(array1[i])

#---------------------------------------------------------------------------------------------
# # 3.     Generar una cadena alfanumérica aleatoria.
# from random import choice
# from string import digits, ascii_lowercase

# letter = digits + ascii_lowercase
# text = ["".join([choice(letter) for i in range(10)])]
# print(text)

#---------------------------------------------------------------------------------------------
# # 4.     Ordenar un array de números.
# array1 = [3, 2, 5, 6, 5, 3, 3, 8]
# array1.sort()
# print('Sorted array :'+str(array1))

#---------------------------------------------------------------------------------------------
# # 5.     Convertir una cadena underscore a camelcase.
# sampleTxt = 'hola_como_estas'

# def underscoreToCamelCase(word):
# 	return ''.join(x.capitalize() or '_' for x in word.split('_'))

# newTxt = underscoreToCamelCase(sampleTxt)
# print(newTxt)

#---------------------------------------------------------------------------------------------
# # 6.     Unir dos arrays en uno solo.
# array1 = [3, 2, 5, 6, 5, 3, 3, 8]
# array2 = [5, 5, 2, 1, 3, 6, 1, 9] 
  
# for i in array2 : 
#     array1.append(i) 
# print ('Concatenated array : ' + str(array1)) 

#---------------------------------------------------------------------------------------------
# 7.     Generar números aleatorios, hasta encontrar N números pares.
# import numpy as np
# oddCount = 0
# for i in range(0,100):
# 	value = np.random.randint(10, size = 1)
# 	if value % 2 == 0:
# 		oddCount += 1
# 		print('count: '+str(oddCount)+' Value: '+str(value[0]))
# 		if oddCount == 10:
# 			break

#---------------------------------------------------------------------------------------------
# # 8.     Generar números aleatorios, hasta encontrar N números impares.
# import numpy as np
# evenCount = 0
# for i in range(0,100):
# 	value = np.random.randint(10, size = 1)
# 	if value % 2 != 0:
# 		evenCount += 1
# 		print('count: '+str(evenCount)+' Value: '+str(value[0]))
# 		if evenCount == 10:
# 			break

#---------------------------------------------------------------------------------------------
# # 9.     Iterar un array e imprimir solo palabras que empiecen con vocal.
# arrayTxt = ['hola','carro','azul','imprimir','caducar','externo','python','excel']
# vowels =('a', 'e', 'i', 'o', 'u')

# def extractVowelWords (arrayTxt, vowels):
# 	for i in arrayTxt:
# 		# print(i)
# 		# print(len(i))
# 		if (i[0] in vowels) == True:
# 			print(i)

# extractVowelWords(arrayTxt,vowels)

#---------------------------------------------------------------------------------------------
# 10.     Iterar un array e imprimir solo palabras que empiecen con vocal.
# arrayTxt = ['hola','carro','azul','imprimir','caducar','externo','python','excel']
# vowels =('a', 'e', 'i', 'o', 'u')

# def extractVowelWords (arrayTxt, vowels):
# 	for i in arrayTxt:
# 		# print(i)
# 		# print(len(i))
# 		if (i[0] in vowels) == False:
# 			print(i)

# extractVowelWords(arrayTxt,vowels)











