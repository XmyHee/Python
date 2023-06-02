#查找列表中的重复元素

def find_duplicates(numbers):
    duplicates = []
    for num in numbers:
        if numbers.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    return duplicates

numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]
duplicate_nums = find_duplicates(numbers)
print("重复的元素:", duplicate_nums) #重复的元素: [1, 2, 3]


#将字符串中的单词反转

def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

sentence = "Hello, World! I am learning Python."
reversed_sentence = reverse_words(sentence)
print("反转后的句子:", reversed_sentence) #反转后的句子: Python. learning am I World! Hello,



#斐波那契数列生成器

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

num_terms = int(input("请输入斐波那契数列的项数: "))
fib_sequence = fibonacci(num_terms)
print("斐波那契数列:", fib_sequence) #请输入斐波那契数列的项数: 4  斐波那契数列: [0, 1, 1, 2]

#统计字符串中各个字符出现的次数

def count_characters(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

text = "Hello, World!"
character_count = count_characters(text)
print("字符出现次数:", character_count) #字符出现次数: {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1}

"""
这些示例涵盖了不同的编程概念，如列表操作、字符串处理、算法等。您可以根据需要选择并尝试运行这些代码，
并根据自己的兴趣和需求进行修改和扩展。希望这些示例能够激发您的创造力并提升您的编程技能！
如果您有任何问题或需要更多的示例，请随时告诉我。
"""
