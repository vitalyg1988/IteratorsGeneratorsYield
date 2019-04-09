import json
import wikipedia
import hashlib
from os import path
from IteratorsGeneratorsYield.logger.loggerDecor import logger_path


PATH_TO_FILE = path.abspath(path.join(path.dirname(__file__), 'output.txt'))


class MyIter:

    def __init__(self, description):
        self.description = description
        self.start_index = -1

    @property
    def name_country(self):
        try:
            return self.description[self.start_index]['name']['common']
        except wikipedia.exceptions.DisambiguationError:
            return ''

    def write_file(self):
        try:
            response = wikipedia.page(self.name_country)
        except wikipedia.exceptions.DisambiguationError:
            response = wikipedia.page(f"{self.name_country} (country)")
        with open(PATH_TO_FILE, 'a', encoding='utf8') as file:
            file.write(f'{response.title}: {response.url}\n')

    def __iter__(self):
        return self

    def __next__(self):
        self.start_index += 1
        if self.start_index != len(self.description):
            self.write_file()
            return self.name_country
        else:
            raise StopIteration


@logger_path('logsFolder')
def hash_md5(self):
    hash_string = hashlib.md5()
    with open(self, encoding='utf8') as file:
        for string_data in file:
            hash_string.update(string_data.encode())
            yield hash_string.hexdigest()


if __name__ == '__main__':
    with open('countries.json', encoding='utf8') as f:
        data = json.load(f)
    for item in MyIter(data):
        print(item)
    for item in hash_md5(PATH_TO_FILE):
        print(item)
