def check_bit_zero(number):
    return bin(number)[-1] == '1'

test_number = 9 
result = check_bit_zero(test_number)
print(f"For the number {test_number}, is bit 0 in its binary representation '1'? {result}")
print("binary_representation =", bin(test_number))

test_number = 10
result = check_bit_zero(test_number)
print(f"For the number {test_number}, is bit 0 in its binary representation '1'? {result}")
print("binary_representation =", bin(test_number))

test_number = 29
result = check_bit_zero(test_number)
print(f"For the number {test_number}, is bit 0 in its binary representation '1'? {result}")
print("binary_representation =", bin(test_number))
