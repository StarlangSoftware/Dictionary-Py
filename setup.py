from setuptools import setup

setup(
    name='NlpToolkit-Dictionary',
    version='1.0.21',
    packages=['Language', 'Dictionary', 'Dictionary.Trie', 'Syllibification'],
    url='https://github.com/StarlangSoftware/Dictionary-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Simple Dictionary Processing',
    install_requires=['NlpToolkit-Math']
)
