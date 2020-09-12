# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

str = "A man, a plan, a canal: Panama"
filtered_str = []

str= str.lower()
for char in str:
    if char.isalnum():
        filtered_str.append(char)

print(filtered_str)

result = True




for i in range(int(len(filtered_str) / 2)) :
 if filtered_str.pop(0) != filtered_str.pop(len(filtered_str)-1) :
    result = False
print(result)
#print("Result : "+result)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
