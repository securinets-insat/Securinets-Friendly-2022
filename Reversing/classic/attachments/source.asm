section .text
	global _start

_start:
	mov rdi, 0x1
	mov rsi, _key
	mov rdx, _key_len
	mov rax, 0x1
	syscall 
	xor rdi, rdi
	mov rsi, flag
	mov rdx, 0x20
	xor rax, rax
	syscall 
	cmp rax, 0x20
	jne _exit

layer1:
	mov r9, 0x656e697275636553
	cmp QWORD  [flag], r9
	jne _exit
	mov r9d, DWORD [flag + 0x8]
	and r9d, 0xffffff
	cmp r9d, 0x7b7374
	jne _exit

layer2:
	mov r10, QWORD [flag + 0xb]
	mov r15, 0x3384bd2e2d365625
	xor r10, r15
	mov r9, 0x5fcb8d4d7261664d
	cmp r10, r9
	jne _exit

prep_for_layer3:
	sub rsp, 0x8
	xor r8, r8
	mov rcx, 0x8

layer3:
	mov r9b, BYTE [flag + 0x13 + rcx - 0x1]
	mov al, 0x7
	mul r9b
	mov BYTE  [rsp + r8], al
	inc r8
	loop layer3
	pop r10
	mov r15, 0x4bca32d71a689622
	xor r10, r15
	mov r9, 0xd29d174ebd2d8dbb
	cmp r10, r9
	jne _exit

prep_for_layer4:
	sub rsp, 0x8
	mov rcx, 0x5

layer4:
	mov r9b, BYTE [flag + 0x1b + rcx - 0x1]
	mov BYTE  [rsp + rcx - 0x1], r9b
	loop layer4
	mov r14b, BYTE [rsp + 0x4]
	sub r14b, 0x3e
	cmp BYTE  [rsp + 0x3], r14b
	jne _exit
	mov r14b, BYTE [rsp + 0x3]
	add r14b, 0x39
	cmp BYTE [rsp], r14b
	jne _exit
	mov r14b, BYTE [rsp]
	sub r14b, 0x42
	cmp BYTE  [rsp + 0x1], r14b
	jne _exit
	mov r14b, BYTE [rsp + 0x1]
	sub r14b, 0x2
	cmp BYTE  [rsp + 0x2], r14b
	jne _exit
	mov rdi, 0x1
	mov rsi, _correct
	mov rdx, _correct_len
	mov rax, 0x1
	syscall 

_exit:
	mov rax, 0x3c
	xor rdi, rdi
	syscall

section .rodata
	_key db 'Key: '
	_key_len equ $-_key
	_correct db 'Correct!', 0xa
	_correct_len equ $-_correct

section .bss
	flag resb 0x20
