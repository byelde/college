def bubbleSort ( array ):
    
    for i in range (len(array)):
        
        flag = False;
        
        for j in range (1, len(array)-i):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j];
                flag = True;

        if not flag:
            break       
        

if __name__ == "__main__":
    array = [7, 6, 9, 4, 5];
    print(array);
    bubbleSort(array);
    print(array);