from hazm import word_tokenize
from hazm.utils import stopwords_list

stop_word = set(stopwords_list())

def tokenizer(text: str, remove_stop_word: bool= False) -> list[str]:
    """
    Tokenize Persian text using Hazm.

    Parameters
    ----------
    text : str
        Input text.

    remove_stopwords : bool, default=False
        Remove Persian stop words.

    Returns
    -------
    list[str]
        List of tokens.
    """

    tokens = word_tokenize(text)
    if remove_stop_word:
        tokens = [token for token in tokens if token not in stop_word]
    return tokens
