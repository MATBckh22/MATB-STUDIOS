# Practical Handbook for Programming in C

## Indexing Arrays with `for` Loops

Looping with `for` keyword but using the last index as the value to stop counter:

```C
const int SIZE = 5;
int prizes[SIZE] = {1,2,3,4,5};
for (int i = 0; i < SIZE; i++){
    printf("&u\n", prices[i]);
}
```

### Alternate Approach

```C
char s[5] = {'a','b','c','d','e'};
for (int i = 0; s[i] != '\0'; i++){
    printf("%c\n",s[i]);
}
```

## Absolute Values

`abs` can be used in C too, just like python:

```C
int num = -2;
num = abs(num);
return num;
```

## Integers to Strings

```C
char *s;
asprintf(&s, "%d", number);
return s;
```
