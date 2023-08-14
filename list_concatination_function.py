"""
In this we learn on how to concatinate lists in Python
"""

def concatinate_list(first, second):
    conc_list = first + second
    return conc_list

def main():
    list_one = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    list_two = ['h', 'i', 'j', 'k', 'l', 'm', 'n']
    list_three = ['o', 'p', 'q', 'r', 's', 't', 'u']
    list_four = ['v', 'w', 'x', 'y', 'z']

    print("List One -> ", list_one)
    print("List Two -> ", list_two)
    print("List Three -> ", list_three)
    print("List Four -> ", list_four)

    list_five = concatinate_list(list_one, list_two)
    list_six = concatinate_list(list_three, list_four)
    
    print("List Five -> ", list_five)
    print("List Six -> ", list_six)

    list_seven = list_five+list_six

    print("List Seven -> ", list_seven)


if __name__=="__main__":
    main()