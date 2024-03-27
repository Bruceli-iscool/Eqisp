.text
.global _main

_main:
    mov x29, sp
    mov x0, #1
    str x0, [sp, #-8]!
    ldr x1, [sp]
    add x0, x1, x0
    ldr x1, [sp], #8
    mov x0, x1
    mov x8, 93
    svc #0

