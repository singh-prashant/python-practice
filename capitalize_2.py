import string
buffer_string = input().split(' ')
output_string =[]
for word in buffer_string:
    if word[0] in string.ascii_lowercase:
        word = word.title()
    output_string.append(word)
    
print(" ".join(output_string))
