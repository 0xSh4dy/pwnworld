#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void callme(){
    system("/bin/cat flag.txt");
}
int main(){
    char buf1[100];
    char buf2[200];
   
    puts("Enter some data, I'll return something back!");
    fgets(buf1,100,stdin);
    strncpy(buf2,buf1,100);
    printf(buf2);
    puts("\nThat's it. Nice to meet you! Goodbye");
    return 0;
}