def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def num_chars(text):
    chars={}
    for char in text.lower():
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars           

def report(text):
    chars = num_chars(text)
    replist = list(chars.items())
    replist.sort(key=lambda x: x[1], reverse=True)
    
    print("--- Begin report ---")
    print(f"{len(text.split())} words found in the document.")
    for char, count in replist:
        print(f"The '{char}' character was found {count} times.")
    print("--- End Report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(num_chars(file_contents))  
        print(count_words(file_contents))
        report(file_contents)

if __name__ == "__main__":
    main()