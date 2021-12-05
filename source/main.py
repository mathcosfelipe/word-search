from boyer_moore import boyer_moore
from default import default
from count import count

def main():
    file = input('Inform the file name: ')
    file = open(file, 'r')
    file = (file.readlines())
    word = input('Inform the word: ')
    count_method = count(word, str(file))
    default_method = default(word, str(file))
    boyer_moore_method = boyer_moore(word, str(file))

main()