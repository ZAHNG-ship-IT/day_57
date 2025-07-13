#include <stdio.h>
//递归求阶乘
int fun(int n)
{
    if(n <= 1) 
        return 1;
    else 
        return n * fun( n - 1);
}

int main()
{
    int b;

    // b = scanf("%d",&b);这行代码是错误的
    scanf("%d",&b);
    // int ret = 1 fun(b);
    int ret = fun(b); 
    printf("%d",ret);
    return 0;

}

//递归有时候不好用，迭代，例如求解第n个斐波那契数列，时间复杂度太大了
//汉诺塔问题，青蛙跳台问题