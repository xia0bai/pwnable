## random

In `random.c`:
```c
#include <stdio.h>

int main(){
    unsigned int random;
    random = rand();    // The seed of random is fixed to 0!!

    unsigned int key=0;
    scanf("%d", &key);

    if( (key ^ random) == 0xdeadbeef ){
        printf("Good!\n");
        system("/bin/cat flag");
        return 0;
    }

    printf("Wrong, maybe you should try 2^32 cases.\n");
    return 0;
}
```