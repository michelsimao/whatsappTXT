with open("teste.txt") as f:
    content = f.read()
    print(f"Exibe linha a linha: \n {content}")
f.close()

#-----

lines = []
with open("teste.txt") as g:
    lines = g.readlines()

count = 0

for line in lines:
    count += 1
    print(f"Linha {count}: {line}")

g.close()

#-------

with open("teste.txt") as h:
    for line in h:
        print(line.strip())

h.close()        