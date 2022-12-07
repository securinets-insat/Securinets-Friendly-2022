import string

allowed = string.ascii_lowercase + '('+')'

inp = input(">>> ")
check = all([n in allowed for n in inp])
exec(inp) if check else print("Nah")
