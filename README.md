# Dictionary

This resource is a dictionary of Modern Turkish, comprised of the definitions of over 50.000 individual entries. Each entry is matched with its corresponding synset (set of synonymous words and expressions) in the Turkish WordNet, KeNet.

For Developers
============
You can also see either [Java](https://github.com/olcaytaner/Dictionary) 
or [C++](https://github.com/olcaytaner/Dictionary-CPP) repository.
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

	git clone https://github.com/olcaytaner/Dictionary-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `DataStructure-PY` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 


## Compile

**From IDE**

After being done with the downloading and Maven indexing, select **Build Project** option from **Build** menu. After compilation process, user can run DataStructure.

Detailed Description
============
+ [TxtDictionary](#txtdictionary)
+ [TxtWord](#txtword)
+ [SyllableList](#syllablelist)

## TxtDictionary

Bir alana özgü veya Türkçe sözlüğü yüklemek için kullanılır. Ayrıca yanlış yazılmış
kelimeler ve yanlış yazılmış kelimelerin doğru formları da yüklenebilir.

Türkçe sözlüğü ve yazım yanlışları sözlüğünü yüklemek için

	a = TxtDictionary()
	
Alana özgü sözlüğü ve yazım yanlışı sözlüğünü yüklemek için

	TxtDictionary(String fileName, WordComparator comparator, String misspelledFileName)

Belirli bir sözcüğün sözlükte olup olmadığı,

	Word getWord(String name)

## TxtWord

Sözlükteki kelimelerin özellikleri TxtWord sınıfının, isim olup olmadıkları

	boolean isNominal()

sıfat olup olmadıkları,

	boolean isAdjective()

bileşik isim olup olmadıkları

	boolean isPortmanteau()

ünlü uyumuna uyup uymadıkları

	notObeysVowelHarmonyDuringAgglutination

ek aldıklarında yumuşayıp yumuşamadıkları

	boolean rootSoftenDuringSuffixation()

## SyllableList

Kelimeyi hecelerine ayırmak için de SyllableList sınıfı kullanılır.

	SyllableList(String word)
