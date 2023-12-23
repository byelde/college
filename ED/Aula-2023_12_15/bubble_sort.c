# include <stdlib.h>
# include <string.h>
# include <math.h>
# include <stdio.h>

void bubbleSort ( int *array, int len ) {

    int flag = 0;
    int aux = 0;

    for ( int i = 0; i < len; i++ ) {

        flag = 0;
        aux = 0;

        for ( int j = 0; j < len - 1; j++ ) {

            if ( array[j] > array[j+1] ) {
                flag = 1;
                aux = array[j];
                array[j] = array[j+1];
                array[j+1] = aux;
            }
            
        }
        if (flag) {
            break;
        };
    };

}

int main () {

    int array[] = {1,3,6,7,9,19,18,'\0'};
    int len = (sizeof(array)/sizeof(array[0])) - 1;

    bubbleSort( array, len );

    printf("[ ");
    for ( int i = 0; array[i]; i++ ) {

        printf("%i", array[i]);
        if ( i != len - 1) {
            printf(", ");
        };

    }
    printf(" ]");


}