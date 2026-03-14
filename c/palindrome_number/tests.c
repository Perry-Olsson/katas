#include "main.h"
#include <assert.h>
#include <stdio.h>

void test_1(void) {
    assert(is_palindrome(121));
    printf("test_1: PASS\n");
}

void test_2() {
    assert(!is_palindrome(-121));
    printf("test_2: PASS\n");
}

void test_3() {
    assert(!is_palindrome(10));
    printf("test_3: PASS\n");
}

void test_4() {
    assert(is_palindrome(1001));
    printf("test_4: PASS\n");
}


int main(void) {
    test_1();
    test_2();
    test_3();
    test_4();
    return 0;
}
