int main()
{
    int a = 0;
    a = 0;      //DexWatch('a')
    a = 0;      //DexWatch('a')
    a = 0;      //DexWatch('a')
    a = 0;      //DexWatch('a')
    return a;   //DexWatch('a')
}

// DexVerify(Henceforth(Expect('a', '0')))
