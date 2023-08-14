"""
This is a file used to lear
all there is in python LISTS
"""
def get_list_length(letter_list):
    list_lenght = len(letter_list)
    return list_lenght

def main():
    l = [ 'a', 'b', 'c', 'd']
    
    # Getting lenght of a list
    length_of_list = get_list_length(l)
    print("Lenght of letter list is -> ", length_of_list)
    
if __name__ == '__main__':
    main()
