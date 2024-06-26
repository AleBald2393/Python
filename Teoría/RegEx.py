Regular expressions (RegEx) are patterns used to match and manipulate strings of text. There are several special sequences in RegEx that can be used to match specific characters or patterns.

| Special Sequence | Meaning                 | 	Example             |
| -----------  | ----------------------- | ----------------------|
| \d|Matches any digit character (0-9)|"123" matches "\d\d\d"|
|\D|Matches any non-digit character|"hello" matches "\D\D\D\D\D"|
|\w|Matches any word character (a-z, A-Z, 0-9, and _)|"hello_world" matches "\w\w\w\w\w\w\w\w\w\w\w"|
|\W|Matches any non-word character|	"@#$%" matches "\W\W\W\W"|
|\s|Matches any whitespace character (space, tab, newline, etc.)|"hello world" matches "\w\w\w\w\w\s\w\w\w\w\w"|
|\S|Matches any non-whitespace character|"hello_world" matches "\S\S\S\S\S\S\S\S\S"|
|\b|Matches the boundary between a word character and a non-word character|"cat" matches "\bcat\b" in "The cat sat on the mat"|
|\B|Matches any position that is not a word boundary|"cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"|
#Ejemplo:
pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)

pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")

s2 = "Michael Jackson was a singer and known as the 'King of Pop'"


# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)

# Print out the list of matched words
print(result)

# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 

#PARA REEMPLAZAR
g.replace("Mary", "Bob")

segunda opción
new_str1 = re.sub(r"fox", "bear", str1)

print(new_str1)

#PARA VOLVER EN LISTA
g.split()

#PARA BUSCAR SI HAY DIGITOS EN UN STRING
s3 = "House number- 1105"
# Write your code below and press Shift+Enter to execute
result=re.search("\d",s3)
if result:
    print("digit found")
else:
    print ("digit not found.")

#GUARDAR EN UNA LISTA LAS OCURRENCIAS DE UN SUB STRING EN UN STRING)
result=re.findall("woo",str2)
result
