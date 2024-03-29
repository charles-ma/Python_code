import random

class Eliza(object):
    '''The class that handles the input and output.'''
    def __init__(self):
        '''Function does the initialization.'''
        self.rules = [Do_more_talking_rule(), Speak_too_much_rule(), Question_rule(), Student_rule(), Family_rule(), Negative_emotion_rule(), Positive_emotion_rule(), Greeting_rule(), Opinion_rule(), Pronoun_sub_rule(), Random_answer_rule()]

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
        family_member_keywords = ['father', 'mother', 'sister', 'brother', 'grandpa','grandma', 'grandmother', 'grandfather', 'cousin','family', 'son', 'daughter', 'wife', 'husband']
        for keyword in family_member_keywords:
            if keyword in string.split(): return True
        return False

    def is_final(self, string): return True
    
    def apply(self, string):
        return 'Tell me more about your family.'

class Negative_emotion_rule(Rule):
    '''Rule that would be applied if input contains a negative attitude.'''
    
    neg_keywords = ['unhappy', 'sad', 'grieved', 'heart-broken', 'broken-hearted', 'crocky','depressed', 'sorrowful', 'grievous', 'moanful', 'woeful', 'painful','disappointed', 'bad', 'panic', 'sick', 'uncomfortable', 'upset','annoyed', 'unwell', 'desperate', 'hopeless', 'despaired', 'despondent','sulky', 'angry', 'hungry', 'nervous', 'thirsty', 'bored', 'tired']
    
    def can_apply(self, string):
        for keyword in self.neg_keywords:
            if keyword in string.split(): return True
        return False

    def is_final(self, string): return True

    def apply(self, string):
        for keyword in self.neg_keywords:
            if keyword in string: return "I'm sorry to hear you're " + keyword + '.'

class Positive_emotion_rule(Rule):
    '''Rule that would be applied if input contains a positive attitude.'''
    
    pos_keywords = ['happy', 'glad', 'pleased', 'elated', 'joyful', 'cheerful', 'delighted','excited', 'jovial', 'jocund', 'sanguine', 'lighthearted', 'rejoiced','enjoyable', 'exuberant', 'revelry', 'joyous', 'convivial', 'well','good', 'fine', 'nice', 'energetic', 'lucky', 'hilarious']
    
    def can_apply(self, string):
        for keyword in self.pos_keywords:
            if keyword in string.split(): return True
        return False

    def is_final(self, string): return True

    def apply(self, string):
        for keyword in self.pos_keywords:
            if keyword in string: return "Glad to know that you're feeling " + keyword + '.'

class Opinion_rule(Rule):
    '''Rule that would be applied to give a response to the user's opinions.'''
    
    opinion_keywords = ['i think', 'i feel', 'i like', 'i love', 'i hope', 'i wish','i wonder', 'i remember', 'i want']
    subs_keywords = ['you think', 'you feel', 'you like', 'you love', 'you hope', 'you wish','you wonder', 'you remember', 'you want']
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

    greetings_1 = ['good morning', 'morning', 'good afternoon', 'good night', 'good evening']
    greetings_2 = ['how are you', 'how are you doing', 'how is it going']
    
    def can_apply(self, string):
        for keyword in self.greetings_1 + self.greetings_2:
            if keyword in string.split():
                return True
        return False

    def is_final(self, string): return True

    def apply(self, string):
        for keyword in self.greetings_1:
            if keyword in string.split():
                return keyword.capitalize() + '!'
        for keyword in self.greetings_2:
            if keyword in string.split():
                return 'Fine. ' + string.capitalize() + '!'

class Student_rule(Rule):
    '''Rule that would be applied when something about the campus mentioned.'''

    student_keywords = ['campus', 'study', 'research', 'class', 'learn', 'lab', 'course', 'homework', 'assignment']
    
    def can_apply(self, string):
        for keyword in self.student_keywords:
            if keyword in string.split():
                return True
        return False

    def is_final(self, string): return True

    def apply(self, string):
        return 'Are you a student or a teacher?'

class Pronoun_sub_rule(Rule):
    '''Rule that would be applied to substitue pronouns in the input.'''
    
    pronouns = ['you', 'i', 'me', 'us', 'we', 'your', 'yours', 'my', 'mine', 'our', 'ours', 'yourself', 'yourselves', "myself", 'ourselves']
    corre_pronouns = ['I', 'you', 'you', 'you', 'you', 'my', 'mine', 'your', 'yours', 'your', 'yours', 'myself', 'ourselves', 'yourself', 'yourselves']

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
        string = ' '.join(word_list).capitalize()
        if string[-1].isalpha(): return string + ', why?'
        return string[:-1] + ', why?'

class Random_answer_rule(Rule):
    '''Rule that would be applied when no other rules are suitable.'''
    
    general_purpose_rsp = ['Tell me more about that.', 'Just give me additional information about that.', 'In what way?', 'Why is that?', 'So what do you want me to do with that?','Can you give me a specific example?', "I'm not really sure what you mean.",'Well, do you have more opinions?', 'How do you like that?']
    
    def apply(self, string): return random.choice(self.general_purpose_rsp)

if __name__ == '__main__':
    Eliza().hold_conversation()
