string = ",,,,blabla,"
string = string.strip(",")
print(string)
string2 = ",,,,blabla,"
for c in string2:
    if c == ",":
        string2 = string2.strip(c)
print(string2)

lista = ["hola"]
print(lista)
