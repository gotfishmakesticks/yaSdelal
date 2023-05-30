import os
for i in range(1, 5000):
    with open(f'tryhere_{i}.txt', 'rb') as f:
        s = f.read()
        if s[:len(s)-2] == 'seti{t00mu4d0cument0s':
            os.remove(f'tryhere_{i}.txt')