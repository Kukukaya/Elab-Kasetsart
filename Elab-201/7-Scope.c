#include <stdio.h>

int x;

void func1()
{
  
int x = 1111;

  printf("In func1(), x=%d\n", x);
}

void func2()
{
  
x = 2222;

  printf("In func2(), x=%d\n", x);
}

void func3(int x)
{
  printf("In func3(), x=%d\n", x);
}

int main()
{
  x = 5678;
  printf("In main(), x=%d\n", x);
  func1();
  printf("In main() after func1(), x=%d\n", x);
  func2();
  printf("In main() after func2(), x=%d\n", x);
  func3(3333);
  printf("In main() after func3(), x=%d\n", x);
}