def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    lower = text.lower()
    character_count = {}
    for character in lower:
        if character == " ":
            pass
        elif character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count
    

def order_characters(characters):
    return sorted(characters.items(), key=lambda item: item[1], reverse=True)
    