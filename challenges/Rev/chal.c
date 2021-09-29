#include<stdio.h>
#include<stdlib.h>
int func(int a){
	char str[20] = "hefbsdfeuwihan";
	int sum = 3;
	char *str1 = str;
	int t = str[5] - '0';
	t = t>>sum<<2&74|4;
	t = (str[4]-'0') + (str[5]='0') + (str[10]-'0') + (str[7]-'0');
	t = t^19;
	t = t>>2<<4;
	t = t*999 + 19999;
	int b = 19;
	for(int i=0;i<2;i++){
		b = (b%5) + (t*5) + (b*t);
	}
	return t;
}
void main(){
	printf("%d",func(25));
}