from setuptools import setup

setup(
    name='NlpToolkit-Dictionary',
    version='1.0.17',
    packages=['Language', 'Dictionary', 'Dictionary.Trie', 'Syllibification'],
    url='https://github.com/olcaytaner/Dictionary-Py',
    license='',
    author='olcaytaner',
    author_email='olcaytaner@isikun.edu.tr',
    description='Simple Dictionary Processing',
    install_requires=['NlpToolkit-Math']
)
