from typing import List
data = [0b10000000,0b10000000,0b10000000,0b10000000,0b10000000,0b10000000,0b10000000,0b10000000,0b10000000,0b10000000]

data = [235, 140, 4]

data = [197, 130, 1]

data = [0b11000111,0b10000111,0b11100111,0b00010111,0b10010111,0b11110111,0b10010111,0b10010111,0b10010111,0b000010111]

data = [248,130,130,130]

class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        mask_one_byte   = 0b10000000
        mask_two_byte   = 0b11000000
        mask_three_byte = 0b11100000
        mask_four_byte  = 0b11110000

        mask_five_byte  = 0b11111000
        mask_six_byte   = 0b11111100
        mask_seven_byte = 0b11111110
        mask_eight_byte = 0b11111111


        sub_mask_byte   = 0b10000000
        current_idx = 0

        for i in data:
            print(bin(i))
        while True:
            if current_idx > len(data) - 1:
                break
            next_val = data[current_idx]
            rest_count = 0

            if (next_val & mask_five_byte) == mask_five_byte or \
                    (next_val & mask_six_byte) == mask_six_byte or \
                    (next_val & mask_seven_byte) == mask_seven_byte or  \
                    (next_val & mask_eight_byte) == mask_eight_byte :
                    return False


            if next_val & mask_four_byte == mask_four_byte:
                rest_count = 3

            elif next_val & mask_three_byte == mask_three_byte:
                rest_count = 2

            elif next_val & mask_two_byte == mask_two_byte:
                rest_count = 1

            elif next_val & mask_one_byte == 0:
                current_idx += 1
                continue
            else:
                return False

            if current_idx+rest_count > len(data)-1:
                return False

            for i in range(1,rest_count+1):
                if current_idx > len(data) - 1:
                    break
                current_idx += 1

                if data[current_idx] & sub_mask_byte != sub_mask_byte:
                    return False

            current_idx +=1
        return True


print(Solution.validUtf8(Solution,data))