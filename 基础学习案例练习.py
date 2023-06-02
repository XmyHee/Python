#如果您希望进行更深入的练习，以下是一些更具挑战性的 Python 练手代码示例：

#实现一个简单的计算器：
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("除数不能为零")

num1 = float(input("请输入第一个数字: "))
operator = input("请输入运算符 (+, -, *, /): ")
num2 = float(input("请输入第二个数字: "))

if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    result = "无效的运算符"

print("结果:", result)
#编写一个函数来查找列表中的最大值和最小值：
def find_min_max(numbers):
    if len(numbers) == 0:
        return None

    min_value = numbers[0]
    max_value = numbers[0]

    for num in numbers:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    return min_value, max_value

numbers = [5, 2, 9, 1, 7, 4]
min_num, max_num = find_min_max(numbers)
print("最小值:", min_num)
print("最大值:", max_num)
#实现一个简单的文本加密器和解密器：
def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + key)
    return encrypted_text

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        decrypted_text += chr(ord(char) - key)
    return decrypted_text

message = input("请输入要加密的文本: ")
encryption_key = int(input("请输入加密密钥: "))

encrypted_message = encrypt(message, encryption_key)
print("加密后的文本:", encrypted_message)

decryption_key = int(input("请输入解密密钥: "))
decrypted_message = decrypt(encrypted_message, decryption_key)
print("解密后的文本:", decrypted_message)

"""
#这些示例涉及更多的函数定义、条件逻辑和算法，可以让您更深入地探索 Python 编程。
#尝试运行这些代码，并根据需要进行修改和扩展，以适应您的练习需求！
"""