int main()
{
    int a = 0;
    a = 1;      //DexWatch('a')
    a = 0;
    a = 0;
    a = 0;
    return a;   //DexWatch('a')
}

// DexVerify(Eventually(Henceforth(Expect('a', '0'))))
