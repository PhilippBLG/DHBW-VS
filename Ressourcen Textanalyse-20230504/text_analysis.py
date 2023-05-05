"""Simple text analysis.

Author:
    Wolfgang Funk <funk@dhbw-vs.de>

"""


def pre_process_text(text):
    text = text.lower()
    text = text.strip()
    substitutes = ["--", ".", ":", ",", ";", "!", "?"]
    for sub in substitutes:
        text = text.replace(sub, "")
    return text


filename = "moby.txt"

try:
    word_count = 0
    char_count = 0
    vowels = {}
    words_count = {}
    with open(filename) as file:
        for raw_line in file:
            line = pre_process_text(raw_line)
            words = line.split()
            word_count += len(words)
            for w in words:
                char_count += len(w)
                for c in w:
                    if c in "aeiou":
                        if c in vowels:
                            vowels[c] += 1
                        else:
                            vowels[c] = 1
            for w in words:
                if w in words_count:
                    words_count[w] += 1
                else:
                    words_count[w] = 1

except FileNotFoundError:
    print(f"{filename} not found. Wrong path?")
else:
    print(f"Wörter: {word_count}")
    print(f"Zeichen: {char_count}")
    print(f"Zeichen pro Wort: {char_count / word_count:.2f}")
    print(f"Number of vowels:")
    for vowel in vowels:
        print(f"    {vowel}:     {vowels[vowel]}")
    print(f"Häufigster Vokal: '{max(vowels, key=vowels.get)}' mit der Anzahl {max(vowels.values())}")
    for i in range(1, 11):
        most_common_word = sorted(words_count, key=words_count.get)[-i]
        print(f"{i}. häufigstes Wort: '{most_common_word}' mit der Anzahl {words_count[most_common_word]}")
