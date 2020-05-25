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
        lowerCase = surfaceForm.lower()
        return lowerCase == "bay" or lowerCase == "bayan"

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
        lowerCase = surfaceForm.lower()
        return lowerCase == "corp" or lowerCase == "inc." or lowerCase == "co."

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
        lowerCase = surfaceForm.lower()
        return lowerCase.startswith("dolar") or lowerCase.startswith("sterlin") or lowerCase.startswith("paunt") or \
               lowerCase.startswith("ons") or lowerCase.startswith("ruble") or lowerCase.startswith("mark") or \
               lowerCase.startswith("frank") or lowerCase == "yen" or lowerCase.startswith("sent") or \
               lowerCase.startswith("cent") or lowerCase.startswith("yen'") or ("$" in lowerCase)

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
        lowerCase = surfaceForm.lower()
        if re.fullmatch("(\\d\\d|\\d):(\\d\\d|\\d):(\\d\\d|\\d)", lowerCase) is not None or \
                re.fullmatch("(\\d\\d|\\d):(\\d\\d|\\d)", lowerCase) is not None:
            return True
        if lowerCase.startswith("ocak") or lowerCase.startswith("şubat") or lowerCase.startswith("mart") or \
                lowerCase.startswith("nisan") or lowerCase.startswith("mayıs") or lowerCase.startswith("haziran") \
                or lowerCase.startswith("temmuz") or lowerCase.startswith("ağustos") or lowerCase.startswith("eylül") \
                or lowerCase.startswith("ekim") or lowerCase.startswith("kasım") or lowerCase == "aralık":
            return True
        if lowerCase == "pazar" or lowerCase == "salı" or lowerCase.startswith("çarşamba") or \
                lowerCase.startswith("perşembe") or lowerCase == "cuma" or lowerCase.startswith("cumartesi") \
                or lowerCase.startswith("pazartesi"):
            return True
        if "'" in lowerCase:
            lowerCase = lowerCase[0:lowerCase.find("'")]
        try:
            time = int(lowerCase)
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
