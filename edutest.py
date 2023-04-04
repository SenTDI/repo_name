tests = {
    "lm2" : {}    
}
badwords = []
badwords2 = []
for line in open("123.txt", 'r', encoding="UTF-8"):
    splitline = line.split(" - ")
    try:
        tests["lm2"][splitline[0]] = splitline[1]
    except Exception:
         pass
for key, value in tests['lm2'].items():
        userinpt = str(input(f"{value.rstrip()}\nВведите слово на английском (0 выход) -> "))
        if userinpt == "0":
             break
        if userinpt.lower() == key.lower(): 
            print(f"{key.rstrip()} - {value.rstrip()} Все правильно!)\n")
        else:
            print(f"{key.rstrip()} - {value.rstrip()} Не правильно!:(\n")
            badwords.append([key, value])
for key, value in tests['lm2'].items():
        userinpt = input()
        if userinpt == "0":
             break
        print(f"{value.rstrip()} - \t\t\t\t\t{key.rstrip()}")

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
for list in badwords:
     f.write(f"{list[0]} - {list[1]}")