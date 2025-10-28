def number_of_words(text):
    new_arr = text.split()
    print(f"Found {len(new_arr)} total words")

def number_of_each_character(text):
    new_arr = list(text.lower())
    dictionary = {}
    for letter in new_arr:
        if not letter.isalpha():  # skip anything that's not a letter
            continue

        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    
    return dictionary

def sorted_character_count(char_dict):
    new_dict = []

    for char, count in char_dict.items():
        new_dict.append({"char": char, "count": count})
    
    sorted_list = sorted(new_dict, reverse=True, key=lambda x: x["count"])
    return sorted_list