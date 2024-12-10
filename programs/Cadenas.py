# Estas son cadenas de texto
print("Hello World")
# En Python podemos usar ambas comillas "dobles" y 'simples'
print('Este es un texto que incluye ""')
# Se pueden alternar ambas comillas para mostrarlas y viceversa, esto es algo unico de python
print("Esta 'palabra' se encuentra escrita entre comillas simples")

# Secuencias de escape
print("Esta \"palabra\" se encuentra escrita para colocar comillas del mismo tipo")
print('Esta es una \"palabra\" se encuentra escrita por las mimsas comillas simples')
print('una cadena')
print("otra cadena")
print("Un texto \t una tabulacion")
print("Un testo \n desde un salto de linea")
print("C:\nombre\directorio")

#! Nota: Esto tiene que ser ejecutado en la terminal, o en la version 9 o 10 de python3 
# # print(r"C:\nombre\directoriox\")
# print("""Una linea)

c = "Esto es una cadena \n de dos lineas"
print(c)
type(c)     #! NOTA: el type() se usa para conocer el tipo de dato de dicha variable

#  Operaciones
c = "Esto es una cadena\n con dos lineas"
print(c + c)

# Esta es la forma de hacer una cadena compuesta en una variable string
s = "una cadena" "compuesta de dos cadenas"
print(s)

# Igual pueden sumar variables string
c1 = "Una cadena"
c2 = "Otra cadena"
print("Una cadena" + c2)

# Para imprimir una cadena n veces se usa el * como multiplicador en vez de un array
then_spaces = " " *10
print(then_spaces + "Un texto a diez espacios")

# Otra forma de multiplicar tus cadenas
m = "Hola"
print(m*10)

# Indices en las cadenas
palabra = "Python"
palabra[0]
print(palabra[0])
print(palabra[3])
print(palabra[-0])