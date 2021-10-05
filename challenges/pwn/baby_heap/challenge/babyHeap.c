#include<stdio.h>
#include<stdlib.h>
int main(){
    char *trash = (char *)malloc(40);
    int *modifyMe = (int *)malloc(4);
    *modifyMe = 1;
    puts("Hey there, welcome to the first heap overflow challenge");
    printf("trash is stored at %p, and modifyMe is stored at %p\n",trash,modifyMe);
    gets(trash);
    if(*modifyMe!=1){
        system("/bin/cat flag.txt");
    }
    else{
        puts("Try harder");
    }
    return 0;
}