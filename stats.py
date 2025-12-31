def get_num_words(text):
    return len(text.split())

def count_characters(text):
    character_count = {}
    text_lower = text.lower() # avoids differentiation between capital and lowercase characters
    for character in text_lower:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def sort_key(characters):
    return characters["num"]

def sort_character_dict(characters_to_sort):
    dict_list = []
    for character in characters_to_sort:
        if character.isalpha() != True:
            continue
        dict_with_keys = {}
        dict_with_keys["char"] = character
        dict_with_keys["num"] = characters_to_sort[character]
        dict_list.append(dict_with_keys)
    dict_list.sort(reverse=True, key=sort_key)
    return dict_list
