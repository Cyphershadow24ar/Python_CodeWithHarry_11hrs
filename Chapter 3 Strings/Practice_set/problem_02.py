#Write a program to fill in a letter template given below with name and date.

# name = input("Enter the name: ")

# date = int(input("Enter the date: "))

letter = '''Dear <|Name|>,
you are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Aniket Raj").replace("<|Date|>", "22nd of June 2024."))

