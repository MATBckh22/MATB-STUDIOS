# Structures, Unions and Bit Manipulation

## Concept of Structures

Structures are derived from different data types, **they're a collection of related variables under one name.**

- used to define records stored in files
- formation of complex data structures
    - linked lists
    - queues
    - stacks
    - trees

## Syntax

```C
struct structure_name{
data_type member1
data_type member2
}; //remember the semicolon!
```

Example:

```C
struct Person {
    char gender;
    unsigned int age;
    char name[50];
    int citNo;
    float salary;
};
```

## Self-Referential Structure

Structures cannot contain an instance of itself, **however pointers of the structure can be included:**

```C
struct employee2 {
    char firstName[20];
    char lastName[20];
    unsigned int age;
    char gender;
    float hourlySalary;
    struct employee2 person; // ERROR
    struct employee2 *ePtr; // pointer
};
```

Pointers to reference the address of `struct employee2` can be accepted.

## Definition  