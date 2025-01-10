words = ["mass","as","hero","superhero"]
a=[]
for i in range(len(words)):
        for j in range(len(words)):
            print(words[i])
            print(words[j])
            if words[i] in words[j] and i != j:
                  a.append(words[i])
print(a)
