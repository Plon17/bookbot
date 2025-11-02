def count_words(text):
    list = text.split()
    count = len(list)
    return count

def count_characters(text):
    letters = {}
    character = text.lower()

    for cha in character:
        if cha not in letters:
            letters[cha] = 1
        else:
            letters[cha] += 1
    
    return letters

def sort_on(item):
    return item["num"]

def sort(keys):
    items = []
    for key, value in keys.items():
        items.append({"char": key, "num": value})
    
    items.sort(reverse=True, key=sort_on)
    return items