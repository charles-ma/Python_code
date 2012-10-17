import unittest
from eliza import *  #have to change this name at the end

class eliza_test(unittest.TestCase):
    def test_rule(self):
        rule = Rule()
        string = 'test string'
        self.assertEqual(False, rule.can_apply(string))
        self.assertEqual(string, rule.apply(string))
        self.assertEqual(False, rule.is_final(string))

    def test_do_more_talking(self):
        string1 = '123456'
        string2 = '123'
        rule = Do_more_talking_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(True, rule.is_final(string1))
        self.assertEqual('Don\'t be shy! Just talk more to me.', rule.apply(string2))

    def test_speak_too_much(self):
        string1 = '123'
        string2 = ''
        for i in range(0, 161):
            string2 = string2 + 'a'
        rule = Speak_too_much_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(True, rule.is_final(string1))
        self.assertEqual('You speak too much. I can\'t really understand!', rule.apply(string2))

    def test_question(self):
        string1 = '123'
        string2 = '123?'
        rule = Question_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(True, rule.is_final(string1))
        self.assertEqual('Why do you want to know that?', rule.apply(string2))

    def test_family(self):
        string1 = 'I love her.'
        string2 = 'I love my mother .'
        rule = Family_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(True, rule.is_final(string1))
        self.assertEqual('Tell me more about your family.', rule.apply(string2))

    def test_negative_emotion(self):
        string1 = '123'
        string2 = 'I feel sad today.'
        rule = Negative_emotion_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(True, rule.is_final(string1))
        self.assertEqual('I\'m sorry to hear you\'re sad.', rule.apply(string2))

    def test_positive_emotion(self):
        string1 = '123'
        string2 = 'I am glad today.'
        rule = Positive_emotion_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(True, rule.is_final(string1))
        self.assertEqual('Glad to know that you\'re feeling glad.', rule.apply(string2))


if __name__ == '__main__':
    unittest.main()
