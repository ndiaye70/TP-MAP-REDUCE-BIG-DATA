#!/usr/bin/env python3
import sys

def reducer():
    current_word = None
    current_count = 0
    
    for line in sys.stdin:
        # Diviser la ligne en mot et compteur
        word, count = line.strip().split('\t')
        count = int(count)
        
        # Si le mot change, émettre le résultat précédent
        if word != current_word:
            if current_word:
                print(f"{current_word}\t{current_count}")
            current_word = word
            current_count = 0
        current_count += count
    
    # Émettre le dernier mot
    if current_word:
        print(f"{current_word}\t{current_count}")

if __name__ == "__main__":
    reducer()