qntd_freq = int(input())
freq = {}

for c in range(qntd_freq):
    id = input()
    try: freq[id] += 1
    except:freq[id] = 1
print(len(freq))