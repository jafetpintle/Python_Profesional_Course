import string


def mayusculas(func):
    def wrapper(text : str):
        return func(text).upper()
    return wrapper

@mayusculas
def mensaje(nombre: string):
    return f'{nombre}, recibiste un mensaje'

def run():
    print(mensaje("Cesar"))

if __name__ == "__main__":
    run()