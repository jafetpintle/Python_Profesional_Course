#Challenge to know if a number is a prime number using static typed
def is_prime(number: int ) -> bool:
    divisors = 0
    for i in range(2,number):
        if number%i == 0 :
            divisors+=1
    return divisors ==0

def run():
    number: int = int(input("Type a number: "))
    if is_prime(number):
        print(str(number) , " is a prime number")
    else:
        print(str(number) , "isn't a prime number")

if __name__ == "__main__":
    run()