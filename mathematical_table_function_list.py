"""
Creating a mathematical table using a list
"""
def calculate(num_list):
    for num in num_list:
        for one_num in num_list:
            print(one_num * num, end=" ")
        print("\n")
        

def main():
    list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    calculate(list_data)

if __name__=="__main__":
    main()