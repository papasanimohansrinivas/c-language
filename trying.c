 #include <stdio.h>
 #include <conio.h>
 #include <string.h>

 int main()
{
	
 char mem[]="*";
 int r[]="1234567\0";
 printf("%d",strlen(r));
 int k=0;
 int e;
 do
{
 for(e=0;e<r[k];e++)
 {
  printf("%s",mem);
 }
 printf("\n");
  
 k++;
}
while(k<strlen(r));


 getchar();
}