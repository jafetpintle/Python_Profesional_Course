import time

def fiboGen():
    n1 = 1 
    n2 = 1
    counter = 0
    while True:
        if counter <= 1:
            counter +=1
            yield 1
        else:
            aux = n1 + n2
            n1 , n2 = n2, aux
            counter +=1
            yield aux

if __name__ == "__main__":
    fibonacci = fiboGen()
    for element in fibonacci:
        print(element)
        time.sleep(0.6)
