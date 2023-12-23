// USING >>TWO ARRAYS<<

# include <stdlib.h>
# include <stdio.h>
# include <string.h>
# include <math.h>

void selectionSort( int *array, int *target, int len_array ) {
    
    int min_index;
    for ( int i = 0; i < len_array; i++ ) {

        min_index = i;

        for ( int j = i; j < len_array; j++) {

            if ( array[j] <= array[min_index] ) {
                min_index = j;
            }
        };

        target[i] = array[min_index];
        array[min_index] = NULL;

    }
};

int main () {

    system("cls");

    int list[] = {1, 8, 3, 8, 3, 5, 6, 3, 7, 9, 5, '\0'};
    int len_list = (sizeof(list)/sizeof(list[0])) - 1;
    int sorted_list[len_list+1];

    selectionSort( list, sorted_list, len_list );

    printf("[");
    for ( int i = 0; i < len_list; i++ ) {

        printf("%i", sorted_list[i]);
        
        if ( i != len_list-1 ) {
            printf(", ");
        }

    };
    printf("]");

}