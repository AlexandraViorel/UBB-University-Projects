// 19. Read from file numbers.txt a string of numbers (positive and //negative). Build two strings using readen numbers:
//P – only with positive numbers
//N – only with negative numbers
//Display the strings on the screen.

#include <stdio.h>

void pozitivnegativ(int number, int p[], int l1, int n[], int l2);

int main()
{
    int p[20];
    int n[20];
    int l1=0, l2=0;
        
    FILE *the_file;
    int x;
    
    the_file = fopen("numbers.txt", "r");
    
    if (the_file == NULL)
    {
        printf("The file cannot be opened for reading.\n");
    }
    else
    {
        while (fscanf(the_file, "%d", &x)!=EOF)
        {
            pozitivnegativ(x, p, l1, n, l2);
            if (x < 0)
            {
                l2 += 4;
            }
            else
            {
                l1 += 4;
            }
        }
        l1 = l1/4;
        l2 = l2/4;
        
        for (int i =1;i<=l1;i++)
            printf("%d ", p[i]);
        printf("\n");
        for (int i=1;i<=l2;i++)
            printf("%d ", n[i]);
        
    }
    fclose(the_file);
    return 0;
}