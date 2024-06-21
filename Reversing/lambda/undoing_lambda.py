def decode_flag(encoded):
  parts = encoded.split('_')
  return ''.join(chr(int(c, 36) + 10) for c in parts)

decode_output = decode_flag("16_10_13_x_6t_4_1o_9_1j_7_9_1j_1o_3_6_c_1o_6r")
print(decode_output)

def xor_characters(s, xor_value):
  return ''.join(chr(xor_value ^ ord(c)) for c in s)

xor_output = xor_characters(decode_output, 123)
print(xor_output)

def shift_characters(s, shift):
  return ''.join(chr(ord(c) + shift) for c in s)

shift_output1 = shift_characters(xor_output, 3)
print(shift_output1)

shift_output2 = shift_characters(shift_output1, -12)
print(shift_output2)
