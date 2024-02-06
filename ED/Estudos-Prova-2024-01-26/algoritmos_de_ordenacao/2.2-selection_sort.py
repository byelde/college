def selectionSort( array ):
    
    for i in range(len(array)):
        
        min_value_index = i;
        
        for j in range(i, len(array)):
            if array[j] < array[min_value_index]:
                min_value_index = j;
        
        array[i], array[min_value_index] = array[min_value_index], array[i]



if __name__ == "__main__":
    array = [7, 6, 9, 4, 5];
    print(array);
    selectionSort( array );
    print(array)