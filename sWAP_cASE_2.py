import string
from io import StringIO
input_string = input()
empty = StringIO()
for alpha in input_string:
    if alpha in string.ascii_lowercase:
        empty.write(string.ascii_uppercase[string.ascii_lowercase.index(alpha)])
    elif alpha in string.ascii_uppercase:
        empty.write(string.ascii_lowercase[string.ascii_uppercase.index(alpha)])
    else:
        empty.write(alpha)
print(empty.getvalue())
        
