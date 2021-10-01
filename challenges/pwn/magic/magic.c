#include<signal.h>
#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>

int flag = 0;
void signal1_handler(){
    if(!flag){
    flag = 1;
    }
    else{
        exit(0);
    }
}

void signal2_handler(){
    flag++;
}
void signal3_handler(){
    if(flag==2){
        system("/bin/cat flag.txt");
    }
    else{
        puts("Try harder");
    }
    exit(0);
}

int main(int argc, char **argv){
    char name[20];
    signal(SIGINT,signal2_handler);
    signal(SIGTSTP,signal3_handler);
    signal(SIGQUIT,signal1_handler);
    puts("Welcome to the first pwn challenge of pwnworld\n");
    fgets(name,20,stdin);
    return 0;
}
