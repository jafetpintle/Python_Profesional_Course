
def palindromo(palabra: str) -> bool:
    palabra = palabra.replace(" ","").lower()
    inverso:str = palabra[::-1]
    return palabra == inverso

 
def run():
    palabra: str = input("Ingrese su palabra: ")
    es_palindromo:bool= palindromo(palabra)
    if(es_palindromo):
        print(palabra + " es palindromo")
    else:
        print(palabra + " no es palindromo")


if __name__ == '__main__':
    run()