## passcode

Checksec: 
```
[*] '/home/passcode/passcode'
    Arch:     i386-32-little
    RELRO:    Partial RELRO     // GOT can be overwritten
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

In asm:
```
08048564 <login>:
    804857c:       8b 55 f0                mov    -0x10(%ebp),%edx
    804857f:       89 54 24 04             mov    %edx,0x4(%esp)
    8048583:       89 04 24                mov    %eax,(%esp)
    8048586:       e8 15 ff ff ff          call   80484a0 <__isoc99_scanf@plt>
    80485e3:       c7 04 24 af 87 04 08    movl   $0x80487af,(%esp)
    80485ea:       e8 71 fe ff ff          call   8048460 <system@plt>
 
08048609 <welcome>:
    804862f:       8d 55 90                lea    -0x70(%ebp),%edx
    8048632:       89 54 24 04             mov    %edx,0x4(%esp)
    8048636:       89 04 24                mov    %eax,(%esp)
    8048639:       e8 62 fe ff ff          call   80484a0 <__isoc99_scanf@plt>
 
08048665 <main>:
    804867a:       e8 8a ff ff ff          call   8048609 <welcome>
    804867f:       e8 e0 fe ff ff          call   8048564 <login>       // same ebp
```

- `name` in welcome: `-0x70(%ebp)`
- `name` max len = 100
- `passcode1` in login: `-0x10(%ebp)`