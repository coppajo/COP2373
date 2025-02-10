#import regular expressions for the findall function
import re

def email_scanner(input):
    #initializing variables
    spam_score = 0
    found_words = []

    #list of flag words and phrases
    flag_words = [
        '100% satisfied',
        'Big bucks',
        'Double your cash',
        'Double your income',
        'Extra cash',
        'Fast cash',
        'Limited time',
        'Once in a lifetime',
        'Guaranteed',
        'Free',
        'Special promotion',
        'Now',
        'What are you waiting for?',
        'Spam',
        'Deal',
        'Not junk',
        'Pre-approved',
        'Cheap',
        'Bonus',
        'Compare rates',
        'Join millions',
        'Offer',
        'Terms and conditions',
        'Work from home',
        'Social security number',
        'No questions asked',
        'No purchase necessary',
        'No hidden',
        'Congratulations',
        'Cure'
    ]

    #loop to check input for each flag word/phrase
    for i in flag_words:

        #findall creates a list with each repeated instance of the word
        word_count = re.findall(i.lower(), input.lower())


        #the length of the list is the amount of times the word/phrase appears
        if len(word_count) == 0:
            continue #goes to next iteration
        else:
            spam_score += len(word_count)
            found_words.append(i)

    return spam_score, found_words


def main():
    email = input("Enter an email message: ")

    #get spam score and words found inside the email from the email scanner function
    spam_score, found_words = email_scanner(email)

    #risk level based off spam score
    if spam_score < 2:
        risk_level = "low risk"
    elif spam_score < 5:
        risk_level = "light risk"
    elif spam_score < 8:
        risk_level = "medium risk"
    else:
        risk_level = 'high risk'

    #display info
    print(f"The email has {risk_level} of being spam.")
    print(f"The email's spam score is {spam_score}")
    print(f"The word(s) and/or phrase(s) that triggered the scanner: ")
    print(*found_words, sep=', ')


main()