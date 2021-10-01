#include<stdio.h>
#include<stdlib.h>

int main(){
    
    int secret_key = rand();
    int userInput;
    puts("Hello user! You need to enter the secret key to get in!\n");
    scanf("%d",&userInput);
    if(userInput==secret_key){
        system("/bin/cat flag.txt");
    }
    else{
        puts("Invalid key! Please try again later\n");
    }
}