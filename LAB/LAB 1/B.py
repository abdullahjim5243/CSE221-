T = int(input())
for j in range(T):
    inp_str = input()
    inp_str_list = inp_str.split()
    operator = inp_str_list[2]
    num1 = inp_str_list[1]
    num2 = inp_str_list[3]

    if operator == '+':
        result = int(num1) + int(num2)    
    if operator == '-':
        result = int(num1) - int(num2)
    if operator == '/':
        result = int(num1) / int(num2)
    if operator == '*':
        result = int(num1) * int(num2) 

    print(f'{result:.6f}')    