N = int(input("Введите количество чисел: "))
numbers = []
for i in range(N):
    number = int(input("Введите число: "))
    numbers.append(number)
with open("file1_11.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")
even_numbers = []
with open("file1_11.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        if number % 2 == 0:
            even_numbers.append(number)
even_numbers.sort(reverse=True)
with open("file2_11.txt", "w") as file:
    for number in even_numbers:
        file.write(str(number) + "\n")





