#include "main.h"
#include <assert.h>
#include <stdio.h>

void test_swap(void) {
    int a = 1;
    int b = 2;
    swap(&a, &b);
    assert(a == 2);
    assert(b == 1);
    printf("test_swap: PASS\n");
}

int main(void) {
    test_swap();
}
