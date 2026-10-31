def genereator_lines():
    with open("text.txt","r") as file:
        for line in file:
            yield line

new_line=genereator_lines()
for line in genereator_lines():
    print(line)
    break

for line in genereator_lines():
    print(line)
    break

for line in genereator_lines():
    print(line)
    break