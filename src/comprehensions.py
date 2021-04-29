l = [i for i in range(10) if i % 2]
print(l)

d = {k:v for k,v in enumerate(l)}
print(d)

d = {v:k for k,v in enumerate(l)}
print(d)
