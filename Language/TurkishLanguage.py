from Language.Language import Language


class TurkishLanguage(Language):
    VOWELS = "aeıioöuüâî"
    BACK_VOWELS = "aıouâ"
    FRONT_VOWELS = "eiöüî"
    BACK_ROUNDED_VOWELS = "ou"
    BACK_UNROUNDED_VOWELS = "aıâ"
    FRONT_ROUNDED_VOWELS = "öü"
    FRONT_UNROUNDED_VOWELS = "eiî"
    CONSONANT_DROPS = "nsy"
    CONSONANTS = "bcçdfgğhjklmnprsştvyzxqw"
    SERT_SESSIZ = "çfhkpsşt"
    LOWERCASE_LETTERS = "abcçdefgğhıijklmnoöprsştuüvyz"
    UPPERCASE_LETTERS = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    LETTERS = LOWERCASE_LETTERS + UPPERCASE_LETTERS

    """
    The isVowel method takes a character as an input and returns true if given character is a vowel.
    
    PARAMETERS
    ----------
    ch : chr
        Character input to check.
        
    RETURNS
    -------
    bool
        true if given character is a vowel.
    """

    def isVowel(ch: str) -> bool:
        return ch in TurkishLanguage.VOWELS

    """
    The isBackVowel method takes a character as an input and returns true if given character is a back vowel.

    PARAMETERS
    ----------
    ch : chr
        Character input to check.

    RETURNS
    -------
    bool
        true if given character is a back vowel.
    """

    def isBackVowel(ch: str) -> bool:
        return ch in TurkishLanguage.BACK_VOWELS

    """
    The isFrontVowel method takes a character as an input and returns true if given character is a front vowel.

    PARAMETERS
    ----------
    ch : chr
        Character input to check.

    RETURNS
    -------
    bool
        true if given character is a front vowel.
    """

    def isFrontVowel(ch: chr) -> bool:
        return ch in TurkishLanguage.FRONT_VOWELS

    """
    The isBackRoundedVowel method takes a character as an input and returns true if given character is a back rounded
    vowel.

    PARAMETERS
    ----------
    ch : chr
        Character input to check.

    RETURNS
    -------
    bool
        true if given character is a back rounded vowel.
    """

    def isBackRoundedVowel(ch: chr) -> bool:
        return ch in TurkishLanguage.BACK_ROUNDED_VOWELS

    """
    The isFrontRoundedVowel method takes a character as an input and returns true if given character is a front rounded
    vowel.

    PARAMETERS
    ----------
    ch : chr
        Character input to check.

    RETURNS
    -------
    bool
        true if given character is a front rounded vowel.
    """

    def isFrontRoundedVowel(ch: chr) -> bool:
        return ch in TurkishLanguage.FRONT_ROUNDED_VOWELS

    """
    The isBackUnroundedVowel method takes a character as an input and returns true if given character is a back 
    unrounded vowel.

    PARAMETERS
    ----------
    ch : chr
        Character input to check.

    RETURNS
    -------
    bool
        true if given character is a back unrounded vowel.
    """

    def isBackUnroundedVowel(ch: chr) -> bool:
        return ch in TurkishLanguage.BACK_UNROUNDED_VOWELS

    """
    The isFrontUnroundedVowel method takes a character as an input and returns true if given character is a front 
    unrounded vowel.

    PARAMETERS
    ----------
    ch : chr
        Character input to check.

    RETURNS
    -------
    bool
        true if given character is a front unrounded vowel.
    """

    def isFrontUnroundedVowel(ch: chr) -> bool:
        return ch in TurkishLanguage.FRONT_UNROUNDED_VOWELS

    """
    The isConsonantDrop method takes a character as an input and returns true if given character is a dropping consonant 

    PARAMETERS
    ----------
    ch : chr
        Character input to check.

    RETURNS
    -------
    bool
        true if given character is a dropping consonant.
    """

    def isConsonantDrop(ch: chr) -> bool:
        return ch in TurkishLanguage.CONSONANT_DROPS

    """
    The isConsonant method takes a character as an input and returns true if given character is a consonant 

    PARAMETERS
    ----------
    ch : chr
        Character input to check.

    RETURNS
    -------
    bool
        true if given character is a consonant.
    """

    def isConsonant(ch: chr) -> bool:
        return ch in TurkishLanguage.CONSONANTS

    """
    The isSertSessiz method takes a character as an input and returns true if given character is a sert sessiz 

    PARAMETERS
    ----------
    ch : chr
        Character input to check.

    RETURNS
    -------
    bool
        true if given character is a sert sessiz.
    """

    def isSertSessiz(ch: chr) -> bool:
        return ch in TurkishLanguage.SERT_SESSIZ
