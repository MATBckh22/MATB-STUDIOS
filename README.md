# Lab Practice 2

## Sums of Integers to 10

```C
#include <stdio.h>

int main(){
    int sum = 0;
    for (int i = 0; i < 11; i++){
        printf("%d\n",sum);
        sum += i;
    }
    printf("%d\n",sum);
    return 0;
}
```

## Sums and Average

```C
#include <stdio.h>

int main(){
    int sum = 0, number;
    float average;
    for (int i = 0; i < 11; i++){
        scanf("%d",&number);
        sum += number;
    }
    average = sum/10;
    printf("The sum is %d and the average is %.2f", sum, average);
}
```

## Multiplication Table

```C
#include <stdio.h>

int main(){
    int number;
    scanf("%d", &number);
    for (int i = 1; i <= 20; i++){
        printf("%d x %d = %d\n", number, i, i*number);
    }
    return 0;
}
```

## Sum and Average of n Terms

```C
#include <stdio.h>
#include <math.h>

int main(){
    int sum = 0, n, count = 0;
    float average;
    scanf("%d", &n);
    printf("The odd numbers until %d are\n", n);
    for (int i = 0; i <= n; i++){
        if (i % 2 != 0){
            count += 1;
            sum += i;
            printf("%d\n", i);
        }
    }
    average = sum/count;
    printf("The sum is %d and the average is %.2f", sum, average);
    printf("%d\n", count);
    return 0;
}
```

## Right angle Triangle of Numbers

```C
#include <stdio.h>
#include <math.h>

int main(){
    int n;
    scanf("%d",&n);
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= i; j++){
            printf("%d",j);
        }
        printf("\n");
    }
    return 0;
}
```

## Factorial 

```C
#include <stdio.h>
#include <math.h>

int main(){
    int n, fact = 1;
    scanf("%d",&n);
    for (int i = 1; i <= n; i++){
        fact *= i;
    }
    printf("The factorial for %d is %d", n, fact);
    return 0;
}
```

