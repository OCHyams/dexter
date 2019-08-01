int g_a = 25;
int g_b = 7;
int g_c = 0;
__attribute__((always_inline))
static int fn_a(unsigned i)
{
  i %= 5;                           // DexLabel('before')
  int array[] {1, 3, 5, 25, 28};
  return array[i];                  // DexLabel('after')
}
int something()
{
  if (g_a == fn_a(0)
   || g_a == fn_a(1)
   || g_a == fn_a(2)
   || g_a == fn_a(g_b))
    g_c = g_a;

  return g_c;
}

// DexExpectWatchValue("i", "0", "1", "2", "7", on_line='before')
// DexExpectWatchValue("i", "0", "1", "2", "2", on_line='after')
