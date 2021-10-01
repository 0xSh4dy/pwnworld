#include<stdio.h>
#include<stdlib.h>
int main(){
    int luckyNums[10];
    int bestNum = 0 ;
    puts("Enter 10 numbers that are lucky for you");
    for(int i=0;i<11;i++){
        scanf("%d",&luckyNums[i]);
    }
   
    if(bestNum == 4){
        puts("Congrats, here's a flag for you\n");
        system("/bin/cat flag.txt");
    }
    return 0;
}