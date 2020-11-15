import sys
from setuptools import pkg_resources

class EngDict():
    """ English Dictionary object
    """
    def __init__(self, file_name = 'data/dictionary.txt'):
        """ Default constructor.
            :param file_name: File to retrieve from the words definitions.
            Defaulted to the file 'dictionary.txt' included in the package.
        """
        self.d = dict()
        try: file = pkg_resources.resource_stream(__name__, file_name)
        except FileNotFoundError as e:
            print('File not found')
            sys.exit(0)
        except Exception as e:
            print('Exception: ' + e)
            sys.exit(0)
        for line in file:
            l = str(line).rstrip('\\r\\n\'').lstrip('b\'')
            s = [l[:l.find('(')].strip().upper(), l[l.find('('):]]
            if s[0] not in self.d: self.d[s[0]] = [s[1]]
            else: self.d[s[0]].append(s[1])
        file.close()

    def search(self, word):
        """ Function to search a word within the dictionary
            :param word: Word to be searched.
            :return self.d[word.upper()]: List of definitions associated to @word.
        """
        if word.upper() not in self.d:
            print('\nWord not found')
            return []
        else:
            return self.d[word.upper()]

