other_symbols = [',', '.', '=', '!',
                 '?', ';', ':',]


class WordsFinder:

    def __init__(self, *file_names):

        self.file_names = list(file_names)

    def get_all_words(self):

        all_words = dict()

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                list_words = list()
                for line in file:
                    for word in line.lower().split():
                        change_word = str()
                        for chars in word:
                            if chars not in other_symbols:
                                change_word += chars
                        else:
                            list_words.append(change_word)
                all_words.update({file_name: list_words})

        return all_words

    def find(self, word):

        result_search = dict()

        for file_name, list_words in self.get_all_words().items():
            if word.lower() in list_words:
                result_search.update(
                    {file_name: list_words.index(word.lower()) + 1}
                )
            else:
                result_search.update(
                    {file_name: f'Слово "{word} не найдено"'}
                )

        return result_search

    def count(self, word):

        result_search = dict()

        for file_name, list_words in self.get_all_words().items():
            if word.lower() in list_words:
                result_search.update(
                    {file_name: list_words.count(word.lower())}
                )
            else:
                result_search.update(
                    {file_name: f'Слово "{word}" не найдено'}
                )

        return result_search


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))

# finder1 = WordsFinder('Rudyard Kipling - If.txt',)
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))

# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))