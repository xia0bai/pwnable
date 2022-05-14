## collision

In `col.c`:
```c
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
    int* ip = (int*)p;  // 4 bytes
    int i;
    int res=0;
    for(i=0; i<5; i++){
            res += ip[i];
    }
    return res;
}

int main(int argc, char* argv[]){
    // ...
    if(strlen(argv[1]) != 20){  // Note: strlen will be truncated by "\x00"
        // ...
    }

    if(hashcode == check_password( argv[1] )){
        // ...
    }
}
```

Only need to make the sum of every 4 bytes of the input string the same as the hashcode. In particular, it should be noted that strlen will be truncated by `\x00`.