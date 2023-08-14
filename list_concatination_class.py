class ListOperations():
    def __init__(self, list_one, list_two):
        self.final_list = list_one + list_two
    
    def return_list(self):
        return self.final_list

def main():
    list_one = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    list_two = ['h', 'i', 'j', 'k', 'l', 'm', 'n']
    list_three = ['o', 'p', 'q', 'r', 's', 't', 'u']
    list_four = ['v', 'w', 'x', 'y', 'z']

    print("List One -> ", list_one)
    print("List Two -> ", list_two)
    print("List Three -> ", list_three)
    print("List Four -> ", list_four)

    listObjOne = ListOperations(list_one, list_two)
    list_five = listObjOne.return_list()
    print("List Five -> ", list_five)

    listObjTwo = ListOperations(list_three, list_four)
    list_six = listObjTwo.return_list()
    print("List Five -> ", list_five)

    list_seven = list_five+list_six
    print("List Seven -> ", list_seven)

if __name__=="__main__":
    main()
    