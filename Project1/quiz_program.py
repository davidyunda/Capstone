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

    # __str__ should be used to return a basic string representation of an object, you should'nt have logic here
    # use a regular method to ask the questions
    def ask_topic_questions(self):

        # keep track of score here
        total_score = 0 
        #loop in list
        
        for question_and_answer in self.questions:  # avoid single letter variable names - what is 'a' ?  One question and answer? 
            # print(a)
            answer = input(question_and_answer[0])
            #ignore case and check if answer is correct
            if answer.lower() == question_and_answer[1].lower():
                print('Correct!\n')
                total_score += 1
            else:
                print('Sorry, the answer is ' + question_and_answer[1] + '.\n')

        # return f'{self.topic}'  # not needed
        # so you can print the number of correct questions, and if the user got all questions correct 
        print(f'Total correct answers = {total_score}')
        if total_score == len(self.questions):
            print('You got all questions correct!')
            

def main():

    #display welcome message
    print('\nQUIZ PROGRAM\n')

    #create new topic and questions  - set this up first 
    # use more descriptive variable names 
    art_topic = Topic('art')

    # consider storing each question as a dictionary so the data is clearly labeled with the keys
    # it's easy to mix up list indexes. Accessing the data with 
    # example:  { 'question': 'Who painted the Mona Lisa?', 'answer': 'Leonardo Da Vinci' }

    
    art_topic.add(['Who painted the Mona Lisa?', 'Leonardo Da Vinci'])
    art_topic.add(['What precious stone is used to make the artist\'s pigment ultramarine?', 'Lapiz lazuli'])
    art_topic.add(['Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?', 'Chicago'])
    
    space_topic = Topic('space')
    space_topic.add(['Which planet is closest to the sun?', 'Mercury'])
    space_topic.add(['Which planet spins in the opposite direction to all the others in the solar system?', 'Venus'])
    space_topic.add(['How many moons does Mars have?', '2'])

    #all topics save in list 
    # all_topics = ['art','space']
    # or a dictionary - topic string name and Topic objects 
    all_topics = { 'art': art_topic, 'space': space_topic}

    #if the input from the user is not in the list it will ask again
    while True:
        topic = input('Would you like art, or space questions? ')
        # new_list = [['new_topic', 'art'],['new_topic_2', 'space']]
        if topic in all_topics:
            print(topic.upper() + ':\n')
            break
        else:
            print('Enter again\n')

    # now you have a topic and can ask just those questions, look up the Topic in the all_topics dictionary,

    selected_topic_questions_and_answers = all_topics[topic]

    selected_topic_questions_and_answers.ask_topic_questions()

    # The user should be able to choose one topic from the choices 
    # print(new_topic)
    # print(new_topic_2)

main()