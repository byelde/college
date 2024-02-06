from math import ceil

def binary_search( array, target_value ):
    
    len_array = len(array);
    init_index = 0;
    end_index = len_array-1;
    target_index = -1;
    
    while ( True ):

        middle_index = ceil((init_index+end_index) / 2)
        
        if (array[middle_index] == target_value):
            target_index = middle_index;
            break;
        
        elif ( array[middle_index] > target_value ):
            end_index = middle_index-1;
            
        elif ( array[middle_index] < target_value ):
            init_index = middle_index+1;
        
    return target_index;

if __name__ == "__main__":
    array = [4, 6, 7, 9, 10];
    target_index = binary_search(array, 10)
    
    print(array);
    
    if (target_index == -1):
        print("Value not founded");
    else:
        print(f"Value founded at index {target_index}")