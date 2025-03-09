import re

def sentence_finder(string):
    # code copied from textbook, I added digits to the set
    pat = r'[0-9A-Z].*?[.!?](?= [0-9A-Z]|$)'
    sentence_list = re.findall(pat, string, flags=re.DOTALL | re.MULTILINE)

    return sentence_list

def main():
    paragraph = input('Enter a paragraph: ')

    sentence_list = sentence_finder(paragraph)

    if len(sentence_list) == 0:
        print('There are no sentences.')
    else:
        # printing the sentences
        print('There are', len(sentence_list), 'sentences. \nThey are as follows:')

        # loop to print each string in list
        for i in sentence_list:
            print('->', i)


main()