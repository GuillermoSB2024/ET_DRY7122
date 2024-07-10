def verificaras(asnumber):
    if 64512 <= asnumber <= 65534 or 4200000000 <= asnumber <= 4294967294:
        return "El AS es privado"
    else:
        return "El AS es público"

if __name == "__main":
    as_number = int(input("Introduce el número de AS de BGP: "))
    print(verificar_as(as_number))