# include <stdio.h>
# include <stdlib.h>
# include <math.h>
# include <string.h>

int bs_recursive( int *array, int len_array, int target_value, int init_index, int end_index, int target_index ) {

    if ( init_index > end_index ) {
        return target_index;
    }

    int middle_index = ceil( (init_index+end_index)/2 );

    // printf("%i-%i-%i\n", init_index, end_index, middle_index);

    if ( array[middle_index] == target_value ){
        target_index = middle_index;
        return target_index;

    } else if ( array[middle_index] > target_value ) {
        return bs_recursive( array, len_array, target_value, init_index, middle_index-1, -1);

    } else {
        return bs_recursive( array, len_array, target_value, middle_index+1, end_index, -1);

    }
}

void printArray ( int *array, int len_array ) {

    printf("[");

    for ( int i = 0 ; i < len_array; i++ ) {

        printf("%i", array[i]);
        if ( i != len_array-1 ) {
            printf(", ");
        };

    };

    printf("]\n");

}

int main () {

    int array[] = {4, 6, 7, 9, 10};
    int len_array = sizeof(array)/sizeof(array[0]);
    int target_index = bs_recursive(array, len_array, 6, 0, len_array-1, -1);
    
    printArray(array, len_array);

    printf("%i", target_index);

}