#include "main.h"
#include <stdio.h>
#include <string.h>

bool is_palindrome(int x) {
    char str[20];
    sprintf(str, "%d", x);
    if (str[0] == '-') {
        return false;
    }

    int left = 0;
    int right = strlen(str) - 1;
    while (left < right) {
        if (str[left] != str[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}


