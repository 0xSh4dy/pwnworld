#include<stdio.h>
#include<stdlib.h>

void callme(){
    system("/bin/cat flag.txt");
}
void fakeFlag(){
    puts("flag{this_is_a_fake_flag}");
}

int main(){
    srand(154345);
    int entry;
    char usrInput[10];
    char *pwn = (char *)malloc(48);
    void(*func_ptr_t)(void); 
    func_ptr_t = fakeFlag;
    void(**fptr)(void) = malloc(16);
    *fptr = func_ptr_t;
    entry = rand();
    entry = (entry ^ 5)>>2;
    puts("Hey there, enter the passcode!");
    fgets(usrInput,10,stdin);
    if(atoi(usrInput)==entry){
        puts("Cool, now you can continue");
        fgets(pwn,0x64,stdin);
        (*fptr)();
        
    }
    else{
        puts("???????? Invalid passcode");
    }
    return 0;
}