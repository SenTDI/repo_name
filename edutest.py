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
words0 = False
ww0 = 0
ww1 = 0
ww2 = 0
for key, value in tests['lm2'].items():        
        if value[1] == 0: ww0 += 1
        elif value[1] == 1: ww1 += 1
        elif value[1] == 2: ww2 += 1
        else:
             pass
print(f"\nСлов с 0 написаний {ww0} Слов с 1 написаний {ww1} Слов с 2 написаний {ww2}\n")
for key, value in tests['lm2'].items():
        if not words0:
            userinpt = str(input(f"{value[0].rstrip()}\nВведите слово на английском (0 выход) -> "))
        else:
            userinpt = "404"
        if userinpt == "0":
            words0 = True
        elif userinpt.rstrip().lower() == key.rstrip().lower():
            print(f"{key.rstrip()} - {value[0].rstrip()} - {value[1]} Все правильно!)\n")
            value[1] += 1
            if value[1] < 3:
                badwords.append([key, value[0], value[1]])
        else:
            print(f"{key.rstrip()} - {value[0].rstrip()} - {value[1]} Не правильно!:(\n")
            if not words0:
                userinptcheck = str(input(f"Слово было написанно правильно Y если да если нет Enter -> "))
                if userinptcheck.rstrip().lower() == "y":
                    value[1] += 1
                    if value[1] < 3:
                        badwords.append([key, value[0], value[1]]) 
            if value[1] < 3:
                badwords.append([key, value[0], value[1]])

f = open("badwords.txt", 'w', encoding="UTF-8")
out = ""
for list in badwords:
    out += f"{list[0].rstrip()} - {list[1].rstrip()} - {list[2]}" + "\n"
f.write(out)
f.close

for key, value in tests['lm2'].items():
        userinpt = input("0 что-бы закончить -> ")
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

