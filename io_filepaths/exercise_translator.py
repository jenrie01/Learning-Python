from translate import Translator

with open('filepaths/to_be_translated.txt') as my_file:
    to_be_translated = my_file.read()

translator = Translator(to_lang="ja")
translation = translator.translate(to_be_translated)
with open('filepaths/translated.txt', mode='w') as my_file2:
    my_file2.write(translation)
print(translation)
