input_str = '1123432121'



def find_longest_palindrom(s : str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right -1 ]:
            left +=1
            right +=1
        return s[left+1:right-1]

    if len(s) < 2 or s==s[::-1]:
        return s

    result = ''

    for i in range

print(find_longest_palindrom(input_str))
