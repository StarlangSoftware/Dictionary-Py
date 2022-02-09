from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='NlpToolkit-Dictionary',
    version='1.0.25',
    packages=['Language', 'Dictionary', 'Dictionary.data', 'Dictionary.Trie', 'Syllibification'],
    package_data={'Dictionary.data': ['*.txt']},
    url='https://github.com/StarlangSoftware/Dictionary-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Simple Dictionary Processing',
    install_requires=['NlpToolkit-Math'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
