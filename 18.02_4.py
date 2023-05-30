list = input("Введите текст: ").split(sep = " ")

tempwords = {"" : 0}
words = {"" : 0}
longest = ""
frequent = ""
frequency = 0

for i in range(len(list)):
    if len(list[i]) > len(longest):
        longest = list[i]
    for dictword in tempwords:
        if dictword == list[i]:
            words.update({list[i]: words[dictword] + 1})
        else:
            words.update({list[i]: 1})
        print(words)
        print(str(tempwords) + "!")
    tempwords = words

for word in words:
    if words[word] > frequency:
        frequent = word
        frequency = words[word]

print(f"Ответ:\nСамое часто встречающееся слово: {frequent} ({frequency} раз)\nСамое длинное слово: {longest} ({len(longest)} символов)")