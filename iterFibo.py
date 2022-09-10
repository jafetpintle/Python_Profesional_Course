import time


class IterFibo:
    """Class who calculate the fibonacci sucesion"""
    def __init__(self , max):
        self.max = max

    def __iter__(self):
        self.first_fib = 1
        self.sec_fib = 1
        self.count = 1
        return self
    
    def __next__(self):
        if  self.count <= self.max:  
            if self.count <=2:
                self.count +=1
                return 1
            else:
                self.result = self.first_fib + self.sec_fib
                self.first_fib, self.sec_fib = self.sec_fib, self.result
                self.count+=1
                return self.result
        else:
            raise StopIteration

def run():
    fibonacci = IterFibo(5)
    for elemenet in fibonacci:
        print(elemenet)
        time.sleep(0.5)

if __name__ == "__main__":
    run()