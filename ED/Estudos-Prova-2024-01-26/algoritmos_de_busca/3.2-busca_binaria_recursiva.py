from math import ceil

def bs_recursive( array, target_value, end_index, init_index = 0):
    
    if ( init_index > end_index ):
        return -1;
    
    middle_index = ceil((init_index+end_index)/2);
    
    if ( array[middle_index] == target_value ):
        return middle_index;
    
    elif ( array[middle_index] > target_value):
        return bs_recursive(array, target_value, init_index, middle_index-1);
    
    else:
        return bs_recursive(array, target_value, middle_index+1, end_index);


if __name__ == "__main__":
    array = [4, 6, 7, 9];
    len_array = len(array);
    target_index = bs_recursive( array, 7, len_array-1 );
    
    print(array);
    
    if ( target_index == -1):
        print("Value not founded.");
    else:
        print(f"Value founded at index {target_index}.")