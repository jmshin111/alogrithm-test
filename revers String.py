from pythonds.basic.stack import Stack

input_str = 'hello'

# str = ['h','e','l','l','o']
str_stack = Stack()
str_list = list(input_str)

print (input_str)

for i in range(0, len(str_list), 1):
    str_pop_zero = str_list.pop(0)
    print (str_pop_zero)
    str_stack.push(str_pop_zero)

output_str = list()
for i in range(0, str_stack.size(),1):
    output_str.append(str_stack.pop())

print(output_str)
