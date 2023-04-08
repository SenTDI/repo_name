tests = {
    "lm2" : {}    
}
badwords = []
badwords2 = []
for line in open("badwords.txt", 'r', encoding="UTF-8"):
    splitline = line.split(" - ")
    try:
        tests["lm2"][splitline[0]] = [splitline[1], int(splitline[2])]
    except IndexError:
        try:
            tests["lm2"][splitline[0]] = [splitline[1], 0]
        except IndexError:
            pass
for key, value in tests['lm2'].items():
        userinpt = str(input(f"{value[0].rstrip()}\nВведите слово на английском (0 выход) -> "))
        if userinpt == "0":
             break
        if userinpt.lower() == key.lower():
            print(f"{key.rstrip()} - {value[0].rstrip()} - {value[1]} Все правильно!)\n")
            if value[1] < 5:
                badwords.append([key, value[0], value[1] + 1])
        else:
            print(f"{key.rstrip()} - {value[0].rstrip()} - {value[1]} Не правильно!:(\n")
            badwords.append([key, value[0], value[1] - 1])
for key, value in tests['lm2'].items():
        userinpt = input()
        if userinpt == "0":
             break
        print(f"{value[0].rstrip()} - {value[1]} -\t\t\t\t\t{key.rstrip()}")

"""
while True:
    if len(badwords) >= 1:
        userinpt = str(input(f"Хотите повторить слова которые вы плохо знаете?\n\
Ведь их {len(badwords)} штук(и/a) :( 0 - нет да - любой(ые) символ(ы)"))    
        if userinpt == "0":
             break
        if userinpt.lower() == key.lower(): 
            print(f"{key} - {value} Все правильно!)")
        else:
            print(f"{key} - {value} Не правильно!:(")
            badwords2.append([key, value])
"""

f = open("badwords.txt", 'w', encoding="UTF-8")
out = ""
for list in badwords:
    out += f"{list[0].rstrip()} - {list[1].rstrip()} - {list[2]}" + "\n"
f.write(out)