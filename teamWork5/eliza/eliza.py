import random
#code by Chao Ma and Zhishen Wen

class Eliza(object):
    '''The class that handles the input and output.'''
    def __init__(self):
        '''Function does the initialization.'''
        self.rules = [Do_more_talking_rule(), Speak_too_much_rule(), Question_rule(),
                      Student_rule(), Family_rule(), Negative_emotion_rule(),
                      Positive_emotion_rule(), Keyword_rule(), Greeting_rule(),
                      Opinion_rule(), Pronoun_sub_rule(), Random_answer_rule()]

    def hold_conversation(self):
        '''Method does the input and output.'''
        rsp = raw_input("Hello! I'm Eliza, Siri's sister. How\'s it going?\n") 
        while not rsp.lower().startswith('goodbye'):
            rsp = raw_input(self.get_response(rsp.lower()) + '\n')
        print 'See you!'
        return None

    def get_response(self, user_input):
        '''Gets the responses according to the input.'''
        shuffled_rules = self.rules[:-3]
        random.shuffle(shuffled_rules)
        shuffled_rules += self.rules[-3:]
        possible_rules = []
        for rule in shuffled_rules:
            if rule.can_apply(user_input):
                if rule.is_final(user_input):
                    return rule.apply(user_input)
                possible_rules.append(rule)
        if len(possible_rules) == 1:
            return possible_rules[0].apply(user_input)
        elif len(possible_rules) == 2:
            user_input = Pronoun_sub_rule().apply(user_input)
            return Opinion_rule().apply(user_input.lower())
        else:
            return Random_answer_rule().apply(user_input)
        
class Rule(object):
    '''Superclass of all the rules.'''
    def apply(self, string): return string

    def can_apply(self, string): return False

    def is_final(self, string): return False

class Do_more_talking_rule(Rule):
    '''Rule that would be applied if input is too short.'''
    
    def can_apply(self, string):
        if len(string) <= 5: return True
        return False
    
    def is_final(self, string): return True

    def apply(self, string):
        return "Don't be shy! Just talk more to me."

class Speak_too_much_rule(Rule):
    '''Rule that would be applied if input is too long.'''
    
    def can_apply(self, string):
        if len(string) >= 160: return True
        return False

    def is_final(self, string): return True

    def apply(self, string):
        return "You speak too much. I can't really understand!"
    
class Question_rule(Rule):
    '''Rule that would be applied if input is a question.'''
    
    def can_apply(self, string):
        if string[-1] == '?': return True
        return False

    def is_final(self, string): return True

    def apply(self, string):
        return "Why do you want to know that?"

class Family_rule(Rule):
    '''Rule that would be applied if keyword involving family has been found.'''
    
    def can_apply(self, string):
        family_member_keywords = ['father', 'mother', 'sister', 'brother',
                                  'grandpa','grandma', 'grandmother', 'grandfather',
                                  'cousin','family', 'son', 'daughter', 'wife', 'husband']
        for keyword in family_member_keywords:
            if keyword in string.split(): return True
        return False

    def is_final(self, string): return True
    
    def apply(self, string):
        return 'Tell me more about your family.'

class Negative_emotion_rule(Rule):
    '''Rule that would be applied if input contains a negative attitude.'''
    
    neg_keywords = ['unhappy', 'sad', 'grieved', 'heart-broken', 'broken-hearted',
                    'crocky','depressed', 'sorrowful', 'grievous', 'moanful', 'woeful',
                    'painful','disappointed', 'bad', 'panic', 'sick', 'uncomfortable',
                    'upset','annoyed', 'unwell', 'desperate', 'hopeless', 'despaired',
                    'despondent','sulky', 'angry', 'hungry', 'nervous', 'thirsty',
                    'bored', 'tired', 'embarrassed']
    responses = ["I'm sorry to hear you're ", 'Do you think coming here will help you not to be too ',
                 'Why do you think you are ', 'It seems not good. Why you feel ', 'Please let me know why you\'re']

    def can_apply(self, string):
        for keyword in self.neg_keywords:
            if keyword in string.split(): return True
        return False

    def is_final(self, string): return True

    def apply(self, string):
        for keyword in self.neg_keywords:
            if keyword in string: return random.choice(self.responses) + keyword + '.'

class Positive_emotion_rule(Rule):
    '''Rule that would be applied if input contains a positive attitude.'''
    
    pos_keywords = ['happy', 'glad', 'pleased', 'elated', 'joyful', 'cheerful',
                    'delighted','excited', 'jovial', 'jocund', 'sanguine', 'lighthearted',
                    'rejoiced','enjoyable', 'exuberant', 'revelry', 'joyous', 'convivial',
                    'well','good', 'fine', 'nice', 'energetic', 'lucky', 'hilarious']
    responses = ["Glad to know that you're feeling ", 'I think that coming here will let you feel even more ',
                 'Why do you think you are ', 'Seems great! I always want to become ',
                 'I feel like I\'ll become happy if you feel ']
    
    def can_apply(self, string):
        for keyword in self.pos_keywords:
            if keyword in string.split(): return True
        return False

    def is_final(self, string): return True

    def apply(self, string):
        for keyword in self.pos_keywords:
            if keyword in string: return random.choice(self.responses) + keyword + '.'

