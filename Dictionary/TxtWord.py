from __future__ import annotations
from Dictionary.Word import Word


class TxtWord(Word):

    __flags: list

    """
    Another constructor of TxtWord class which takes a String name and a flag as inputs and calls its super class Word
    with given name. Then, creates a new list as flags and calls addFlag method with given flag.

    PARAMETERS
    ----------
    name : str
        String input.
    flag : str
        String input.
    """
    def __init__(self, name : str, flag=None):
        super().__init__(name)
        self.__flags = []
        if flag is not None:
            self.addFlag(flag)

    """
    The addFlag method takes a String flag as an input and adds given flag to the flags list.

    PARAMETERS
    ----------
    flag : str
        String input to add.
    """
    def addFlag(self, flag : str):
        self.__flags.append(flag)

    """
    The removeFlag method takes a String flag as an input and removes given flag from the flags list.

    PARAMETERS
    ----------
    flag : str
        String input to remove.
    """
    def removeFlag(self, flag: str):
        self.__flags.remove(flag)

    """
    The verbType method checks flags list and returns the corresponding cases.

    RETURNS
    -------
    str
        the corresponding cases.
    """
    def verbType(self) -> str:
        if "F1P1-NO-REF" in self.__flags:
            """
            There is no example in the Turkish dictionary.
            """
            return "F1P1-NO-REF"
        if "F2P1-NO-REF" in self.__flags:
            """
            F2P1-NO-REF: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn 
            suffix, can take PassiveHl suffix, can take CausativeT suffix. e.g. Doğ, göç, için
            """
            return "F2P1-NO-REF"
        if "F3P1-NO-REF" in self.__flags:
            """
            F3P1-NO-REF: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn 
            suffix, can take Passive Hl suffix, can take CausativeT suffix. e.g. Ak
            """
            return "F3P1-NO-REF"
        if "F4P1-NO-REF" in self.__flags:
            """
            F4P1-NO-REF: The bare-form is a verb and depending on this attribute, the verb can't take PassiveHn 
            suffix, can take CausativeT suffix. e.g. Aksa
            """
            return "F4P1-NO-REF"
        if "F4PR-NO-REF" in self.__flags:
            """
            F4PR-NO-REF: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn 
            suffix, can take PassiveHl suffix, can take CausativeT suffix. e.g. Çevir, göster
            """
            return "F4PR-NO-REF"
        if "F4PL-NO-REF" in self.__flags:
            """
            F4PL-NO-REF: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn 
            suffix, can take CausativeT suffix. e.g. Azal, çoğal
            """
            return "F4PL-NO-REF"
        if "F4PW-NO-REF" in self.__flags:
            """
            F4PW-NO-REF: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn 
            suffix, can take PassiveN suffix, can take CausativeT suffix. e.g. Birle, boya
            """
            return "F4PW-NO-REF"
        if "F5PL-NO-REF" in self.__flags:
            """
            F5PL-NO-REF: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn 
            suffix, can take CausativeDHr suffix. e.g. Çal, kal
            """
            return "F5PL-NO-REF"
        if "F5PR-NO-REF" in self.__flags:
            """
            F5PR-NO-REF: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn 
            suffix, can take PassiveHl suffix, can take CausativeDHr suffix. e.g. Birleş, çöz
            """
            return "F5PR-NO-REF"
        if "F5PW-NO-REF" in self.__flags:
            """
            F5PW-NO-REF: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn 
            suffix, can take PassiveHl suffix, can take CausativeDHr suffix. e.g. Ye
            """
            return "F5PW-NO-REF"
        if "F1P1" in self.__flags:
            """
            F1P1: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn suffix, can 
            take PassiveHl suffix, can take CausativeAr suffix, can take ReciprocalHs suffix. e.g. Çık, kop
            """
            return "F1P1"
        if "F2P1" in self.__flags:
            """
            F2P1: The bare-form is a verb and depending on this attribute, the verb can can not PassiveHn suffix, can 
            take CausativeHr suffix, can take CausativeDHr suffix, can take ReciprocalHs suffix. e.g. Bit, doy, düş
            """
            return "F2P1"
        if "F2PL" in self.__flags:
            """
            F2PL: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn suffix, can 
            take CausativeHr suffix, can take CausativeDHr suffix, can take ReciprocalHs suffix. e.g. Art, çök
            """
            return "F2PL"
        if "F3P1" in self.__flags:
            """
            F3P1: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn suffix, can 
            take PassiveHl suffix, can take CausativeHl suffix, can take ReciprocalHs suffix. e.g. Kok, sark
            """
            return "F3P1"
        if "F4P1" in self.__flags:
            """
            F4P1: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn suffix,
            can take CausativeT suffix, can take ReciprocalHs suffix. e.g. Anla
            """
            return "F4P1"
        if "F4PR" in self.__flags:
            """
            F4PR: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn suffix, can 
            take PassiveHl suffix, can take CausativeT suffix, can take ReciprocalHs suffix. e.g. Bitir, çağır
            """
            return "F4PR"
        if "F4PL" in self.__flags:
            """
            F4PL: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn suffix, can 
            take PassiveN suffix, can take CausativeT suffix, can take ReciprocalHs suffix. e.g. Bolal, çömel
            """
            return "F4PL"
        if "F4PW" in self.__flags:
            """
            F4PW: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn suffix, can 
            take PassiveN suffix, can take CausativeT suffix, can take ReciprocalHs suffix. e.g. Boyla, çağla
            """
            return "F4PW"
        if "F5P1" in self.__flags:
            """
            F5P1: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn suffix, can 
            take PassiveHl suffix, can take CausativeDHr suffix, can take ReciprocalHs suffix, can take ReflexiveHn 
            suffix. e.g. Giy
            """
            return "F5P1"
        if "F5PL" in self.__flags:
            """
            F5PL: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn suffix, can 
            take PassiveHl suffix, can take CausativeDHr suffix, can take ReciprocalHs suffix. e.g. Böl, dal
            """
            return "F5PL"
        if "F5PR" in self.__flags:
            """
            F5PR: The bare-form is a verb and depending on this attribute, the verb can take NominalVerb suffixes 
            "-sHm, -SHn, -yHz, SHnHz, -lAr", can take NominalVerb1 suffixes, "-yDH, -ysA", can take NominalVerb2 suffix,
            "-ymHs", can take AdjectiveRoot suffix, "-SH", can take Adjective suffix, "-ŞAr" e.g. Bilin, çalış
            """
            return "F5PR"
        if "F5PW" in self.__flags:
            """
            F5PW: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn suffix,
            can take CausativeDHr suffix, can take ReciprocalHs suffix. e.g. Boşver, cezbet
            """
            return "F5PW"
        if "F6P1" in self.__flags:
            """
            F6P1: The bare-form is a verb and depending on this attribute, the verb can not take PassiveHn suffix, 
            can take PassiveN suffix, can take ReciprocalHs suffix, can take ReflexiveHn suffix. e.g. Gizle, hazırla, 
            kaşı
            """
            return "F6P1"
        return ""

    """
    The samePos method takes TxtWord as input and returns true if;
    
    flags list contains CL_ISIM 
    CL_ISIM: The bare-form of the word is a noun. e.g. Abla

    flags list contains CL_FIIL
    CL_FIIL: The bare-form of the word is a verb. e.g. Affet

    flags list contains IS_ADJ
    IS_ADJ: The bare-form of the word is a adjective. e.g. Acayip

    flags list contains IS_ZM
    IS_ZM: The bare-form of the word is a pronoun. e.g. Başkası

    flags list contains IS_ADVERB
    IS_ADVERB: The bare-form of the word is a adverb. e.g. Tekrar, açıktan, adeta

    PARAMETERS
    ----------
    word : TxtWord
        TxtWord type input.
        
    RETURNS
    -------
    bool
        true if given word is nominal, verb, adjective, pronoun or adverb, false otherwise.
    """
    def samePos(self, word: TxtWord) -> bool:
        if self.isNominal() and word.isNominal():
            return True
        if self.isVerb() and word.isVerb():
            return True
        if self.isAdjective() and word.isAdjective():
            return True
        if self.isPronoun() and word.isPronoun():
            return True
        if self.isAdverb() and word.isAdverb():
            return True
        return False

    """
    The isNominal method returns true if flags list contains CL_ISIM.

    RETURNS
    -------
    bool
        true if flags list contains CL_ISIM.
    """
    def isNominal(self) -> bool:
        return "CL_ISIM" in self.__flags

    """
    The isPassive method returns true if flags list contains PASSIVE-HN.

    RETURNS
    -------
    bool
        true if flags list contains PASSIVE-HN.
    """
    def isPassive(self) -> bool:
        return "PASSIVE-HN" in self.__flags

    """
    The isAbbreviation method returns true if flags list contains IS_KIS.

    RETURNS
    -------
    bool
        true if flags list contains IS_KIS.
    """
    def isAbbreviation(self) -> bool:
        return "IS_KIS" in self.__flags

    """
    The isInterjection method returns true if flags list contains IS_INTERJ.

    RETURNS
    -------
    bool
        true if flags list contains IS_INTERJ.
    """
    def isInterjection(self) -> bool:
        return "IS_INTERJ" in self.__flags

    """
    The isDuplicate method returns true if flags list contains IS_DUP.

    RETURNS
    -------
    bool
        true if flags list contains IS_DUP.
    """
    def isDuplicate(self) -> bool:
        return "IS_DUP" in self.__flags

    """
    The isHeader method returns true if flags list contains IS_HEADER.

    RETURNS
    -------
    bool
        true if flags list contains IS_HEADER.
    """
    def isHeader(self) -> bool:
        return "IS_HEADER" in self.__flags

    """
    The isAdjective method returns true if flags list contains IS_ADJ.

    RETURNS
    -------
    bool
        true if flags list contains IS_ADJ.
    """
    def isAdjective(self) -> bool:
        return "IS_ADJ" in self.__flags

    """
    The isPureAdjective method returns true if flags list contains IS_PUREADJ.

    RETURNS
    -------
    bool
        true if flags list contains IS_PUREADJ.
    """
    def isPureAdjective(self) -> bool:
        return "IS_PUREADJ" in self.__flags

    """
    The isPronoun method returns true if flags list contains IS_ZM.
    IS_ZM: The bare-form of the word is a pronoun. e.g. Hangi, hep, hiçbiri

    RETURNS
    -------
    bool
        true if flags list contains IS_ZM.
    """
    def isPronoun(self) -> bool:
        return "IS_ZM" in self.__flags

    """
    The isQuestion method returns true if flags list contains IS_QUES.
    IS_QUES: The bare-form of the word is a question. e.g. Mi, mu, mü

    RETURNS
    -------
    bool
        true if flags list contains IS_QUES.
    """
    def isQuestion(self) -> bool:
        return "IS_QUES" in self.__flags

    """
    The isVerb method returns true if flags list contains CL_FIIL.

    RETURNS
    -------
    bool
        true if flags list contains CL_FIIL.
    """
    def isVerb(self) -> bool:
        return "CL_FIIL" in self.__flags

    """
    The isPortmanteau method returns true if flags list contains IS_BILEŞ.
    IS_BILEŞ: The bare-form is a portmanteau word in affixed form. e.g. gelinçiçeği

    RETURNS
    -------
    bool
        true if flags list contains IS_BILEŞ.
    """
    def isPortmanteau(self) -> bool:
        return "IS_BILEŞ" in self.__flags

    """
    The isDeterminer method returns true if flags list contains IS_DET.
    IS_DET: The bare-form of the word is a determiner. e.g. Bazı, bir

    RETURNS
    -------
    bool
        true if flags list contains IS_DET.
    """
    def isDeterminer(self) -> bool:
        return "IS_DET" in self.__flags

    """
    The isConjunction method returns true if flags list contains IS_CONJ.
    IS_CONJ: The bare-form of the word is a conjunction. e.g. Gerek, halbuki

    RETURNS
    -------
    bool
        true if flags list contains IS_CONJ.
    """
    def isConjunction(self) -> bool:
        return "IS_CONJ" in self.__flags

    """
    The isAdverb method returns true if flags list contains IS_ADVERB.

    RETURNS
    -------
    bool
        true if flags list contains IS_ADVERB.
    """
    def isAdverb(self) -> bool:
        return "IS_ADVERB" in self.__flags

    """
    The isPostP method returns true if flags list contains IS_POSTP.
    IS_POSTP: The bare-form of the word is a postposition. e.g. Önce, takdirde, üzere

    RETURNS
    -------
    bool
        true if flags list contains IS_POSTP.
    """
    def isPostP(self) -> bool:
        return "IS_POSTP" in self.__flags

    """
    The isPortmanteauEndingWithSI method returns true if flags list contains IS_B_SI.
    IS_B_SI: The bare-form is a portmanteau word ending with "sı". e.g. Giritlalesi

    RETURNS
    -------
    bool
        true if flags list contains IS_B_SI.
    """
    def isPortmanteauEndingWithSI(self) -> bool:
        return "IS_B_SI" in self.__flags

    """
    The isPortmanteauFacedVowelEllipsis method returns true if flags list contains IS_B_UD.
    IS_B_UD: The bare-form of the word includes vowel epenthesis,
    therefore the last inserted vowel drops during suffixation. e.g. İnsanoğlu

    RETURNS
    -------
    bool
        true if flags list contains IS_B_UD.
    """
    def isPortmanteauFacedVowelEllipsis(self) -> bool:
        return "IS_B_UD" in self.__flags

    """
    The isPortmanteauFacedSoftening method returns true if flags list contains IS_B_SD.
    IS_B_SD: The bare-form of the word includes softening. e.g. Çançiçeği

    RETURNS
    -------
    bool
        true if flags list contains IS_B_SD.
    """
    def isPortmanteauFacedSoftening(self) -> bool:
        return "IS_B_SD" in self.__flags

    """
    The isSuffix method returns true if flags list contains EK.
    EK: This tag indicates complementary verbs. e.g. İdi, iken, imiş.

    RETURNS
    -------
    bool
        true if flags list contains EK.
    """
    def isSuffix(self) -> bool:
        return "EK" in self.__flags

    """
    The isProperNoun method returns true if flags list contains IS_OA.
    IS_OA: The bare-form of the word is a proper noun. e.g. Abant, Beşiktaş

    RETURNS
    -------
    bool
        true if flags list contains IS_OA.
    """
    def isProperNoun(self) -> bool:
        return "IS_OA" in self.__flags

    """
    The isPlural method returns true if flags list contains IS_CA.
    IS_CA: The bare-form of the word is already in a plural form,
    therefore can not take plural suffixes such as "ler" or "lar". e.g. Buğdaygiller

    RETURNS
    -------
    bool
        true if flags list contains IS_CA.
    """
    def isPlural(self) -> bool:
        return "IS_CA" in self.__flags

    """
    The isNumeral method returns true if flags list contains IS_SAYI.
    IS_SAYI: The word is a number. e.g. Dört

    RETURNS
    -------
    bool
        true if flags list contains IS_SAYI.
    """
    def isNumeral(self) -> bool:
        return "IS_SAYI" in self.__flags

    """
    The isReal method returns true if flags list contains IS_REELSAYI.

    RETURNS
    -------
    bool
        true if flags list contains IS_REELSAYI.
    """
    def isReal(self) -> bool:
        return "IS_REELSAYI" in self.__flags

    """
    The isFraction method returns true if flags list contains IS_KESIR.

    RETURNS
    -------
    bool
        true if flags list contains IS_KESIR.
    """
    def isFraction(self) -> bool:
        return "IS_KESIR" in self.__flags

    """
    The isTime method returns true if flags list contains IS_ZAMAN.

    RETURNS
    -------
    bool
        true if flags list contains IS_ZAMAN.
    """
    def isTime(self) -> bool:
        return "IS_ZAMAN" in self.__flags

    """
    The isDate method returns true if flags list contains IS_DATE.

    RETURNS
    -------
    bool
        true if flags list contains IS_DATE.
    """
    def isDate(self) -> bool:
        return "IS_DATE" in self.__flags

    """
    The isPercent method returns true if flags list contains IS_PERCENT.

    RETURNS
    -------
    bool
        true if flags list contains IS_PERCENT.
    """
    def isPercent(self) -> bool:
        return "IS_PERCENT" in self.__flags

    """
    The isRange method returns true if flags list contains IS_RANGE.

    RETURNS
    -------
    bool
        true if flags list contains IS_RANGE.
    """
    def isRange(self) -> bool:
        return "IS_RANGE" in self.__flags

    """
    The isOrdinal method returns true if flags list contains IS_ORD.
    IS_ORD: The bare-form of the word can take suffixes and these suffixes define a ranking. e.g. Birinci

    RETURNS
    -------
    bool
        true if flags list contains IS_ORD.
    """
    def isOrdinal(self) -> bool:
        return "IS_ORD" in self.__flags

    """
    The notObeysVowelHarmonyDuringAgglutination method returns true if flags list contains IS_UU.
    IS_UU: The bare-form does not obey vowel harmony while taking suffixes. e.g. Dikkat

    RETURNS
    -------
    bool
        true if flags list contains IS_UU.
    """
    def notObeysVowelHarmonyDuringAgglutination(self) -> bool:
        return "IS_UU" in self.__flags

    """
    The obeysAndNotObeysVowelHarmonyDuringAgglutination method returns true if flags list contains IS_UUU.
    IS_UUU: The bare-form does not obey vowel harmony while taking suffixes. e.g. Bol, kalp

    RETURNS
    -------
    bool
        true if flags list contains IS_UUU.
    """
    def obeysAndNotObeysVowelHarmonyDuringAgglutination(self) -> bool:
        return "IS_UUU" in self.__flags

    """
    The rootSoftenDuringSuffixation method returns true if flags list contains IS_SD, F_SD.

    RETURNS
    -------
    bool
        true if flags list contains IS_SD, F_SD.
    """
    def rootSoftenDuringSuffixation(self) -> bool:
        return "IS_SD" in self.__flags or "F_SD" in self.__flags

    """
    The rootSoftenAndNotSoftenDuringSuffixation method returns true if flags list contains IS_SDD.
    IS_SDD: The bare-form final consonant can (or can not) get devoiced during vowel-initial suffixation. e.g. Kalp

    RETURNS
    -------
    bool
        true if flags list contains IS_SDD.
    """
    def rootSoftenAndNotSoftenDuringSuffixation(self) -> bool:
        return "IS_SDD" in self.__flags

    """
    The verbSoftenDuringSuffixation method returns true if flags list contains F_SD.
    F_SD: The bare-form final consonant gets devoiced during vowel-initial suffixation. e.g. Cezbet

    RETURNS
    -------
    bool
        true if flags list contains F_SD.
    """
    def verbSoftenDuringSuffixation(self) -> bool:
        return "F_SD" in self.__flags

    """
    The nounSoftenDuringSuffixation method returns true if flags list contains IS_SD.
    IS_SD: The bare-form final consonant already has an accusative suffix. e.g. Kabağı

    RETURNS
    -------
    bool
        true if flags list contains IS_SD.
    """
    def nounSoftenDuringSuffixation(self) -> bool:
        return "IS_SD" in self.__flags

    """
    The endingKChangesIntoG method returns true if flags list contains IS_KG.
    IS_KG: The bare-form includes vowel epenthesis, therefore the last inserted vowel drope
    during suffixation. e.g. Çelenk

    RETURNS
    -------
    bool
        true if flags list contains IS_KG.
    """
    def endingKChangesIntoG(self) -> bool:
        return "IS_KG" in self.__flags

    """
    The isExceptional method returns true if flags list contains IS_EX.
    IS_EX: This tag defines exception words. e.g. Delikanlı

    RETURNS
    -------
    bool
        true if flags list contains IS_EX.
    """
    def isExceptional(self) -> bool:
        return "IS_EX" in self.__flags

    """
    The duplicatesDuringSuffixation method returns true if flags list contains IS_ST.
    IS_ST: The second consonant of the bare-form undergoes a resyllabification. e.g. His

    RETURNS
    -------
    bool
        true if flags list contains IS_ST.
    """
    def duplicatesDuringSuffixation(self) -> bool:
        return "IS_ST" in self.__flags

    """
    The duplicatesAndNotDuplicatesDuringSuffixation method returns true if flags list contains IS_STT.
    IS_STT: The second consonant of the bare-form undergoes a resyllabification. e.g. His

    RETURNS
    -------
    bool
        true if flags list contains IS_STT.
    """
    def duplicatesAndNotDuplicatesDuringSuffixation(self) -> bool:
        return "IS_STT" in self.__flags

    """
    The lastIdropsDuringSuffixation method returns true if flags list contains IS_UD.
    IS_UD: The bare-form includes vowel epenthesis, therefore the last inserted vowel drops during suffixation.
    e.g. Boyun

    RETURNS
    -------
    bool
        true if flags list contains IS_UD.
    """
    def lastIdropsDuringSuffixation(self) -> bool:
        return "IS_UD" in self.__flags

    """
    The lastIDropsAndNotDropDuringSuffixation method returns true if flags list contains IS_UDD.
    IS_UDD: The bare-form includes vowel epenthesis, therefore the last inserted vowel can (or can not) drop during 
    suffixation. e.g. Kadir

    RETURNS
    -------
    bool
        true if flags list contains IS_UDD.
    """
    def lastIDropsAndNotDropDuringSuffixation(self) -> bool:
        return "IS_UDD" in self.__flags

    """
    The takesRelativeSuffixKi method returns true if flags list contains IS_KI.
    IS_KI: The word can take a suffix such as "ki". e.g. Önce

    RETURNS
    -------
    bool
        true if flags list contains IS_KI.
    """
    def takesRelativeSuffixKi(self) -> bool:
        return "IS_KI" in self.__flags

    """
    The takesRelativeSuffixKu method returns true if flags list contains IS_KU.
    IS_KU: The word can take a suffix such as "kü". e.g. Bugün

    RETURNS
    -------
    bool
        true if flags list contains IS_KU.
    """
    def takesRelativeSuffixKu(self) -> bool:
        return "IS_KU" in self.__flags

    """
    The consonantSMayInsertedDuringPossesiveSuffixation method returns true if flags list contains IS_SII.

    RETURNS
    -------
    bool
        true if flags list contains IS_SII.
    """
    def consonantSMayInsertedDuringPossesiveSuffixation(self) -> bool:
        return "IS_SII" in self.__flags

    """
    The lastIdropsDuringPassiveSuffixation method returns true if flags list contains F_UD.
    F_UD: The bare-form includes vowel epenthesis, therefore the last "ı"
    drops during passive suffixation. e.g. Çağır

    RETURNS
    -------
    bool
        true if flags list contains F_UD.
    """
    def lastIdropsDuringPassiveSuffixation(self) -> bool:
        return "F_UD" in self.__flags

    """
    The vowelAChangesToIDuringYSuffixation method returns true if flags list contains F_GUD.
    F_GUD: The verb bare-form includes vowel reduction, the last vowel "a" of the bare-form is replaced with "ı"
    e.g. Buzağıla

    RETURNS
    -------
    bool
        true if flags list contains F_GUD.
    """
    def vowelAChangesToIDuringYSuffixation(self) -> bool:
        return "F_GUD" in self.__flags

    """
    The vowelEChangesToIDuringYSuffixation method returns true if flags list contains F_GUDO.
    F_GUDO: The verb bare-form includes viwel reduction, the last vowel "e" of the
    bare-form is replaced with "i". e.g. Ye

    RETURNS
    -------
    bool
        true if flags list contains F_GUDO.
    """
    def vowelEChangesToIDuringYSuffixation(self) -> bool:
        return "F_GUDO" in self.__flags

    """
    The takesSuffixIRAsAorist method returns true if flags list contains F_GIR.
    F_GIR: The bare-form of the word takes "ir" suffix. e.g. Geç

    RETURNS
    -------
    bool
        true if flags list contains F_GIR.
    """
    def takesSuffixIRAsAorist(self) -> bool:
        return "F_GIR" in self.__flags

    """
    The takesSuffixDIRAsFactitive method returns true if flags list contains F_DIR.
    F_DIR: The bare-form of the word takes "tır" suffix. e.g. Daral

    RETURNS
    -------
    bool
        true if flags list contains F_DIR.
    """
    def takesSuffixDIRAsFactitive(self) -> bool:
        return "F_DIR" in self.__flags

    """
    The showsSuRegularities method returns true if flags list contains IS_SU.

    RETURNS
    -------
    bool
        true if flags list contains IS_SU.
    """
    def showsSuRegularities(self) -> bool:
        return "IS_SU" in self.__flags

    """
    The containsFlag method returns true if flags list contains flag.

    RETURNS
    -------
    bool
        true if flags list contains flag.
    """
    def containsFlag(self, flag: str) -> bool:
        return flag in self.__flags

    def __str__(self) -> str:
        result = super().__str__()
        for flag in self.__flags:
            result = result + " " + flag
        return result
