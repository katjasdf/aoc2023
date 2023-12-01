lines = open("day_1_data.txt", "r").readlines()
numbers = []
response = 0

for line in lines:
    line_numbers = []
    letters = list(line)
    for letter in letters:
        if letter.isnumeric():
            line_numbers.append(letter)

    two_numbers = line_numbers[0] + line_numbers[-1]
    numbers.append(two_numbers)

for number in numbers:
    response += int(number)

print(response)