import numpy as np;
import time;

def mergeSort ( array ):
    
    if ( len(array) > 1 ):
        
        resultArray = [ 0 for i in range(len(array)) ];
        
        middleIndex = (len(array))//2;
        
        leftSide = array[:middleIndex];
        rightSide = array[middleIndex:];

        leftSide = mergeSort(leftSide);
        rightSide = mergeSort(rightSide);
        
        i = j = k = 0;
        
        while i < len(leftSide) and j < len(rightSide):
            if leftSide[i] < rightSide[j]:
                resultArray[k] = leftSide[i];
                i += 1;
            else:
                resultArray[k] = rightSide[j];
                j += 1;
            k += 1;
            
        while i < len(leftSide):
            resultArray[k] = leftSide[i];
            i += 1;
            k += 1;
        
        while j < len(rightSide):
            resultArray[k] = rightSide[j];
            j += 1;
            k += 1;
            
        return resultArray;
    
    return array;
                 
        
        
if __name__ == "__main__":
    
    array = np.random.randint( low=1, high=500_000, size= 500_000 );
    array = list(array);
    
    # print(array);
    init = time.time()
    print(mergeSort( array ));
    end = time.time()

    print(f"|{end-init:.20f}|");