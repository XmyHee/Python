#当提到 Python 基础练手代码，以下是一些简单的示例，涵盖了常见的编程概念和技巧：

#计算两个数的和：
a = 5
b = 3
sum = a + b
print("和为:", sum)

#判断一个数是否为素数：
num = 17
is_prime = True

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "是一个素数")
else:
    print(num, "不是一个素数")

#反转字符串：
string = "Hello, World!"
reversed_string = string[::-1]
print("反转后的字符串:", reversed_string)

#统计列表中元素的个数：
numbers = [2, 4, 6, 8, 10, 2, 6, 2]
count = 0

for num in numbers:
    if num == 2:
        count += 1

print("2 在列表中出现的次数:", count)

#打印九九乘法表：
for i in range(1, 10):
    for j in range(1, i+1):
        print(i, "*", j, "=", i*j, end="\t")
    print()
"""
这些是一些简单的练手代码示例，涵盖了数学运算、条件判断、循环、字符串操作和列表操作等基本编程概念。
您可以尝试运行这些代码，并进行修改和扩展，以进一步巩固您的编程能力。 
"""