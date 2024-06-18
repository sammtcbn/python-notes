start_addr_str = "1FFC000"
new_hex_str = format(int(start_addr_str, 16) + 1, 'X')
print("original hex =", start_addr_str)
print("after increment =", new_hex_str)

# for each
for i in range(10):
    current_offset = format(int(start_addr_str, 16) + i, 'X')
    print(f"{current_offset}")
