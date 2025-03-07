string  = "lets check the length of this string"
print(len(string))

# Form feed

print("Hello \f World")

# Octal Value \000

txt = "\110\145\154\154\157"
print(txt)

 # Hex Value 

txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

# String Methods

# CAPITALIZE 
txt = "My name is Sojwal"
print(txt.capitalize())

# CASEFOLD
txt = "HEY GUys my NAme is SOJWAL"
print(txt.casefold())

# CENTER
txt = "sojwal"
print(txt.center(51))

# COUNT
txt = "I love apples , apples are my fav fruit"
print(txt.count("apples"))

# ENCODE 
txt = "Text to be encode"
print(txt.encode())

# ENDSWITH
txt = "Hello , Welcome to my World"
print(txt.endswith("World"))

# ---------> 

txt = "Hello , welcome to my channel"
print(txt.endswith("channel"))

# ---------->

txt = " hey guys welcome to my channel"
print(txt.find("welcome"))

a = 'hey'
b = ' soju' 
c = a+b
print(c)