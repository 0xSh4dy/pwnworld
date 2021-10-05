#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
void ignore_me_init_buffering() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

void kill_on_timeout(int sig) {
  if (sig == SIGALRM) {
  	printf("[!] Anti DoS Signal. Patch me out for testing.");
    _exit(0);
  }
}
void ignore_me_init_signal() {
	signal(SIGALRM, kill_on_timeout);
	alarm(60);
}
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
    ignore_me_init_buffering();
    ignore_me_init_signal();
    signal(SIGINT,signal2_handler);
    signal(SIGTSTP,signal3_handler);
    signal(SIGQUIT,signal1_handler);
    puts("Welcome to the first pwn challenge of pwnworld\n");
    fgets(name,20,stdin);
    return 0;
}
