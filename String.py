words = []
worthy = []

for i in range(10):
    #This is where we input the words!
    word = input("Enter Word: ")
    words.append(word)
        
#This is where the words are determined for their length
lengthinput = int(input("Enter a length/Number: "))
for words in words:
    if (len(words)) >= lengthinput:
        worthy.append(words)
    else:
        continue

print(worthy)
