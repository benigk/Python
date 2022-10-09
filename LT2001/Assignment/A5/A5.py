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

   
