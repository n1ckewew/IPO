input=input("Введите последовательность символов: ")
result=set()
vowels="aeiouAEIOU"
digit_5 = "5"
for char in input:
    if char in vowels or char == digit_5:
        result.add(char)
print("Множество элементов:", result)
