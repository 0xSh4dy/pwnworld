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
int main(){
    char pwnybuff[40];
    ignore_me_init_buffering();
	ignore_me_init_signal();
    puts("Hello there! This challenge will teach you the basics of ret2libc attack");
    puts("So, get ready to improve your pwn skills");
    puts("Since this is the first challenge related to ret2libc, I would provide you some help! ");
    printf("%p ,a small gift for you!\n",&fgets);
    gets(pwnybuff);
    return 0;
}