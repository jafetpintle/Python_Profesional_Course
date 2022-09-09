def make_division_by(den : int):
    def div(num : int):
        return num / den
    return div

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_3 = make_division_by(5)
    print(division_by_3(100))
    
    division_by_3 = make_division_by(18)
    print(division_by_3(54))
    
if __name__ == "__main__":
    run()