## bof

In `bof.c`:
```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(int key){
    char overflowme[32];
    gets(overflowme);   // gets may cause overflow
    if(key == 0xcafebabe){
        // ...
    }
    // ...
}
// ...
```

Overwrite the value of key with 0xcafebabe through `gets`.