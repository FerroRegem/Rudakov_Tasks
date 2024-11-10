numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
countNone = 0
sumNum = 0
for i in range(len(numbers)):
    if numbers[i] == None:
        countNone = i
        continue
    sumNum += numbers[i]
numbers[countNone] = sumNum/len(numbers)

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
