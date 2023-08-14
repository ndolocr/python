class ListOperator():
    def __init__(self, list_param):
        self.list_param = list_param

    def calculate_multiples(self):
        for val in self.list_param:
            for num in self.list_param:
                print(val*num, end=" ")
            print("\n")

def main():
    list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    mult = ListOperator(list_data)
    mult.calculate_multiples()

if __name__ == "__main__":
    main()