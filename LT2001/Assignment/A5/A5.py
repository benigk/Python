
from ast import Delete


def main():


    if __name__=='__main__':
    
        main()

def trimmed_max(xs, y):
    new_list = []
    for element in xs:
        if element < y:
            new_list.append(element)
            print('element:', element) 
    max_value = max(new_list)
    return max_value 
    
print(trimmed_max([-3,5,-0.1,-100,1,5000],0))

<<<<<<< HEAD
=======
def normalize_spaces(text):
    new_list = []
    front_char = ' '
    for current in text:
        if current != ' ':
            new_list.append(current)
        elif front_char != ' ':
            new_list.append(current)
        front_char = current
        print(new_list)
    new_list.pop(len(new_list)-1)
    print(new_list)
        
normalize_spaces(" What's up,    doc?     ")

    
>>>>>>> c71b7c2717a996e695b453d296a84b1db564fb0f
   
