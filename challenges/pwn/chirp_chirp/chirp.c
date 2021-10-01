#include<stdio.h>
#include<stdlib.h>
void you_win(){
    system("/bin/cat flag.txt");
}
void vuln(){
    char name[20];
    puts("Hey, what's your name?\n");
    fgets(name,200,stdin);
    printf(name);
    char buf[40];
    puts("\nCanary *chirp *chirp ***\n");
    fgets(buf,0x40,stdin);
}
int main(){
    
    vuln();
    return 0;
}