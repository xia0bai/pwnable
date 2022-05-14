## mistake

In `mistake.c`:
```c
#include <stdio.h>
#include <fcntl.h>

// ...

int main(int argc, char* argv[]){
    int fd;
    if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0){ // The "<" operator takes precedence over "="
        // ...
    }

    // ...
    if(!(len=read(fd,pw_buf,PW_LEN) > 0)){
        // ...
    }

    char pw_buf2[PW_LEN+1];
    printf("input password : ");
    scanf("%10s", pw_buf2);

    // ...
}
```

The `<` operator takes precedence over `=`, so fd is constant at `0`.You can enter anything as your password in `read`.Therefore, you only need to enter the XOR result of the password you entered in `scanf` to get the flag.