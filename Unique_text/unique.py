unique_set=set()
with open("text.txt","r") as file:
    for line in file:
        words=line.split()
        for word in words:
            unique_set.add(word)

    
print(unique_set)

with open("write.txt","w") as file:
    for word in unique_set:
        file.write(word+" "+"\n")
    # file.write("\n")

