from hazm import Normalizer
import string
import re


# normalizer
normalizer = Normalizer()
def normalize_text(text: str) -> str:
    """
    Normalize Persian text using Hazm.

    Parameters
    ----------
    text : str
        Input Persian text.
    Returns
    -------
    str
        Normalized text.
    """
    return normalizer.normalize(text)


# clean number
def convert_digit(text: str) -> str:
    """
    Convert Persian digits to English digits.
    Parameters
    ----------
    text : str
        Input text.
    Returns
    -------
    str
        Text with English digits.
    """
    persian_number = "۰۱۲۳۴۵۶۷۸۹"
    english_number = "0123456789"
    tabel = str.maketrans(persian_number, english_number)

    return text.translate(tabel)


# clean mention
def renove_mention(text: str) -> str:
    """
    Remove mention from text.

    Parameters
    ----------
    text : str
        Input text.
    Returns
    -------
    str
        Text without mention.
    """
    return re.sub(r"@\w+", "", text)


# clean punctuationun
def remove_punctuation(text: str, keep: str="") -> str:
    """
    Remove punctuation characters from text.

    Parameters
    ----------
    text : str
        Input text.

    keep : str, optional
        Punctuation characters that should not be removed.

    Returns
    -------
    str
        Text without punctuation.
    """

    punctuation = string.punctuation + "،؛«»٪"

    punctuation = "".join(ch for ch in punctuation if ch not in keep)

    return "".join(ch for ch in text if ch not in punctuation)


# clean extra space
def remove_extra_space(text: str) -> str:
    """
    Remove redundant whitespace from text.
    Parameters
    ----------
    text : str
        Input text.
    Returns
    -------
    str
        Text with normalized spacing.
    """
    return re.sub(r"\s+", " ", text).strip()



# pipeline
def preprocesing_text(text: str, keep_punctuation: str="") -> str:
    """
    Apply the preprocessing pipeline to a text.

    Parameters
    ----------
    text : str
        Input text.

    keep_punctuation : str, optional
        Punctuation characters that should not be removed.

    Returns
    -------
    str
        Cleaned text.
    """
    text = normalize_text(text)

    text = convert_digit(text)

    text = renove_mention(text)

    text = remove_punctuation(text, keep= keep_punctuation)

    text = remove_extra_space(text)

    return text