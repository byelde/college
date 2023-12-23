// USING >>ONE ARRAY<<

# include <stdlib.h>
# include <stdio.h>
# include <string.h>
# include <math.h>

void selectionSort( int *array, int len_array ) {

    int min_index;
    int aux;
    
    for ( int i = 0; i < len_array; i++ ) {

        min_index = i;

        for ( int j = i; j < len_array; j++) {
            if ( array[min_index] > array[j] ) {
                min_index = j;
            };
        };

        if ( array[i] > array[min_index] ){
            aux = array[min_index];
            array[min_index] = array[i];
            array[i] = aux;
        }

    }
};

int main () {

    system("cls");

    int list[] = {1, 8, 3, 8, 3, 5, 6, 3, 7, 9, 5, '\0'};
    int len_list = (sizeof(list)/sizeof(list[0])) - 1;

    selectionSort( list, len_list );

    printf("[");
    for ( int i = 0; i < len_list; i++ ) {

        printf("%i", list[i]);
        
        if ( i != len_list-1 ) {
            printf(", ");
        }

    };
    printf("]");

}