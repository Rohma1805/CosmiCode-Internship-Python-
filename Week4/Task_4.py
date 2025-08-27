#Task 4:
#Input string
text = input("Enter a string: ")
#Create an empty dictionary
freq = {}
#Count frequency 
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
#result
print("Character frequencies:")
for key, value in freq.items():
    print(f"{key}: {value}")