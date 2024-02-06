def sequential_search(array, target_value):
    
    len_array = len(array);
    target_index = -1;
    
    for i in range(len_array):
        if array[i] == target_value:
            target_index = i;
            break;
    
    return target_index;


if __name__ == "__main__":
    array = [4, 6, 7, 9];
    target_index = sequential_search( array, 7 );
    
    print(array);
    
    if ( target_index == -1 ):
        print("Value not founded.");
    else:
        print(f"Value founded at index {target_index}");