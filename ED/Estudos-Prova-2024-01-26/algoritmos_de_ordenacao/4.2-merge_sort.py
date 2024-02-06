from math import ceil

def mergeSort( array ):
    
    if len(array) == 1:
        return array;
    
    init_index = 0;
    end_index = len(array)-1;
    middle_index = ceil((init_index+end_index)/2);
    
    result_array = [0 for k in range(len(array))];
    left_part = mergeSort(array[:middle_index]);
    right_part = mergeSort(array[middle_index:]);
    
    l = r = p = 0

    while l < len(left_part) and r < len(right_part):
        if left_part[l] < right_part[r]:
            result_array[p] = left_part[l];
            l += 1;
    
        else:
            result_array[p] = right_part[r];
            r += 1;
        p += 1;
    
    while l < len(left_part):
        result_array[p] = left_part[l];
        l += 1;
        p += 1;
            
    while r < len(right_part):
        result_array[p] = right_part[r];
        r += 1;
        p += 1;
        
    return result_array;
        
            
    
if __name__ == "__main__":
    array = [7, 6, 9, 4, 5];
    print(array);
    array = mergeSort( array );
    print(array);