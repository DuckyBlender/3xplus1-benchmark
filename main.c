#include <stdio.h>
#include <time.h>

int main()
{
    clock_t t;
    printf("Start!\n");
    t = clock();
    unsigned int num;

    for (unsigned int i = 1; i <= 1000000; i++) {
        num = i;
        while(1) {
            if (num == 1) {
                break;
            }
            else if (num % 2 == 0) {
                num = num / 2;
            }
            else if (num % 2 == 1) {
                num = 3 * num + 1;
            }
        }
    }
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("End! This took %f seconds!\n", time_taken);
    return 0;
}