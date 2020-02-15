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

    @staticmethod
    def isVowel(ch: str) -> bool:
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
        return ch in TurkishLanguage.VOWELS

    @staticmethod
    def isBackVowel(ch: str) -> bool:
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
        return ch in TurkishLanguage.BACK_VOWELS

    @staticmethod
    def isFrontVowel(ch: str) -> bool:
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
        return ch in TurkishLanguage.FRONT_VOWELS

    @staticmethod
    def isBackRoundedVowel(ch: str) -> bool:
        """
        The isBackRoundedVowel method takes a character as an input and returns true if given character is a back
        rounded vowel.

        PARAMETERS
        ----------
        ch : chr
            Character input to check.

        RETURNS
        -------
        bool
            true if given character is a back rounded vowel.
        """
        return ch in TurkishLanguage.BACK_ROUNDED_VOWELS

    @staticmethod
    def isFrontRoundedVowel(ch: str) -> bool:
        """
        The isFrontRoundedVowel method takes a character as an input and returns true if given character is a front
        rounded vowel.

        PARAMETERS
        ----------
        ch : chr
            Character input to check.

        RETURNS
        -------
        bool
            true if given character is a front rounded vowel.
        """
        return ch in TurkishLanguage.FRONT_ROUNDED_VOWELS

    @staticmethod
    def isBackUnroundedVowel(ch: str) -> bool:
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
        return ch in TurkishLanguage.BACK_UNROUNDED_VOWELS

    @staticmethod
    def isFrontUnroundedVowel(ch: str) -> bool:
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
        return ch in TurkishLanguage.FRONT_UNROUNDED_VOWELS

    @staticmethod
    def isConsonantDrop(ch: str) -> bool:
        """
        The isConsonantDrop method takes a character as an input and returns true if given character is a dropping
        consonant

        PARAMETERS
        ----------
        ch : chr
            Character input to check.

        RETURNS
        -------
        bool
            true if given character is a dropping consonant.
        """
        return ch in TurkishLanguage.CONSONANT_DROPS

    @staticmethod
    def isConsonant(ch: str) -> bool:
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
        return ch in TurkishLanguage.CONSONANTS

    @staticmethod
    def isSertSessiz(ch: str) -> bool:
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
        return ch in TurkishLanguage.SERT_SESSIZ
