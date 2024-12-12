"""
Create a dictionary and dump it into a JSON file
"""
import json

my_big_dictionary = {'key':'secret', 'number':92, 'Name':'it doesnt matter what your name is'}
with open('my_big_dictionary.json', 'w') as file:
    json.dump(my_big_dictionary, file, indent=4)
