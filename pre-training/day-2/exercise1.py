import string

def word_frequency(text):

    text = text.lower()
    

    for p in string.punctuation:
        text = text.replace(p, "")
    

    words = text.split()
    

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    return freq



text = """
Python is a powerful programming language. Python is easy to learn and very
popular for data science, web development, and automation. Many developers
love Python because Python code is simple and readable.
"""


freq_dict = word_frequency(text)


sorted_words = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)


print("Top 5 most common words:")
for word, count in sorted_words[:5]:
    print(word, count)