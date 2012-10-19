import unittest
from eliza import *  #have to change this name at the end
#code by Chao Ma and Zhishen Wen

class eliza_test(unittest.TestCase):
    def test_rule(self):
        rule = Rule()
        string = 'test string'
        self.assertEqual(False, rule.can_apply(string))
        self.assertEqual(string, rule.apply(string))
        self.assertEqual(False, rule.is_final(string))

    def test_do_more_talking_rule(self):
        string1 = '123456'
        string2 = '123'
        rule = Do_more_talking_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(True, rule.is_final(string1))
        self.assertEqual('Don\'t be shy! Just talk more to me.', rule.apply(string2))

    def test_speak_too_much_rule(self):
        string1 = '123'
        string2 = ''
        for i in range(0, 161):
            string2 = string2 + 'a'
        rule = Speak_too_much_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(True, rule.is_final(string1))
        self.assertEqual('You speak too much. I can\'t really understand!', rule.apply(string2))

    def test_question_rule(self):
        string1 = '123'
        string2 = '123?'
        rule = Question_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(True, rule.is_final(string1))
        self.assertEqual('Why do you want to know that?', rule.apply(string2))

    def test_family_rule(self):
        string1 = 'I love her.'
        string2 = 'I love my mother .'
        rule = Family_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(True, rule.is_final(string1))
        self.assertEqual('Tell me more about your family.', rule.apply(string2))

    def test_negative_emotion_rule(self):
        string1 = '123'
        string2 = 'I feel sad today.'
        rule = Negative_emotion_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(True, rule.is_final(string1))

    def test_positive_emotion_rule(self):
        string1 = '123'
        string2 = 'I am glad today.'
        rule = Positive_emotion_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(True, rule.is_final(string1))
        
    def test_opinion_rule(self):
        string1 = '123'
        string2 = 'i think you should help me.'
        rule = Opinion_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(False, rule.is_final(string1))

    def test_greeting_rule(self):
        string1 = '123'
        string2 = 'how are you doing'
        rule = Greeting_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(True, rule.is_final(string1))
        self.assertEqual('Not too bad. How are you doing!', rule.apply(string2))

    def test_student_rule(self):
        string1 = '123'
        string2 = 'I study chemistry at Penn.'
        rule = Student_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(True, rule.is_final(string1))
        self.assertEqual('Are you a student or a teacher?', rule.apply(string2))

    def test_pronoun_sub_rule(self):
        string1 = '123'
        string2 = 'My father made me come to see you!'
        rule = Pronoun_sub_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(False, rule.is_final(string1))
        self.assertEqual('My father made you come to see you, why?', rule.apply(string2))

    def test_keyword_rule(self):
        string1 = '123'
        string2 = 'People always like money and power.'
        rule = Keyword_rule()
        self.assertEqual(True, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(True, rule.is_final(string1))

    def test_random_answer_rule(self):
        string1 = '123'
        string2 = 'People always cheat themselves to avoid being laughed at.'
        rule = Random_answer_rule()
        self.assertEqual(False, rule.can_apply(string2))
        self.assertEqual(False, rule.can_apply(string1))
        self.assertEqual(False, rule.is_final(string1))
        self.assertTrue(rule.apply(string2) in rule.general_purpose_rsp)

if __name__ == '__main__':
    unittest.main()
