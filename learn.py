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
        userinpt = input()
        if userinpt == "0":
             break
        print(f"{value[0].rstrip()} - {value[1]} -\t\t\t\t\t{key.rstrip()}")