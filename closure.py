from bisect import insort_right


def repeat_string(number : int ): #Superior order function
    def rept(word : str): 
        assert type(word) == str, "Only can use strings" #Assert to check if only use strings
        return word*number 
    return rept

def run():
    repeat_5 = repeat_string(5) #Call my function and save the number, returning the nested function
    print(repeat_5("Closure")) #This will print Closure five times

    repeat_10 = repeat_string(10) #Set number 10 to repeat
    print(repeat_10("Hi_World_"))#This will repeat Hi_World_ ten times

if __name__ == "__main__":
    run()