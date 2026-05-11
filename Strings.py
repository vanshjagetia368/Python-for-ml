#================================================================================
# COMPREHENSIVE PYTHON STRINGS TUTORIAL - COMPLETE GUIDE
#================================================================================
# What are Strings?
# Strings are immutable sequences of characters enclosed in quotes. They are one 
# of the most fundamental data types in Python used to represent text data.
#
# KEY CHARACTERISTICS OF STRINGS:
# - IMMUTABLE: Cannot be changed after creation (creates new string when modified)
# - ORDERED: Characters maintain their position (index-based access)
# - INDEXABLE: Access individual characters using integer indices (0-based)
# - ITERABLE: Can loop through all characters
# - SUPPORTS OPERATIONS: Concatenation, repetition, slicing, comparison
# - SEQUENCE TYPE: Can be accessed like lists but cannot be modified in-place
# - UNICODE SUPPORT: Can contain any Unicode character
#================================================================================

print("=" * 80)  # OUTPUT: ================================================================================
print("1. CREATING AND INITIALIZING STRINGS")  # OUTPUT: 1. CREATING AND INITIALIZING STRINGS
print("=" * 80)  # OUTPUT: ================================================================================

# Method 1: Using double quotes
greeting = "Hello, World!"
print(f"Double quotes: {greeting}")  # OUTPUT: Double quotes: Hello, World!

# Method 2: Using single quotes
name = 'Alice'
print(f"Single quotes: {name}")  # OUTPUT: Single quotes: Alice

# Method 3: Using triple quotes for multi-line strings
multi_line = """This is a
multi-line
string."""
print(f"Multi-line string:\n{multi_line}")  # OUTPUT: Multi-line string:\nThis is a\nmulti-line\nstring.

# Method 4: Using triple single quotes
multi_line2 = '''Another
multi-line
example'''
print(f"Triple single quotes:\n{multi_line2}")  # OUTPUT: Triple single quotes:\nAnother\nmulti-line\nexample

# Method 5: Empty string
empty = ""
print(f"Empty string: '{empty}', Length: {len(empty)}")  # OUTPUT: Empty string: '', Length: 0

# Method 6: Using string constructor
s_from_list = str([1, 2, 3])
print(f"String from list: {s_from_list}")  # OUTPUT: String from list: [1, 2, 3]

