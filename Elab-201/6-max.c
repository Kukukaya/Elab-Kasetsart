#include <stdio.h>

// การประกาศฟังก์ชันสามารถละชื่อพารามิเตอร์เอาไว้ได้
int max_of_three(int,int,int);
int main()
{
  int a,b,c;
  printf("Enter three integers: ");
  scanf("%d %d %d", &a, &b, &c);
  printf("The maximum value is %d\n", max_of_three(a,b,c));
}

int max_of_three(int x, int y, int z) {
    if (x > y && x > z)
        return x;
    else if (y > z)
        return y;
    else
        return z;
}