#include<stdio.h>
 
int main()
{

    char lable[] = "hello";
    char lable2[] = "hello";
    char *s = lable;
    char *t = lable2;
 
    if(s != NULL && t != NULL)
    {
        if(s == t)
        {
            printf("s and t are equal\n");
        }
        else
        {
            printf("s and t are unequal\n");
        }
 
    }
 
    return 0;
}
