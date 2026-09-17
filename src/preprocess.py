import re
import string
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words("english"))


def clean_text(text):
    """
    Lowercase, remove punctuation/numbers, remove stopwords.
    Returns a single cleaned string (tokens joined by space).
    """
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)  # keep only letters and spaces
    tokens = text.split()
    tokens = [word for word in tokens if word not in STOPWORDS and len(word) > 1]

    return " ".join(tokens)


if __name__ == "__main__":
    # quick manual test
    sample = "I have 5+ years of experience in Data Analysis, SQL, and Python!"
    print("Before:", sample)
    print("After: ", clean_text(sample))