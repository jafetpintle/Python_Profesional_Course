import time

def fiboGen(max : int) -> int:
    n1 = 1 
    n2 = 1
    counter = 0
    while counter < max:
        if counter <= 1:
            counter +=1
            yield 1
        else:
            aux = n1 + n2
            n1 , n2 = n2, aux
            counter +=1
            yield aux

if __name__ == "__main__":
    max :int = int(input("Numbers of fibonacci susecion:"))
    fibonacci = fiboGen(max)
    for element in fibonacci:
        print(element)
        time.sleep(0.6)
