from base64 import b64decode
part1="5345435552494e4554537b6845785f416e445f6234354536345f49355f34"
part2="X2dhVEVfN0hlX3c0eV9UMF8zdjNyeTdISW5nfQ=="
print(bytes.fromhex(part1)+b64decode(part2))