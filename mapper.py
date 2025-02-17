#!/usr/bin/env python3
import sys

def mapper():
    for line in sys.stdin:
        # Diviser chaque ligne en mots
        words = line.strip().split()
        for word in words:
            # Nettoyer les mots
            cleaned_word = word.strip('.,!?;:"()[]').lower()
            if cleaned_word:
                # Émettre (mot, 1)
                print(f"{cleaned_word}\t1")

if __name__ == "__main__":
    mapper()