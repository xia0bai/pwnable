## fd

- `fd`:
    - 0: stdin
    - 1: stdout
    - 2: stderr
    - 2<: etc.

In `fd.c`: 
```c
int main(int argc, char* argv[], char* envp[]){
    // ...
    int fd = atoi( argv[1] ) - 0x1234;
    int len = 0;
    len = read(fd, buf, 32);
    if(!strcmp("LETMEWIN\n", buf)){
        // ...
    }
    // ...
}
```

If we set the value of `fd` to `0`, we can enter anything we want to read.