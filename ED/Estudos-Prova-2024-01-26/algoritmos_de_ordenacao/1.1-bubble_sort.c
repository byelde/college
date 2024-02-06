# include <stdlib.h>
# include <stdio.h>
# include <string.h>
# include <math.h>

void printArray ( int *array, int len_array ) {

    printf("[");

    for ( int i = 0 ; i < len_array; i++ ) {

        printf("%i", array[i]);
        if ( i != len_array-1 ) {
            printf(", ");
        };

    };

    printf("]\n");

};

void bubbleSort( int *array, int len_array ) {

    int j, i, aux, flag;

    for ( i = 0; i < len_array; i++ ) {

        flag = 0;

        for (j = 1; j < len_array - i; j++) {

            if ( array[j] < array[j-1] ) {
                aux = array[j];
                array[j] = array[j-1];
                array[j-1] = aux;
                flag = 1;
            };

        };
        
        if ( flag == 0) {
            break;
        };

    };


}

int main () {

    int array[] = {7, 6, 9, 4, 5};
    int len_array = (sizeof(array)/sizeof(array[0]));

    printArray(array, len_array);
    bubbleSort(array, len_array);
    printArray(array, len_array);
}