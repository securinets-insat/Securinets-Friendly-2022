#include <stdio.h>
#include <string.h>
#include <unistd.h>

char flag_enc[] = "\xee\x9f\x04\xad\x65\xd5\xab\xc5\x69\xa5\xab\x00\x2d\x89\x8c\x51\x97\xb9\x8a\xa3\xad\x84\xdf\x67\x65\x80\x53\xc3\xd4\x4d\xb5\xa7\x15\x8f\x4c\xac\xde\xd6}";

int main() {
	char input[0x40];
	memset(input, 0, 0x40);
	int len = read(0x0, input, 0x40);
	*(input + (len - 1)) = '\0';
	if ((len - 1) == 0x27) {
		for (int i = 0; i < 0x27; i++) {
			*(input + i) -= (*(input + (i + 1)) * (i + 1));
		}

		if (!memcmp(input, flag_enc, 0x27))
			puts("[+] That should be the flag!");
		else
			puts("[+] Unfortunately it's not the flag!");
	}
	return 0;
}
