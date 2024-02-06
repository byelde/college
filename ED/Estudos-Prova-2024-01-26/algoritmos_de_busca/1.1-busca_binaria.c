# include <stdlib.h>
# include <stdio.h>
# include <string.h>
# include <math.h>

int binary_search ( int *array, int len_array, int target_value ) {

    int init_index = 0;
    int end_index = len_array-1;
    int middle_index;
    int target_index = -1;

    while (1) {

        middle_index = ceil((init_index + end_index)/2);

        if ( array[middle_index] == target_value ) {
            target_index = middle_index;
            break;

        } else if ( array[middle_index] > target_value ) {
            end_index = middle_index-1;

        } else /*array[middle_index] < target_value*/ {
            init_index = ++middle_index;
        };

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

}

int main () {

    int array[] = {4, 6, 7, 9, 10};
    int len_array = (sizeof(array)/sizeof(array[0]));
    int target_index = binary_search(array, len_array, 10);

    printArray(array, len_array);

    if (target_index == -1) {
        printf("Value not founded.");
    } else {
        printf("Value founded at index %i.", target_index);
    }

}