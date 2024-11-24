int main()
{
  int val;

  printf("Enter a value: ");
  scanf("%d", &val);
  if ((50<=val) && (val<=200))
    printf("Good value.\n");
  else
    printf("Bad value.\n");

  return 0;
}