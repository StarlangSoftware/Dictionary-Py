from Language.TurkishLanguage import TurkishLanguage
import re


class Word:
    name: str

    def __init__(self, name: str):
        """
        A constructor of Word class which gets a String name as an input and assigns to the name variable.

        PARAMETERS
        ----------
        name : str
            String input.
        """
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __str__(self) -> str:
        """
        The overridden __str__ method returns the name variable.

        RETURNS
        -------
        str
            the name variable.
        """
        return self.name

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name

    def charCount(self) -> int:
        """
        The charCount method returns the length of name variable.

        RETURNS
        -------
        int
            the length of name variable.
        """
        return len(self.name)

    def getName(self) -> str:
        """
        Getter for the name variable.

        RETURNS
        -------
        str
            name variable.
        """
        return self.name

    def setName(self, name: str):
        """
        Setter for the name variable.

        PARAMETERS
        ----------
        name : str
            String input.
        """
        self.name = name

    @staticmethod
    def beforeLastVowel(stem: str) -> str:
        """
        The beforeLastVowel method takes a str stem as an input. It loops through the given stem and returns
        the second last vowel.

        PARAMETERS
        ----------
        stem : str
            String input.

        RETURNS
        -------
        str
            Vowel before the last vowel.
        """
        last = "0"
        before = 1
        for i in range(len(stem) - 1, -1, -1):
            if TurkishLanguage.isVowel(stem[i]):
                if before == 1:
                    last = stem[i]
                    before = before - 1
                    continue
                return stem[i]
        return last

    @staticmethod
    def lastVowel(stem: str) -> str:
        """
        The lastVowel method takes a str stem as an input. It loops through the given stem and returns
        the last vowel.

        PARAMETERS
        ----------
        stem : str
            String input.

        RETURNS
        -------
        str
            The last vowel.
        """
        for i in range(len(stem) - 1, - 1, -1):
            if TurkishLanguage.isVowel(stem[i]):
                return stem[i]
        for i in range(len(stem) - 1, -1, -1):
            if "0" <= stem[i] <= "9":
                return stem[i]
        return "0"

    @staticmethod
    def lastPhoneme(stem: str) -> str:
        """
        The lastPhoneme method takes a str stem as an input. It then returns the last phoneme of the given stem.

        PARAMETERS
        ----------
        stem : str
            String input.

        RETURNS
        -------
        str
            The last phoneme.
        """
        if len(stem) == 0:
            return " "
        if stem[len(stem) - 1] != "'":
            return stem[len(stem) - 1]
        else:
            return stem[len(stem) - 2]

    @staticmethod
    def isCapital(surfaceForm: str) -> bool:
        """
        The isCapital method takes a String surfaceForm as an input and returns true if the character at first index of
        surfaceForm is a capital letter, false otherwise.

        PARAMETERS
        ----------
        surfaceForm : str
            String input to check the first character.

        RETURNS
        -------
        bool
            true if the character at first index of surfaceForm is a capital letter, false otherwise.
        """
        return surfaceForm[0] in TurkishLanguage.UPPERCASE_LETTERS

    @staticmethod
    def isPunctuationSymbol(surfaceForm: str) -> bool:
        """
        The isPunctuationSymbol method takes a String surfaceForm as an input and returns true if it is a punctuation,
        False otherwise.
        Grave accent : \u0060
        Left quotation mark : \u201C
        Right quotation mark : \u201D
        Left single quotation mark : \u2018
        Horizontal ellipsis : \u2026

        PARAMETERS
        ----------
        surfaceForm : str
            String input to check.

        RETURNS
        -------
        bool
            true if it is a punctuation, false otherwise.
        """
        return surfaceForm == "." or surfaceForm == "..." or surfaceForm == "[" or surfaceForm == "]" or \
               surfaceForm == "\u2026" or surfaceForm == "%" or surfaceForm == "&" or surfaceForm == "=" or \
               surfaceForm == "\u0060\u0060" or surfaceForm == "\u0060" or surfaceForm == "''" or surfaceForm == "$" or \
               surfaceForm == "!" or surfaceForm == "?" or surfaceForm == "," or surfaceForm == ":" or \
               surfaceForm == "--" or surfaceForm == ";" or surfaceForm == "(" or surfaceForm == ")" or \
               surfaceForm == "'" or surfaceForm == "\"" or surfaceForm == "\u201C" or surfaceForm == "\u2018" or \
               surfaceForm == "\u201D" or surfaceForm == "…" or surfaceForm == "\u25CF" or surfaceForm == "/" or \
               surfaceForm == "-" or surfaceForm == "+" or surfaceForm == "-LRB-" or surfaceForm == "-RRB-" or \
               surfaceForm == "-LCB-" or surfaceForm == "-RCB-" or surfaceForm == "-LSB-" or surfaceForm == "-RSB-"

    @staticmethod
    def isHonorific(surfaceForm: str) -> bool:
        """
        The isHonorific method takes a String surfaceForm as an input and after converting it to lower case it returns
        true if it equals to "bay" or "bayan", false otherwise.

        PARAMETERS
        ----------
        surfaceForm : str
            String input to check.

        RETURNS
        -------
        bool
            true if it equals to "bay" or "bayan", false otherwise.
        """
        lower_case = surfaceForm.lower()
        return lower_case == "bay" or lower_case == "bayan"

    @staticmethod
    def isOrganization(surfaceForm: str) -> bool:
        """
        The isOrganization method takes a String surfaceForm as an input and after converting it to lower case it
        returns true if it equals to "corp", "inc.", or "co.", and false otherwise.

        PARAMETERS
        ----------
        surfaceForm : str
            String input to check.

        RETURNS
        -------
        bool
            true if it equals to "corp", "inc.", or "co.", and false otherwise.
        """
        lower_case = surfaceForm.lower()
        return lower_case == "corp" or lower_case == "inc." or lower_case == "co."

    @staticmethod
    def isMoney(surfaceForm: str) -> bool:
        """
        The isMoney method takes a String surfaceForm as an input and after converting it to lower case it returns true
        if it equals to one of the dolar, sterlin, paunt, ons, ruble, mark, frank, yan, sent, yen' or $, and false
        otherwise.

        PARAMETERS
        ----------
        surfaceForm : str
            String input to check.

        RETURNS
        -------
        bool
            true if it equals to one of the dolar, sterlin, paunt, ons, ruble, mark, frank, yan, sent, yen' or $, and
            false otherwise.
        """
        lower_case = surfaceForm.lower()
        return lower_case.startswith("dolar") or lower_case.startswith("sterlin") or lower_case.startswith("paunt") or \
               lower_case.startswith("ons") or lower_case.startswith("ruble") or lower_case.startswith("mark") or \
               lower_case.startswith("frank") or lower_case == "yen" or lower_case.startswith("sent") or \
               lower_case.startswith("cent") or lower_case.startswith("yen'") or ("$" in lower_case)

    def isPunctuation(self) -> bool:
        """
        The isPunctuation method without any argument, it checks name variable whether it is a punctuation or not and
        returns true if so.

        RETURNS
        -------
        bool
            true if name is a punctuation.
        """
        return self.name == "," or self.name == "." or self.name == "!" or self.name == "?" or self.name == ":" or \
               self.name == ";" or self.name == "\"" or self.name == "''" or self.name == "'" or self.name == "`" or \
               self.name == "``" or self.name == "..." or self.name == "-" or self.name == "--"

    @staticmethod
    def isTime(surfaceForm: str) -> bool:
        """
        The isTime method takes a String surfaceForm as an input and after converting it to lower case it checks some
        cases.
        If it is in the form of 12:23:34 or 12:23 it returns true.
        If it starts with name of months; ocak, şubat, mart, nisan, mayıs, haziran, temmuz, ağustos, eylül, ekim, kasım,
        aralık it returns true.
        If it equals to the name of days; pazar, pazartesi, salı, çarşamba, perşembe, cuma, cumartesi it returns true.

        PARAMETERS
        ----------
        surfaceForm : str
            String input to check.

        RETURNS
        -------
        bool
            true if it presents time, and false otherwise.
        """
        lower_case = surfaceForm.lower()
        if re.fullmatch("(\\d\\d|\\d):(\\d\\d|\\d):(\\d\\d|\\d)", lower_case) is not None or \
                re.fullmatch("(\\d\\d|\\d):(\\d\\d|\\d)", lower_case) is not None:
            return True
        if lower_case.startswith("ocak") or lower_case.startswith("şubat") or lower_case.startswith("mart") or \
                lower_case.startswith("nisan") or lower_case.startswith("mayıs") or lower_case.startswith("haziran") \
                or lower_case.startswith("temmuz") or lower_case.startswith("ağustos") or lower_case.startswith("eylül") \
                or lower_case.startswith("ekim") or lower_case.startswith("kasım") or lower_case == "aralık":
            return True
        if lower_case == "pazar" or lower_case == "salı" or lower_case.startswith("çarşamba") or \
                lower_case.startswith("perşembe") or lower_case == "cuma" or lower_case.startswith("cumartesi") \
                or lower_case.startswith("pazartesi"):
            return True
        if "'" in lower_case:
            lower_case = lower_case[0:lower_case.find("'")]
        try:
            time = int(lower_case)
            if 1900 < time < 2200:
                return True
        except ValueError:
            return False
        return False

    @staticmethod
    def toWordArray(sourceArray: list) -> list:
        """
        The toWordArray method takes a String sourceArray as an input. First it creates a Word type result list and puts
        items of input sourceArray to this result list.

        PARAMETERS
        ----------
        sourceArray : list
            String list.

        RETURNS
        -------
        list
            Word type list.
        """
        result = []
        for word in sourceArray:
            result.append(Word(word))
        return result

    def toCharacters(self) -> list:
        """
        The toCharacters method creates a Word type characters list and adds characters of name variable
        to newly created list.

        RETURNS
        -------
        list
            Word type list.
        """
        characters = []
        for i in range(len(self.name)):
            characters.append(Word(self.name[i]))
        return characters

    def __repr__(self):
        return self.name
