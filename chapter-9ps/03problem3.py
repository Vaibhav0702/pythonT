def generatetable(n):
    table = ''
    for i in range(1,10):
        table += f"{n}* {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)

    


for i in range(2,21):
    generatetable(i)