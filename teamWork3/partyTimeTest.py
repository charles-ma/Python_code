import unittest
import partyTime

class test_party_time(unittest.TestCase):
    
    def test_gene(self):
        relation_list = partyTime.random_relation(100)
        self.assertEqual(100, len(partyTime.gene_sets(relation_list)))
    
    def test_sort(self):
        relation_list = partyTime.random_relation(100)
        set_dic = partyTime.gene_sets(relation_list)
        key_list = partyTime.sort_sets(set_dic)
        max_item = set_dic[key_list[0]]
        min_item = set_dic[key_list[-1]]
        self.assertTrue(len(max_item) > len(min_item))
        
    def test_calculate(self):
        relation_list = partyTime.random_relation(100)
        self.assertTrue(len(partyTime.calculate(relation_list)) <= 100)

    def test_cons_2(self):
        relation_list = partyTime.random_relation(100)
        self.assertTrue(len(partyTime.cons_2(relation_list)) != 0)

    def test_solve_1(self):
        self.assertIsNone(partyTime.solve_1('nameInfo.txt'))

    def test_solve_2(self):
        self.assertIsNone(partyTime.solve_2('nameInfo.txt'))


if __name__ == '__main__':
    unittest.main()
