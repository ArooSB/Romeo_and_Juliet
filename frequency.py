from romeo_and_juliet import PLAY


def get_words(text):
    words = text.split()
    return words


def words_frequency(words):
    frequency_dictionary = {}
    for word in words:
        frequency_dictionary[word] = frequency_dictionary.get(word, 0) + 1
    return frequency_dictionary


def top_n_words(freq, n):
    top_n = {}

    for _ in range(n):
        max_word = max(freq, key=freq.get)
        print(f"{max_word}: {freq[max_word]}")
        del freq[max_word]


def main():
    split_words = get_words(PLAY)
    freq_dict = words_frequency(split_words)
    top_n_words(freq_dict, 50)


if __name__ == "__main__":
    main()