def quickSort( array, init = 0, end = None ):
    if end is None:
        end = len(array) - 1
    
    if init < end:
        
        pivot = array[end];
        i = init;
        
        for j in range(init, end):
            if array[j] <= pivot:
                array[i], array[j] = array[j], array[i];
                i += 1;
        
        array[i], array[end] = array[end], array[i];
        
        partition = i;
        
        quickSort(array, init, partition-1);
        quickSort(array, partition+1, end)
        
    return array;
        
    
array = [9, 1, 7, 4];
print(quickSort(array));