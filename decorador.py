def decorator(func):
    def wrappper(): #It will change the behabior of our function func 
        print("New function added")
        func()
    return wrappper

@decorator
def hello():
    print("Hello world!")

def run():
    print("Decorator function\n")
    hello()

if __name__ == "__main__":
    run()