""" A quiz program. """
"This program asks the user for input and then it decides if the answer entered was correct "
"if not it will display a message with the right answer."

class Topic:

    def __init__(self, topic):
        self.topic = topic          
        self.questions = []
        
    #add question to list
    def add(self, question):
        self.questions.append(question)

    def __str__(self):
        #loop in list
        for a in self.questions:
            # print(a)
            answer = input(a[0])
            #ignore case and check if answer is correct
            if answer.lower() == a[1].lower():
                print('Correct!\n')
            else:
                print('Sorry, the answer is ' + a[1] + '.\n')

        return f'{self.topic}'

def main():

    #display welcome message
    print('\nQUIZ PROGRAM\n')

    #all topics save in list
    all_topics = ['art','space']

    #if the input from the user is not in the list it will ask again
    while True:
        topic = input('Would you like art, or space questions? ')
        # new_list = [['new_topic', 'art'],['new_topic_2', 'space']]
        if topic in all_topics:
            print(topic.upper() + ':\n')
            break
        else:
            print('Enter again\n')

    #create new topic and questions 
    new_topic = Topic('art')
    new_topic.add(['Who painted the Mona Lisa?', 'Leonardo Da Vinci'])
    new_topic.add(['What precious stone is used to make the artist\'s pigment ultramarine?', 'Lapiz lazuli'])
    new_topic.add(['Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?', 'Chicago'])
    
    new_topic_2 = Topic('space')
    new_topic_2.add(['Which planet is closest to the sun?', 'Mercury'])
    new_topic_2.add(['Which planet spins in the opposite direction to all the others in the solar system?', 'Venus'])
    new_topic_2.add(['How many moons does Mars have?', '2'])
    
    print(new_topic)
    print(new_topic_2)

main()