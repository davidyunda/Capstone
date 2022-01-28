"""Camelcase converter program! """

def camelcase (sentence):
    """Convert sentence to camelCase, for example, "Display all books" 
    is converted to "displayAllBooks"  """
    title_case = sentence.title()  #uppercase first letter of each word
    upper_camel_cased = title_case.replace(' ','') #remove spaces
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def banner():
    """Display program name, using statrs"""
    message = 'Awesome camelcase program'
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars}\n')

def instructions():
    """Display instructions for how to use the program """
    print('Enter a sentence and this program will convert it to camelcase.')

def main():
    banner()
    instructions()
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()
    