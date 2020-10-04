from sys import getsizeof


def analise_text(path_to_text):
    with open(path_to_text, 'r') as text:
        char_dictionary = {}
        word_dictionary = {}
        string_from_text = text.readline().replace('\n', '')
        while string_from_text != '':                                  # цикл, который прокручивает каждую строку текста
            for number_of_char in range(len(string_from_text)):        # цикл, составляющий алфавит текста
                char = {string_from_text[number_of_char] : 0}
                char_dictionary.update(char)
            words_from_line = string_from_text.split(' ')
            for number_of_word in range(len(words_from_line)):         # цикл, заполняющий словарь словами текста
                word = {words_from_line[number_of_word]: 0}
                word_dictionary.update(word)
            string_from_text = text.readline().replace('\n', '')
    with open(path_to_text, 'r') as text:
        quantity_of_words = 0;
        string_from_text = text.readline().replace('\n', '')
        while string_from_text != '':                                   # цикл, который прокручивает каждую строку текста
            quantity_of_words += len(words_from_line)
            for number_of_char in range(len(string_from_text)):         # цикл, считающий буквы
                char = string_from_text[number_of_char]
                char_dictionary[char] += 1
            words_from_line = string_from_text.split(' ')
            for number_of_word in range(len(words_from_line)):          # цикл, считающий слова
                word = words_from_line[number_of_word]
                word_dictionary[word] += 1
            string_from_text = text.readline().replace('\n', '')
    for key in word_dictionary:
        if word_dictionary[key] == max(word_dictionary.values()):
            often_word = key
    for key in char_dictionary:
        if char_dictionary[key] == max(char_dictionary.values()):
            often_char = key

    return often_word, often_char, max(char_dictionary.values())/quantity_of_words




dictionary = {}
previous_size = getsizeof(dictionary)
for i in range(2000):
    dictionary[i] = i
    if previous_size != getsizeof(dictionary):
        print(previous_size*8, ' - минимальный объем памяти для словаря с ', i, ' элементами')
    previous_size = getsizeof(dictionary)
print(analise_text('text.txt'))