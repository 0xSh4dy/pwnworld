#include<stdio.h>
int main(){
    char pwnybuff[40];
    puts("Hello there! This challenge will teach you the basics of ret2libc attack");
    puts("So, get ready to improve your pwn skills");
    puts("Since this is the first challenge related to ret2libc, I would provide you some help! ");
    printf("%p ,a small gift for you!\n",&fgets);
    gets(pwnybuff);
    return 0;
}