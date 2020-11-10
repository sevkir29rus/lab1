import re
import csv
all_char = 0
spaces = 0
punct = 0
sentences = 0
words = 0


f= open("f1.csv", encoding="utf-8")
csv_reader = csv.reader(f)
for line in csv_reader:
            char = ",".join(line)
            all_char += len(char)
            spaces += char.count(" ")
            punct+= char.count(".") + char.count(",") + char.count("?") \
                    + char.count("(") + char.count(")") + char.count(";") \
                    + char.count("-") + char.count("_") + char.count(":") \
                    + char.count("/") + char.count("\'") + char.count("\"")
            words += len(re.findall(r"(\w+'\w+)|(\w+-\w+'\w+)|(\w+-\w+'\w)|\w+", char))
            sentences += len(re.findall(r"([A-Z][^\.!?]*[\.!?])", char))
print("Число символов", all_char)
print("Число символов без пробелов", all_char - spaces)
print("Количество символов без знаков препинания ", all_char - punct)
print("Количество слов ", words)
print("Количество предложений ", sentences)
f.close() 