For Developers
============

You can also see [Cython](https://github.com/starlangsoftware/Dictionary-Cy), [Java](https://github.com/starlangsoftware/Dictionary), [C++](https://github.com/starlangsoftware/Dictionary-CPP), [Swift](https://github.com/starlangsoftware/Dictionary-Swift), or [C#](https://github.com/starlangsoftware/Dictionary-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called Dictionary will be created. Or you can use below link for exploring the code:

	git clone https://github.com/starlangsoftware/Dictionary-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `DataStructure-PY` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 

Detailed Description
============

+ [TxtDictionary](#txtdictionary)
+ [TxtWord](#txtword)
+ [SyllableList](#syllablelist)

## TxtDictionary

Dictionary is used in order to load Turkish dictionary or a domain specific dictionary. In addition, misspelled words and the true forms of the misspelled words can also be loaded.

To load the Turkish dictionary and the misspelled words dictionary,

	a = TxtDictionary()
	
To load the domain specific dictionary and the misspelled words dictionary,

	TxtDictionary(self, fileName=None, misspelledFileName=None)

And to see if the dictionary involves a specific word, getWord is used.

	getWord(self, name: str) -> Word

## TxtWord

The word features: To see whether the TxtWord class of the dictionary is a noun or not,

	isNominal(self) -> bool

To see whether it is an adjective,

	isAdjective(self) -> bool

To see whether it is a portmanteau word,

	isPortmanteau(self) -> bool

To see whether it obeys vowel harmony,

	notObeysVowelHarmonyDuringAgglutination(self) -> bool

And, to see whether it softens when it get affixes, the following is used.

	rootSoftenDuringSuffixation(self) -> bool

## SyllableList

To syllabify the word, SyllableList class is used.

	SyllableList(self, word: str)
