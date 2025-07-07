def get_num_words(content):
    count = len(content.split())
    return count
def get_num_character(contet):
    count_character = {}
    for words in contet.lower():
        for char in words:
            if char in count_character:
                count_character.update({char:count_character[char]+1})  
            else:
                count_character[char]=1
    return count_character
def count_character_report(path,num_words, num_char):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    itens_ordenados = sorted(num_char.items(), key=lambda item: item[1], reverse=True)
    for x,t in itens_ordenados:
        print(f"{x}: {t}")
    print("============= END ===============")
