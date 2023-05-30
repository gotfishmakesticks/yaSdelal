a = input("Введите слово: ")
b = a.lower()
c = ""
for i in range(len(b)):
    c += b[len(b)-i-1]
if c == b:
    print(f"{a} - палиндром")
else:
    print(f"{a} - не палиндром")