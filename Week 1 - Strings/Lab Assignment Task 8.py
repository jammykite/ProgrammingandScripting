#print intro and request user input
print("Welcome to the Spellchecker")

while True:
    user_input = input("Please enter a word you would like to check: ")

    # replacements for common misspellings
    modified_input = user_input.replace('ths', 'this') \
        .replace('teh', 'the') \
        .replace('helo', 'hello') \
        .replace('recieve', 'receive') \
        .replace('definately', 'definitely') \
        .replace('seperate', 'separate') \
        .replace('occured', 'occurred') \
        .replace('untill', 'until') \
        .replace('acommodate', 'accommodate') \
        .replace('believeing', 'believing') \
        .replace('calender', 'calendar') \
        .replace('appologies', 'apologies') \
        .replace('arguement', 'argument') \
        .replace('buisness', 'business') \
        .replace('embarras', 'embarrass') \
        .replace('existance', 'existence') \
        .replace('judgement', 'judgment') \
        .replace('neccessary', 'necessary') \
        .replace('occurence', 'occurrence') \
        .replace('recomend', 'recommend') \
        .replace('temperary', 'temporary')

    # Provide feedback on the correction process
    if modified_input != user_input:
        print(f"The word you entered: '{user_input}' has been corrected to: '{modified_input}'")
    else:
        print(f"The word you entered: '{user_input}' is spelled correctly.")

