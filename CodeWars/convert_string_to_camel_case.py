#!/usr/bin/env python3
# 3/5/2020
# CODEWARS
# Complete the method/function so that it converts dash/underscore 
# delimited words into camel casing. The first word within the output should 
# be capitalized only if the original word was capitalized (known as Upper Camel Case, 
# also often referred to as Pascal case).

# Examples
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

def to_camel_case(text):
    textList = []
    camelCaseText = ""
    
    if text == "":
        print("Empty String\n")
    else:
        textList = text.replace("-", "_").split("_")

        camelCaseText = textList[0]

        for word in textList[1:]:
            camelCaseText += word.capitalize() 

        print("ORIGINAL: " + str(text)) 
        print("CAMEL CASE: " + str(camelCaseText))
        print("\n")

    
print("## Testing function to_camel_case ##\n")
to_camel_case('')
to_camel_case("the_stealth_warrior")
to_camel_case("The-Stealth-Warrior")
to_camel_case("A-B-C")