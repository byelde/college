# include <stdio.h>
# include <stdlib.h>
# include <math.h>
# include <string.h>

void selectionSort( int *array, int len ) {

    int currentValue;
    int j;

    for ( int i = 1; i < len; i++ ) {
        currentValue = array[i];

        j = i-1;

        while ( j >= 0 && currentValue < array[j] ) {
            array[j+1] = array[j];
            j--;
        }
        array[j+1] = currentValue;
        
    }

} 

void printArray ( int *array, int len) {

    printf("[");
    for ( int i = 0; i < len; i++ ) {

        printf("%i", array[i]);
        
        if ( i != len-1 ) {
            printf(", ");
        }

    };
    printf("]\n");

}

int main () {

    system("cls");

    int array[] = {7, 1, 3, 6, 1, 8, '\0'};
    int len = sizeof(array)/sizeof(array[0]) - 1;

    printArray( array, len );
    selectionSort( array, len );
    printArray( array, len );

}
