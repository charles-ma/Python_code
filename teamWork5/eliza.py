class Eliza(object):
    '''The class that handles the input and output.'''
    def __init__(self):
        '''Functino does the initialization.'''
        self.rules = []

    def hold_conversation(self):
        '''Does the input and output in the method.'''
        rsp = raw_input("Hello! I'm Eliza, Siri's sister. What can I do for you?")
        while not rsp.startswith('goodbye'):
            rsp = raw_input(get_response(rsp))
        return 'See you!'

    def get_response(user_input):
        '''Gets the responses according to the input.'''
        
class Rule(object):
    '''Superclass of all the rules.'''
    def apply(self, string): return string

    def can_apply(self, string): return False

    def is_final(self, string): return False

if __name__ == '__main__':
    eliza = Eliza()
    eliza.hold_conversation()