class Opinion_rule(Rule):
    '''Rule that would be applied to give a response to the user's opinions.'''
    
    opinion_keywords = ['i think', 'i feel', 'i like', 'i love', 'i hope', 'i wish',
                        'i wonder', 'i remember', 'i want', 'i believe']
    subs_keywords = ['you think', 'you feel', 'you like', 'you love', 'you hope',
                     'you wish','you wonder', 'you remember', 'you want']
    responses = ['What let you think ', 'Why would you consider ', 'How can you think ']
    
    def can_apply(self, string):
        for keyword in self.opinion_keywords:
            if keyword in string: return True
        return False

    def apply(self, string):
        for keyword in self.subs_keywords:
            if keyword in string: i = string.find(keyword) + len(keyword) + 1
        if string[i : i + 3] == 'to ':
            return random.choice(self.responses) + string[i:] + '?'
        return random.choice(self.responses) + 'of ' + string[i:] + '?'

class Greeting_rule(Rule):
    '''Rule that would be applied when the user greets our Eliza.'''

    greetings_1 = ['good morning', 'morning', 'good afternoon', 'good night',
                   'good evening', 'nice to meet you']
    greetings_2 = ['how are you', 'how are you doing', 'how is it going']
    
    def can_apply(self, string):
        for keyword in self.greetings_1 + self.greetings_2:
            if keyword in string:
                return True
        return False

    def is_final(self, string): return True

    def apply(self, string):
        for keyword in self.greetings_1:
            if keyword in string:
                return keyword.capitalize() + '!'
        for keyword in self.greetings_2:
            if keyword in string:
                return 'Not too bad. ' + string.capitalize() + '!'

class Student_rule(Rule):
    '''Rule that would be applied when something about the campus mentioned.'''

    student_keywords = ['campus', 'study', 'research', 'class', 'learn', 'lab',
                        'course', 'homework', 'assignment', 'course']
    
    def can_apply(self, string):
        for keyword in self.student_keywords:
            if keyword in string.split():
                return True
        return False

    def is_final(self, string): return True

    def apply(self, string):
        return 'Are you a student or a teacher?'

class Keyword_rule(Rule):
    '''Rule that would be applied when specific keywords mentioned.'''

    special_keywords = ['love', 'life', 'career', 'python', 'programming', 'computer',
                        'money', 'transportation', 'power', 'world', 'politics', 'war',
                        'peace', 'security', 'travel', 'dream', 'business', 'health',
                        'science', 'technology', 'entertainment', 'woman', 'girl']
    responses = [' is not always simple!', ' is different now from the past.',
                 ' is something people never feel bored with. Right?',
                 ' is what people are often curious to get familiar with.',
                 ' should be interesting!', ' seems to be a lot of fun I think.']
    
    def can_apply(self, string):
        for keyword in self.special_keywords:
            if keyword in string.split():
                return True
        return False

    def is_final(self, string): return True

    def apply(self, string):
        for keyword in self.special_keywords:
            if keyword in string: return keyword + random.choice(self.responses)

class Pronoun_sub_rule(Rule):
    '''Rule that would be applied to substitue pronouns in the input.'''
    
    pronouns = ['you', 'i', 'me', 'us', 'we', 'your', 'yours', 'my', 'mine',
                'our', 'ours', 'yourself', 'yourselves', 'myself', 'ourselves',
                'you\'re', 'i\'m']
    corre_pronouns = ['I', 'you', 'you', 'you', 'you', 'my', 'mine', 'your',
                      'yours', 'your', 'yours', 'myself', 'ourselves', 'yourself',
                      'yourselves', 'I am', 'you are']
    pronouns_2 = ['i are', 'i were', 'you am', 'you was']
    corre_pronouns_2 = ['I am', 'I was', 'you are', 'you were']

    def can_apply(self, string):
        for pronoun in self.pronouns:
            if pronoun in string.split():
                return True
        return False

    def apply(self, string):
        word_list = string.split()
        for i in range(0, len(word_list)):
            if word_list[i] in self.pronouns:
                word_list[i] = self.corre_pronouns[self.pronouns.index(word_list[i])]
        string = ' '.join(word_list)
        for word in self.pronouns_2:
            if word in string:
                string = string.replace(word, self.corre_pronouns_2[self.pronouns_2.index(word)])
        if string[-1].isalpha(): return string.capitalize() + ', why?'
        return string[:-1].capitalize() + ', why?'

class Random_answer_rule(Rule):
    '''Rule that would be applied when no other rules are suitable.'''
    
    general_purpose_rsp = ['Tell me more about that.', 'In what way?',
                           'Just give me additional information about that.',
                           'Why is that?', 'So what do you want me to do with that?',
                           'Can you give me a specific example?',
                           "I'm not really sure what you mean.", "Why do you say so?",
                           'Well, do you have more opinions?', 'How do you like that?']
    
    def apply(self, string): return random.choice(self.general_purpose_rsp)

if __name__ == '__main__':
    Eliza().hold_conversation()
