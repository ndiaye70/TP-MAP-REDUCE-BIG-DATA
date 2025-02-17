# WordCount sans MapReduce en Python

def wordcount_local(filename):
    word_counts = {}
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.lower()
                word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts


if __name__ == "__main__":
    filename = "Senegal.txt"  
    counts = wordcount_local(filename)
    

    for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")
