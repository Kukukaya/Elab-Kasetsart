#include <stdio.h>

#define SQUARE(x) ((x)*(x))

int main()
{
  printf("square of 2+2 is %d\n", SQUARE(2+2));
  printf("16 divided by square of 2+2 is %d\n", 16/SQUARE(2+2));
}