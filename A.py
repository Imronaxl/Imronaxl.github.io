bits = list(input("Введите 7-битное сообщение (например, 1010100): "))
def hamming_decode():
    global bits
    r1, r2, r3 = int(bits[0]), int(bits[1]), int(bits[3])
    i1, i2, i3, i4 = int(bits[2]), int(bits[4]), int(bits[5]), int(bits[6])
    errors_bit = ['', 'r1', 'r2', 'i1', 'r3', 'i2', 'i3', 'i4']
    s1 = r1 ^ i1 ^ i2 ^ i4
    s2 = r2 ^ i1 ^ i3 ^ i4
    s3 = r3 ^ i2 ^ i3 ^ i4
    
    error_pos = s1 + (s2 << 1) + (s3 << 2)
    
    if error_pos != 0:
        print(f"Ошибка в бите {errors_bit[error_pos]}. Исправляем.")
        bits[error_pos - 1] = '1' if bits[error_pos - 1] == '0' else '0'
    
    else:
        print("Ошибок не найдено")
corrected_message = hamming_decode()
print(''.join(bits))
