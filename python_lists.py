"""
This is a file used to lear
all there is in python LISTS
"""
def get_list_length(letter_list):
    list_lenght = len(letter_list)
    return list_lenght

class ListLearning():
    def __init__(self, l_list):
        self.letter_list = l_list
        
    def display_list(self):        
        return len(self.letter_list)

def main():
    l = [ 'a', 'b', 'c', 'd']
    
    # Getting lenght of a list
    length_of_list = get_list_length(l)
    print("Lenght of list from function based view is -> ", length_of_list)

    # Getting length of a list from class based views
    list_example = ListLearning(l)
    print("Length of list fom class based view is -> ", list_example.display_list())

if __name__ == '__main__':
    main()
