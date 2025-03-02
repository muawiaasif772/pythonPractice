logo=""""
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88
            88             88
           ""              88
                           88
 ,adPPYba, 88 8b,dPPYba,   88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a  88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8  88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8"  88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'   88       88  '"Ybbd8"' 88
              88
              88
"""
print(logo)
def life_in_weeks(age):
    yraes_remaing=90-age
    my_weeks_left=yraes_remaing*52
    return my_weeks_left

print(life_in_weeks(25))


def calculate_love_score(name1, name2):
    combined_name = name1 + name2
    love_name = combined_name.lower()

    # Calculate first digit
    first_digits=[]
    second_digits=[]
    first_digits.extend(
        [love_name.count('t'),love_name.count('r'),love_name.count('u'),love_name.count('e')]
    )

    second_digits.extend(
        [love_name.count('l'), love_name.count('o'), love_name.count('v'), love_name.count('e')]
    )


    first_sum = sum(first_digits)
    second_sum = sum(second_digits)

    # Create final score by concatenating
    score = int(str(first_sum) + str(second_sum))

    print(score)
# Example usage
calculate_love_score("Muawia", "Hamza")


# task 2
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# Define the alphabet
# alphabet = list("abcdefghijklmnopqrstuvwxyz")


def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter  # Keep non-alphabet characters unchanged
        else:
            if encode_or_decode == 'encode':

                shifted_position = (alphabet.index(letter) + shift_amount)
                shifted_position %= len(alphabet)
            elif encode_or_decode == 'decode':
                shifted_position = (alphabet.index(letter) - shift_amount)
                shifted_position %= len(alphabet)


            output_text += alphabet[shifted_position]  # Append the shifted letter

    print(f'Here is the {encode_or_decode}d text: {output_text}')


# Example usage
shoul_continue=True
while shoul_continue:
    direction = input("enter your direction: encode to encrypt decode to decrypt\n ").lower()
    text = input("enter your text:\n ").lower()
    shift = int(input("enter your shift number: "))
    ceaser(text, shift, direction)  # Output: khoor

    restsart=input('type yes to write agin otherwise no\n')
    if restsart=='no':
     shoul_continue=False
     print('goodbye')


