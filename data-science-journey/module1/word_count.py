"""Word frequency counter."""
import re

def word_count(text: str) -> dict[str, int]:
    """Return word frequencies sorted by descending count.

    Args:
        text: Input text to analyze.

    Returns:
        Dict mapping each lowercase word to its frequency.
    """
    txt = text.lower()
    words = re.findall(r"\w+", txt)
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
    return sorted_word_freq

    raise NotImplementedError