import random

class Eliza(object):
    '''The class that handles the input and output.'''
    def __init__(self):
        '''Function does the initialization.'''
        family_rule = Family_rule()
        do_more_talking_rule = Do_more_talking_rule()
        speak_too_much_rule = Speak_too_much_rule()
        pathetic_rule = Pathetic_rule()
        happy_rule = Happy_rule()
        ask_how_rule = Ask_how_rule()
        ask_why_rule = Ask_why_rule()
        greeting_rule = Greeting_rule()
        random_answer_rule = Random_answer_rule()
        self.rules = [family_rule, do_more_talking_rule, speak_too_much_rule, pathetic_rule, happy_rule, ask_how_rule, ask_why_rule,greeting_rule, random_answer_rule]

    def hold_conversation(self):
        '''Method does the input and output.'''
        rsp = raw_input("Hello! I'm Eliza, Siri's sister. How\'s it going?\n") 
        while not rsp.lower().startswith('goodbye'):
            rsp = raw_input(self.get_response(rsp.lower()) + '\n')
        print 'See you!'
        return None

    def get_response(self, user_input):
        '''Gets the responses according to the input.'''
        possible_rules = []
        for rule in self.rules:
            if rule.can_apply(user_input):
                possible_rules.append(rule)
                if rule.is_final(user_input):
                    return rule.apply(user_input)
            else:
                pass
        random_num = random.randint(0, 4*len(possible_rules) - 4)
        rule = possible_rules[random_num / 4]
        reply = rule.apply(user_input)
        return reply
        
class Rule(object):
    '''Superclass of all the rules.'''
    def apply(self, string): return string

    def can_apply(self, string): return False

    def is_final(self, string): return False

class Family_rule(Rule):
    '''Rule that would be applied if keyword involving family has been found.'''
    def can_apply(self, string):
        family_members = ['father', 'mother', 'sister', 'brother', 'grandpa', 'grandma', 'grandmother', 'grandfather', 'cousin']
        for member in family_members:
            if member in string: return True
        return False
    
    def apply(self, string):
             return 'Tell me more about your family.'

class Do_more_talking_rule(Rule):
    '''Rule that would be applied if input is too short.'''
    def can_apply(self, string):
        if len(string) <= 5: return True
        return False

    def apply(self, string):
             return "Don't be shy! Just talk more to me."

class Speak_too_much_rule(Rule):
    '''Rule that would be applied if input is too long.'''
    def can_apply(self, string):
        if len(string) >= 160: return True
        return False

    def apply(self, string):
             return "You speak too much. I can't really understand!"
    
class Pathetic_rule(Rule):
    '''Rule that would be applied if input contains some sad words.'''
    def can_apply(self, string):
        sad_words = ['sad', 'unhappy', 'upset', 'grieved', 'heart broken', 'painful', 'crocky']
        for sad_word in sad_words:
            if sad_word in string:
                return True
            else:
                pass
        return False

    def apply(self, string):
        return 'I am sorry to hear that.'

class Happy_rule(Rule):
    '''Rule that would be applied if input contains some happy words.'''
    def can_apply(self, string):
        happy_words = ['happy', 'glad', 'excited', 'lucky', 'hilarious', 'cheerful']
        for happy_word in happy_words:
            if happy_word in string:
                return True
            else:
                pass
        return False

    def apply(self, string):
        return 'I am glad to hear that!'

class Ask_why_rule(Rule):
    '''Rule that would be applied when the input states some facts about the user itself.'''
    def can_apply(self, string):
        word_list = string.split()
        if word_list[0].lower() == 'i' and word_list[1].lower() != 'don\'t' and word_list[1].lower() != 'do':
            return True
        else:
            return False

    def apply(self, string):
        word_list = string.split()
        if word_list[-1] == '.':
            word_list = word_list[0 : len(word_list) - 1]
        word_list = word_list[1 :]
        return 'Why do you ' + ' '.join(word_list) + '?'

class Ask_how_rule(Rule):
    '''Rule that would be applied when the user wants to do something.'''
    def can_apply(self, string):
        if string.lower().startswith('i want to'):
            return True
        else:
            pass
        return False

    def apply(self, string):
        word_list = string.split()
        if word_list[-1] == '.':
            word_list = word_list[0 : len(word_list) - 1]
        word_list = word_list[3 :]
        return 'How will you ' + ' '.join(word_list) + '?'

class Random_answer_rule(Rule):
    '''Rule that would be applied when no other rules are suitable.'''
    def can_apply(self, string):
        return True

    def apply(self, string):
        random_answers = ['Tell me more about it!', 'Go on...', 'Really?']
        random_num = random.randint(0, 2)
        return random_answers[random_num]

class Greeting_rule(Rule):
    '''Rule that would be applied when the user greets our Eliza.'''
    def can_apply(self, string):
        self.greetings_1 = ['good morning', 'morning', 'good afternoon', 'good night']
        self.greetings_2 = ['how are you?', 'how are you doing?', 'how is it going?']
        if string.lower() in self.greetings_1 or string.lower() in self.greetings_2:
            return True
        else:
            pass
        return False

    def apply(self, string):
        if string.lower() in self.greetings_1:
            return string
        else:
            return 'Fine, ' + string

    def is_final(self, string):
        return True

if __name__ == '__main__':
    eliza = Eliza()
    eliza.hold_conversation()
