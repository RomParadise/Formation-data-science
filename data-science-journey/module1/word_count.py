"""Word frequency counter."""


def word_count(text: str) -> dict[str, int]:
    txt = text.lower()
    words = txt.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
    return sorted_word_freq

    raise NotImplementedError