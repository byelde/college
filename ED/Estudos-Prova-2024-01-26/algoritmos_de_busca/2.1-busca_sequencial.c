# include <stdio.h>
# include <stdlib.h>
# include <math.h>
# include <string.h>

int sequential_search( int *array, int len_array, int target_value ) {

    int target_index = -1;

    for ( int i = 0; i < len_array; i++ ) {
        if ( array[i] == target_value ) {
            target_index = i;
            break;
        }
    }

    return target_index;

};

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

int main () {

    int array[] = {4, 6, 7, 9};
    int len_array = sizeof(array)/sizeof(array[0]);
    int target_index =  sequential_search(array, len_array, 7);

    printArray(array, len_array);

    if ( target_index == -1 ) {
        printf("Value not founded.");
    } else {
        printf("Value founded at index %i", target_index);
    }

};