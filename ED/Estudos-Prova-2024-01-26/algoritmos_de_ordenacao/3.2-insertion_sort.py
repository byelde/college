def insertionSort (array):
    len_array = len(array);
    
    for i in range(1, len_array):
        
        current_value = array[i];
        
        j = i-1;
        
        while (j >= 0 and current_value < array[j]):
            array[j+1] = array[j];
            j -= 1;
            
        array[j+1] = current_value

if __name__ == "__main__":
    array = [7, 6, 9, 4, 5];
    print(array);
    insertionSort( array );
    print(array);