# Method 7: Raw strings (ignoring escape sequences)
raw_string = r"C:\Users\name\file.txt"
print(f"Raw string: {raw_string}")  # OUTPUT: Raw string: C:\Users\name\file.txt

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("2. STRING INDEXING AND ACCESSING CHARACTERS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 2. STRING INDEXING AND ACCESSING CHARACTERS

text = "Python"
print(f"String: {text}")  # OUTPUT: String: Python

# Positive indexing
print(f"Index 0: {text[0]}")  # OUTPUT: Index 0: P
print(f"Index 2: {text[2]}")  # OUTPUT: Index 2: t
print(f"Index 5: {text[5]}")  # OUTPUT: Index 5: n

# Negative indexing
print(f"Index -1 (last): {text[-1]}")  # OUTPUT: Index -1 (last): n
print(f"Index -2: {text[-2]}")  # OUTPUT: Index -2: o
print(f"Index -6 (first): {text[-6]}")  # OUTPUT: Index -6 (first): P

# Length of string
print(f"Length: {len(text)}")  # OUTPUT: Length: 6

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("3. STRING SLICING")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 3. STRING SLICING

text = "Hello, World!"
print(f"Original: {text}")  # OUTPUT: Original: Hello, World!

# Basic slicing
print(f"text[0:5]: {text[0:5]}")  # OUTPUT: text[0:5]: Hello
print(f"text[7:12]: {text[7:12]}")  # OUTPUT: text[7:12]: World
print(f"text[:5]: {text[:5]}")  # OUTPUT: text[:5]: Hello
print(f"text[7:]: {text[7:]}")  # OUTPUT: text[7:]: World!

# Slicing with step
print(f"text[::2] (every 2nd char): {text[::2]}")  # OUTPUT: text[::2] (every 2nd char): Hlo ol!
print(f"text[1::2]: {text[1::2]}")  # OUTPUT: text[1::2]: el,Wrd

# Negative slicing
print(f"text[-6:-1]: {text[-6:-1]}")  # OUTPUT: text[-6:-1]: World
print(f"text[-13:]: {text[-13:]}")  # OUTPUT: text[-13:]: Hello, World!

# Reversing with negative step
print(f"text[::-1] (reversed): {text[::-1]}")  # OUTPUT: text[::-1] (reversed): !dlroW ,olleH
print(f"text[10:2:-1]: {text[10:2:-1]}")  # OUTPUT: text[10:2:-1]: roW ,

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("4. ESCAPE CHARACTERS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 4. ESCAPE CHARACTERS

# Newline
print("Hello\nWorld")  # OUTPUT: Hello\nWorld
print(f"Newline example: {'Hello\\nWorld'}")  # OUTPUT: Newline example: Hello\nWorld

# Tab
print("Name\tAge\tCity")  # OUTPUT: Name\tAge\tCity
print(f"Tab example: {'Name\\tAge\\tCity'}")  # OUTPUT: Tab example: Name\tAge\tCity

# Backslash
print("Path: C:\\Users\\Documents")  # OUTPUT: Path: C:\Users\Documents
print(f"Backslash example: {'C:\\\\Users\\\\Documents'}")  # OUTPUT: Backslash example: C:\\Users\\Documents

# Quotes
print('She said, "Hello!"')  # OUTPUT: She said, "Hello!"
print("It's a nice day!")  # OUTPUT: It's a nice day!

# Other escapes
print("Alert:\a")  # OUTPUT: Alert:(bell sound - not audible in text)
print(f"Carriage return example")  # OUTPUT: Carriage return example
print(f"Quote escape: {'He said \"Hi\"'}")  # OUTPUT: Quote escape: He said "Hi"

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("5. STRING OPERATORS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 5. STRING OPERATORS

s = "Hello"

# Concatenation
result = s + " " + "World"
print(f"Concatenation: {result}")  # OUTPUT: Concatenation: Hello World

# Repetition
print(f"s * 3: {s * 3}")  # OUTPUT: s * 3: HelloHelloHello
print(f"s * 0: {s * 0}")  # OUTPUT: s * 0: (empty string)

# Comparison operators
s1 = "Apple"
s2 = "Banana"
print(f"'{s1}' == '{s2}': {s1 == s2}")  # OUTPUT: 'Apple' == 'Banana': False
print(f"'{s1}' != '{s2}': {s1 != s2}")  # OUTPUT: 'Apple' != 'Banana': True
print(f"'{s1}' < '{s2}': {s1 < s2}")  # OUTPUT: 'Apple' < 'Banana': True
print(f"'{s1}' > '{s2}': {s1 > s2}")  # OUTPUT: 'Apple' > 'Banana': False

# Membership operators
text = "Python Programming"
print(f"'P' in text: {'P' in text}")  # OUTPUT: 'P' in text: True
print(f"'Java' in text: {'Java' in text}")  # OUTPUT: 'Java' in text: False
print(f"'Pro' in text: {'Pro' in text}")  # OUTPUT: 'Pro' in text: True

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("6. ASCII AND CHARACTER CODES")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 6. ASCII AND CHARACTER CODES

# ord() - Get ASCII value
print(f"ord('A'): {ord('A')}")  # OUTPUT: ord('A'): 65
print(f"ord('a'): {ord('a')}")  # OUTPUT: ord('a'): 97
print(f"ord('0'): {ord('0')}")  # OUTPUT: ord('0'): 48
print(f"ord(' '): {ord(' ')}")  # OUTPUT: ord(' '): 32

# chr() - Get character from ASCII value
print(f"chr(65): {chr(65)}")  # OUTPUT: chr(65): A
print(f"chr(97): {chr(97)}")  # OUTPUT: chr(97): a
print(f"chr(48): {chr(48)}")  # OUTPUT: chr(48): 0

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("7. STRING FORMATTING - OLD STYLE (% Operator)")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 7. STRING FORMATTING - OLD STYLE (% Operator)

# %s for strings
name = "Alice"
result = "Hello, %s!" % name
print(f"String: {result}")  # OUTPUT: String: Hello, Alice!

# %d for integers
age = 30
result = "Age: %d years" % age
print(f"Integer: {result}")  # OUTPUT: Integer: Age: 30 years

# %f for floats
price = 19.99
result = "Price: $%.2f" % price
print(f"Float: {result}")  # OUTPUT: Float: Price: $19.99

# Multiple values
result = "%s is %d years old and lives in %s" % ("Bob", 25, "NYC")
print(f"Multiple: {result}")  # OUTPUT: Multiple: Bob is 25 years old and lives in NYC

# Format specifiers
print(f"Hex (%%x): {0xFF:x}")  # OUTPUT: Hex (%x): ff
print(f"Octal (%%o): {8:o}")  # OUTPUT: Octal (%o): 10
print(f"Binary (%%b): {5:b}")  # OUTPUT: Binary (%b): 101

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("8. STRING FORMATTING - .format() METHOD")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 8. STRING FORMATTING - .format() METHOD

# Positional arguments
result = "Hello {}, you are {} years old".format("Alice", 30)
print(f"Positional: {result}")  # OUTPUT: Positional: Hello Alice, you are 30 years old

# Named arguments
result = "Hello {name}, age {age}".format(name="Bob", age=25)
print(f"Named: {result}")  # OUTPUT: Named: Hello Bob, age 25

# Format specifiers
result = "Float: {:.2f}".format(3.14159)
print(f"2 decimals: {result}")  # OUTPUT: 2 decimals: Float: 3.14

result = "Padding: |{:10}|".format("Hi")
print(f"Padding: {result}")  # OUTPUT: Padding: |        Hi|

result = "Alignment: |{:<10}|{:^10}|{:>10}|".format("left", "center", "right")
print(f"Alignment: {result}")  # OUTPUT: Alignment: |left      |  center  |     right|

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("9. STRING FORMATTING - F-STRINGS (Python 3.6+)")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 9. STRING FORMATTING - F-STRINGS (Python 3.6+)

name = "Charlie"
age = 35
city = "Boston"

# Simple f-string
result = f"I'm {name}, {age} years old from {city}"
print(f"Simple: {result}")  # OUTPUT: Simple: I'm Charlie, 35 years old from Boston

# Expressions in f-strings
x = 10
y = 5
result = f"Sum: {x + y}, Product: {x * y}"
print(f"Expressions: {result}")  # OUTPUT: Expressions: Sum: 15, Product: 50

# Formatting in f-strings
pi = 3.14159
result = f"Pi rounded: {pi:.2f}"
print(f"Formatted: {result}")  # OUTPUT: Formatted: Pi rounded: 3.14

# Uppercase
result = f"Uppercase: {name.upper()}"
print(f"Method call: {result}")  # OUTPUT: Method call: Uppercase: CHARLIE

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("10. CASE CONVERSION METHODS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 10. CASE CONVERSION METHODS

text = "Hello World"
print(f"Original: {text}")  # OUTPUT: Original: Hello World

# upper()
result = text.upper()
print(f"upper(): {result}")  # OUTPUT: upper(): HELLO WORLD

# lower()
result = text.lower()
print(f"lower(): {result}")  # OUTPUT: lower(): hello world

# capitalize()
result = text.capitalize()
print(f"capitalize(): {result}")  # OUTPUT: capitalize(): Hello world

# title()
result = text.title()
print(f"title(): {result}")  # OUTPUT: title(): Hello World

# swapcase()
result = text.swapcase()
print(f"swapcase(): {result}")  # OUTPUT: swapcase(): hELLO wORLD

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("11. STRING STRIPPING AND ALIGNMENT METHODS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 11. STRING STRIPPING AND ALIGNMENT METHODS

text = "  Hello World  "
print(f"Original: '{text}'")  # OUTPUT: Original: '  Hello World  '

# strip() - Remove both sides
result = text.strip()
print(f"strip(): '{result}'")  # OUTPUT: strip(): 'Hello World'

# lstrip() - Remove left side
result = text.lstrip()
print(f"lstrip(): '{result}'")  # OUTPUT: lstrip(): 'Hello World  '

# rstrip() - Remove right side
result = text.rstrip()
print(f"rstrip(): '{result}'")  # OUTPUT: rstrip(): '  Hello World'

# Custom characters to strip
text2 = "xxxHelloxxxWORLD xxx"
result = text2.strip('x ')
print(f"strip('x '): '{result}'")  # OUTPUT: strip('x '): 'HelloxxxWORLD'

# center()
result = "Hi".center(10)
print(f"center(10): '{result}'")  # OUTPUT: center(10): '    Hi    '

# ljust() - Left justify
result = "Hi".ljust(10)
print(f"ljust(10): '{result}'")  # OUTPUT: ljust(10): 'Hi        '

# rjust() - Right justify
result = "Hi".rjust(10)
print(f"rjust(10): '{result}'")  # OUTPUT: rjust(10): '        Hi'

# zfill() - Fill with zeros
result = "42".zfill(5)
print(f"zfill(5): '{result}'")  # OUTPUT: zfill(5): '00042'

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("12. SEARCHING AND FINDING METHODS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 12. SEARCHING AND FINDING METHODS

text = "Hello, Hello, World! Hello"
print(f"Text: {text}")  # OUTPUT: Text: Hello, Hello, World! Hello

# find() - First occurrence, returns -1 if not found
index = text.find("Hello")
print(f"find('Hello'): {index}")  # OUTPUT: find('Hello'): 0

index = text.find("Python")
print(f"find('Python'): {index}")  # OUTPUT: find('Python'): -1

# rfind() - Last occurrence
index = text.rfind("Hello")
print(f"rfind('Hello'): {index}")  # OUTPUT: rfind('Hello'): 20

# index() - Like find but raises error if not found
try:
    index = text.index("World")
    print(f"index('World'): {index}")  # OUTPUT: index('World'): 14
except ValueError:
    print("Not found!")

# count() - Count occurrences
count = text.count("Hello")
print(f"count('Hello'): {count}")  # OUTPUT: count('Hello'): 3

count = text.count("o")
print(f"count('o'): {count}")  # OUTPUT: count('o'): 4

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("13. REPLACEMENT AND SPLITTING METHODS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 13. REPLACEMENT AND SPLITTING METHODS

text = "Hello World Python World"
print(f"Original: {text}")  # OUTPUT: Original: Hello World Python World

# replace() - Replace occurrences
result = text.replace("World", "Universe")
print(f"replace('World', 'Universe'): {result}")  # OUTPUT: replace('World', 'Universe'): Hello Universe Python Universe

# replace() with limit
result = text.replace("World", "Universe", 1)
print(f"replace with limit 1: {result}")  # OUTPUT: replace with limit 1: Hello Universe Python World

# split() - Split into list
words = text.split()
print(f"split(): {words}")  # OUTPUT: split(): ['Hello', 'World', 'Python', 'World']

# split() with separator
csv = "apple,banana,cherry,date"
items = csv.split(",")
print(f"split(','):  {items}")  # OUTPUT: split(','):  ['apple', 'banana', 'cherry', 'date']

# splitlines() - Split by line breaks
multiline = "Line 1\nLine 2\nLine 3"
lines = multiline.splitlines()
print(f"splitlines(): {lines}")  # OUTPUT: splitlines(): ['Line 1', 'Line 2', 'Line 3']

# join() - Combine list into string
words = ["Hello", "World", "Python"]
result = " ".join(words)
print(f"' '.join(): {result}")  # OUTPUT: ' '.join(): Hello World Python

result = "-".join(words)
print(f"'-'.join(): {result}")  # OUTPUT: '-'.join(): Hello-World-Python

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("14. PREFIX AND SUFFIX METHODS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 14. PREFIX AND SUFFIX METHODS

text = "Hello.txt"
print(f"Text: {text}")  # OUTPUT: Text: Hello.txt

# startswith()
result = text.startswith("Hello")
print(f"startswith('Hello'): {result}")  # OUTPUT: startswith('Hello'): True

result = text.startswith("Hi")
print(f"startswith('Hi'): {result}")  # OUTPUT: startswith('Hi'): False

# endswith()
result = text.endswith(".txt")
print(f"endswith('.txt'): {result}")  # OUTPUT: endswith('.txt'): True

result = text.endswith(".py")
print(f"endswith('.py'): {result}")  # OUTPUT: endswith('.py'): False

# removeprefix() - Python 3.9+
result = text.removeprefix("Hello")
print(f"removeprefix('Hello'): {result}")  # OUTPUT: removeprefix('Hello'): .txt

# removesuffix() - Python 3.9+
result = text.removesuffix(".txt")
print(f"removesuffix('.txt'): {result}")  # OUTPUT: removesuffix('.txt'): Hello

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("15. CHARACTER TYPE CHECKING METHODS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 15. CHARACTER TYPE CHECKING METHODS

# isalpha() - All alphabetic
print(f"'Hello'.isalpha(): {'Hello'.isalpha()}")  # OUTPUT: 'Hello'.isalpha(): True
print(f"'Hello123'.isalpha(): {'Hello123'.isalpha()}")  # OUTPUT: 'Hello123'.isalpha(): False

# isdigit() - All digits
print(f"'12345'.isdigit(): {'12345'.isdigit()}")  # OUTPUT: '12345'.isdigit(): True
print(f"'123A5'.isdigit(): {'123A5'.isdigit()}")  # OUTPUT: '123A5'.isdigit(): False

# isalnum() - All alphanumeric
print(f"'Hello123'.isalnum(): {'Hello123'.isalnum()}")  # OUTPUT: 'Hello123'.isalnum(): True
print(f"'Hello 123'.isalnum(): {'Hello 123'.isalnum()}")  # OUTPUT: 'Hello 123'.isalnum(): False

# isspace() - All whitespace
print(f"'   '.isspace(): {'   '.isspace()}")  # OUTPUT: '   '.isspace(): True
print(f"' A '.isspace(): {' A '.isspace()}")  # OUTPUT: ' A '.isspace(): False

# islower() - All lowercase
print(f"'hello'.islower(): {'hello'.islower()}")  # OUTPUT: 'hello'.islower(): True
print(f"'Hello'.islower(): {'Hello'.islower()}")  # OUTPUT: 'Hello'.islower(): False

# isupper() - All uppercase
print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")  # OUTPUT: 'HELLO'.isupper(): True
print(f"'Hello'.isupper(): {'Hello'.isupper()}")  # OUTPUT: 'Hello'.isupper(): False

# istitle() - Title case
print(f"'Hello World'.istitle(): {'Hello World'.istitle()}")  # OUTPUT: 'Hello World'.istitle(): True
print(f"'hello world'.istitle(): {'hello world'.istitle()}")  # OUTPUT: 'hello world'.istitle(): False

# isidentifier() - Valid Python identifier
print(f"'my_var'.isidentifier(): {'my_var'.isidentifier()}")  # OUTPUT: 'my_var'.isidentifier(): True
print(f"'123var'.isidentifier(): {'123var'.isidentifier()}")  # OUTPUT: '123var'.isidentifier(): False

# isdecimal() - Decimal digits
print(f"'12345'.isdecimal(): {'12345'.isdecimal()}")  # OUTPUT: '12345'.isdecimal(): True

# isnumeric() - Numeric characters
print(f"'12345'.isnumeric(): {'12345'.isnumeric()}")  # OUTPUT: '12345'.isnumeric(): True

# isprintable() - All printable
print(f"'Hello'.isprintable(): {'Hello'.isprintable()}")  # OUTPUT: 'Hello'.isprintable(): True

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("16. PARTITION METHODS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 16. PARTITION METHODS

text = "filename.tar.gz"
print(f"Text: {text}")  # OUTPUT: Text: filename.tar.gz

# partition() - Split into 3 parts
result = text.partition(".")
print(f"partition('.'): {result}")  # OUTPUT: partition('.'): ('filename', '.', 'tar.gz')

# rpartition() - From right
result = text.rpartition(".")
print(f"rpartition('.'): {result}")  # OUTPUT: rpartition('.'): ('filename.tar', '.', 'gz')

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("17. EXPANSION AND ENCODING METHODS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 17. EXPANSION AND ENCODING METHODS

# expandtabs()
text = "Name\tAge\tCity"
result = text.expandtabs(10)
print(f"expandtabs(10): '{result}'")  # OUTPUT: expandtabs(10): 'Name      Age       City'

# encode() - String to bytes
text = "Hello"
encoded = text.encode()
print(f"encode(): {encoded}")  # OUTPUT: encode(): b'Hello'

# UTF-8 encoding
encoded_utf8 = "Hello 世界".encode('utf-8')
print(f"encode('utf-8'): {encoded_utf8}")  # OUTPUT: encode('utf-8'): b'Hello \\xe4\\xb8\\x96\\xe7\\x95\\x8c'

# Latin-1 encoding
encoded_latin = "Hello".encode('latin-1')
print(f"encode('latin-1'): {encoded_latin}")  # OUTPUT: encode('latin-1'): b'Hello'

# Reverse - decode bytes to string
decoded = encoded.decode()
print(f"decode(): {decoded}")  # OUTPUT: decode(): Hello

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("18. ADVANCED STRING OPERATIONS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 18. ADVANCED STRING OPERATIONS

# maketrans() and translate()
from_chars = "aeiou"
to_chars = "12345"
translation_table = str.maketrans(from_chars, to_chars)
text = "hello world"
result = text.translate(translation_table)
print(f"translate: {result}")  # OUTPUT: translate: h2ll4 w4rld

# format_map()
person = {'name': 'Alice', 'age': 30}
result = "Hello {name}, you are {age} years old".format_map(person)
print(f"format_map: {result}")  # OUTPUT: format_map: Hello Alice, you are 30 years old

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("19. STRING VALIDATION EXAMPLES")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 19. STRING VALIDATION EXAMPLES

# Validate email
email = "user@example.com"
is_valid_email = "@" in email and "." in email.split("@")[1]
print(f"Valid email format: {is_valid_email}")  # OUTPUT: Valid email format: True

# Validate phone
phone = "555-123-4567"
digits_only = phone.replace("-", "")
is_valid_phone = len(digits_only) == 10 and digits_only.isdigit()
print(f"Valid phone format: {is_valid_phone}")  # OUTPUT: Valid phone format: True

# Check password strength
password = "SecurePass123!"
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(not c.isalnum() for c in password)
is_strong = len(password) >= 12 and has_upper and has_lower and has_digit and has_special
print(f"Strong password: {is_strong}")  # OUTPUT: Strong password: True

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("20. STRING MANIPULATION EXAMPLES")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 20. STRING MANIPULATION EXAMPLES

# Reverse a string
text = "Python"
reversed_text = text[::-1]
print(f"Reversed: {reversed_text}")  # OUTPUT: Reversed: nohtyP

# Count vowels and consonants
text = "hello"
vowels = sum(1 for c in text if c.lower() in "aeiou")
consonants = sum(1 for c in text if c.isalpha() and c.lower() not in "aeiou")
print(f"Vowels: {vowels}, Consonants: {consonants}")  # OUTPUT: Vowels: 2, Consonants: 3

# Remove duplicate characters
text = "mississippi"
unique = "".join(dict.fromkeys(text))
print(f"Unique characters: {unique}")  # OUTPUT: Unique characters: misp

# Palindrome check
text = "racecar"
is_palindrome = text == text[::-1]
print(f"Is palindrome: {is_palindrome}")  # OUTPUT: Is palindrome: True

# Word frequency
text = "hello world hello python hello"
words = text.split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
print(f"Word frequency: {word_freq}")  # OUTPUT: Word frequency: {'hello': 3, 'world': 1, 'python': 1}

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("21. STRING METHODS REFERENCE (COMPLETE SUMMARY)")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 21. STRING METHODS REFERENCE (COMPLETE SUMMARY)
print("""
METHOD                     | DESCRIPTION                              | EXAMPLE
---------------------------|------------------------------------------|----------
upper()                    | Convert to uppercase                     | 'hello'.upper() → 'HELLO'
lower()                    | Convert to lowercase                     | 'HELLO'.lower() → 'hello'
capitalize()               | Capitalize first character               | 'hello'.capitalize() → 'Hello'
title()                    | Capitalize first letter of each word     | 'hello world'.title() → 'Hello World'
swapcase()                 | Swap case of all characters              | 'Hello'.swapcase() → 'hELLO'
strip()                    | Remove leading/trailing whitespace       | '  hi  '.strip() → 'hi'
lstrip()                   | Remove leading whitespace                | '  hi  '.lstrip() → 'hi  '
rstrip()                   | Remove trailing whitespace               | '  hi  '.rstrip() → '  hi'
replace(old, new)          | Replace substring                        | 'hi hi'.replace('hi', 'bye') → 'bye bye'
split(sep)                 | Split into list                          | 'a,b,c'.split(',') → ['a', 'b', 'c']
join(list)                 | Join list into string                    | ','.join(['a','b']) → 'a,b'
find(sub)                  | Find first occurrence                    | 'hello'.find('l') → 2
rfind(sub)                 | Find last occurrence                     | 'hello'.rfind('l') → 3
count(sub)                 | Count occurrences                        | 'hello'.count('l') → 2
startswith(prefix)         | Check if starts with                     | 'hello'.startswith('he') → True
endswith(suffix)           | Check if ends with                       | 'hello'.endswith('lo') → True
isalpha()                  | All alphabetic characters                | 'hello'.isalpha() → True
isdigit()                  | All digits                               | '123'.isdigit() → True
isalnum()                  | All alphanumeric                         | 'abc123'.isalnum() → True
isspace()                  | All whitespace                           | '   '.isspace() → True
islower()                  | All lowercase                            | 'hello'.islower() → True
isupper()                  | All uppercase                            | 'HELLO'.isupper() → True
istitle()                  | Title case                               | 'Hello World'.istitle() → True
center(width)              | Center in width                          | 'hi'.center(5) → '  hi  '
ljust(width)               | Left justify                             | 'hi'.ljust(5) → 'hi   '
rjust(width)               | Right justify                            | 'hi'.rjust(5) → '   hi'
zfill(width)               | Pad with zeros                           | '5'.zfill(3) → '005'
format()                   | Format string                            | '{} {}'.format('hello', 'world')
encode()                   | Encode to bytes                          | 'hello'.encode() → b'hello'
decode()                   | Decode from bytes                        | b'hello'.decode() → 'hello'
""")

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("22. SUMMARY AND KEY TAKEAWAYS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 22. SUMMARY AND KEY TAKEAWAYS
print("""
✓ Strings are immutable sequences of characters in Python
✓ Can be created with single, double, or triple quotes
✓ Support indexing, slicing, and various operations
✓ Multiple formatting methods: %, .format(), f-strings
✓ Rich set of methods for manipulation and validation
✓ Unicode support for international characters
✓ Escape sequences for special characters
✓ Can be efficiently searched, replaced, and transformed
✓ Membership testing with 'in' operator
✓ Strings are iterable and can be looped through
""")

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("END OF COMPREHENSIVE STRINGS TUTORIAL")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: ================================================================================