from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Execution time: "+ str(time_elapsed.total_seconds()) + " seconds")
    return wrapper

@execution_time
def random_funct():
    for _ in range(1, 10000000):
        pass

@execution_time
def sum(a : int , b : int) -> int:
    return a + b

def run():
    print("For loop time")
    random_funct()
    print("Sum")
    sum(5,5)

if __name__ == "__main__":
    run()
