import sys

sys.setrecursionlimit(10000000)

def main():
    flag = input('Enter the flag: ')
    processed_flag = process_input(flag)
    correct_flag = decode_flag('16_10_13_x_6t_4_1o_9_1j_7_9_1j_1o_3_6_c_1o_6r')
    
    if processed_flag == correct_flag:
        print('Correct FLAG!')
    else:
        print('Incorrect')

def process_input(flag):
    step1 = shift_characters(flag, 12)
    step2 = shift_characters(step1, -3)
    step3 = xor_characters(step2, 123)
    return step3

def shift_characters(s, shift):
    return ''.join(chr(ord(c) + shift) for c in s)

def xor_characters(s, xor_value):
    return ''.join(chr(xor_value ^ ord(c)) for c in s)

def decode_flag(encoded):
    parts = encoded.split('_')
    return ''.join(chr(int(c, 36) + 10) for c in parts)

if __name__ == "__main__":
    main()
