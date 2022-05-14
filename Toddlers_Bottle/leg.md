## leg

- PC Register: In the `ARM` state, it saves the current address plus 8 (or plus 12). In the `Thumb` state, it saves the current address plus 4.
- `bx` command: Switch the state according to the lowest bit. When it is 0, it means `ARM`, and when it is 1, it means `Thumb`.

In [leg.asm](http://pwnable.kr/bin/leg.asm): 
```asm
(gdb) disass main
    0x00008d68 <+44>:	bl	0x8cd4 <key1>
    0x00008d6c <+48>:	mov	r4, r0
    0x00008d70 <+52>:	bl	0x8cf0 <key2>
    0x00008d74 <+56>:	mov	r3, r0
    0x00008d7c <+64>:	bl	0x8d20 <key3>
    0x00008d80 <+68>:	mov	r3, r0

(gdb) disass key1
    0x00008cdc <+8>:	mov	r3, pc  // r3 = 0x08cdc + 8 = 0x08ce4
    0x00008ce0 <+12>:	mov	r0, r3

(gdb) disass key2
    0x00008cfc <+12>:	add	r6, pc, #1  // r6 = pc + 1 = 0x08d04 + 1 = 0x08d05
    0x00008d00 <+16>:	bx	r6  // lowest bit is 1 (5: 0101), change to Thumb state
    0x00008d04 <+20>:	mov	r3, pc  // r3 = pc = 0x08d04 + 4 = 0x08d08
    0x00008d06 <+22>:	adds    r3, #4  // r3 = 0x08d0c
    0x00008d10 <+32>:	mov r0, r3

(gdb) disass key3
    0x00008d28 <+8>:	mov	r3, lr  // lr = 0x08d80
    0x00008d2c <+12>:	mov	r0, r3
```

According to the above analysis, the following information can be obtained: 
- `key1()`: `0x08ce4`
- `key2()`: `0x08d0c`
- `key3()`: `0x08d80`

The result of the sum is `0x08ce4 + 0x08d0c + 0x08d80 = 0x1a770 = 108400`.