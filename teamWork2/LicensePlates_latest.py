import random
import unittest

#0
def generate_license_plate_numbers(size) :
    plate_list = []
    while len(plate_list) <  size :
        plate_number = str(chr(random.randint(65, 90))) + str(chr(random.randint(65, 90))) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
        if not (plate_number in plate_list) :
            plate_list.append(plate_number)
    return plate_list
           
#1
def create_database_from_list(list_of_licenses) :
    'Creates a copy of license plate list'
    copy_list = list_of_licenses[:]
    return copy_list

#2
def make_simple_corrections(license):
    '''Makes simple corrections to the license plate number that is given to it.'''
    license_list = list(license)
    i = 0
    while i < len(license_list):
        if license_list[i] == ' ' or license_list[i] == '\t':
            license_list[i : i+1] = []
        else:
            i += 1
    license = ''.join(license_list)
    license = license.upper()
    if len(license) > 4:
        license = change_digits_to_letters(license)
        license = change_letters_to_digits(license)
    else:
        pass
    return license

#3
def change_digits_to_letters(license) :
    'If digits occur where there should be LETTERS, do the conversion'
    letters = ['O', 'I', 'Z', 'B', 'A', 'S', 'G', 'T', 'B', 'P']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    first_two_letters = ''
    for i in range(0, 2) :
        if license[i] in numbers :
            first_two_letters += letters[int(license[i])]
        else :
            first_two_letters += license[i]
    return first_two_letters + license[2:]


#4
def change_letters_to_digits(license):
    '''Converts letters to similar digits.'''
    license_number_list = list(license)
    letter_set = ['A', 'B', 'C', 'D', 'G', 'I', 'O', 'Q', 'S', 'T', 'Z']
    number_set = ['4', '8', '0', '0', '6', '1', '0', '0', '5', '7', '2']
    for i in range(2, 5):
        if license_number_list[i] in letter_set:
            index = letter_set.index(license_number_list[i])
            license_number_list[i] = number_set[index]
        else:
            pass
    return ''.join(license_number_list)


#5
def has_exact_match(license, database) :
    'checks if the database contains this license'
    return (license in database)

#6
def count_nonmatching_characters(string_1, string_2):
    '''Counts the number of characters that are different in the two strings.'''    
    assert len(string_1) == len(string_2)
    count = 0
    for i in range(len(string_1)):
        if string_1[i] == string_2[i]:
            pass
        else:
            count += 1
    return count
    

#7
def count_differences(license_1, license_2) :
    'Returns the number of differences (as defined by the chief of police) in the two license plate numbers.'
    
    if (len(license_1) == len(license_2)) :
        return count_nonmatching_characters(license_1, license_2)
    else :
        if (len(license_1) > len(license_2)) :
            plate1, plate2 = license_1, license_2
        else :
            plate1, plate2 = license_2, license_1

        difference = len(plate2)
        
        ## Remove one digit from the longer number
        for i in range (0,len(plate1)) :
            if i < (len(plate1)-1) :
                trimmed_plate = plate1[ : i] + plate1[i+1 : ]
            else :
                trimmed_plate = plate1[ : i]

            ## count non-matching chars
            count = count_nonmatching_characters(trimmed_plate, plate2)
            if count < difference :
                difference = count  ## update lower non-matching chars

        return difference + 1  



#8
def find_best_match(license, database, max_differences):
    '''Finds possible matching licenses.'''
    if max_differences > 6:# make corrections to max differences
        max_differences = 6
    elif max_differences < 0:
        max_differences = 0
    else:
        pass
    matching_list = []
    for i in range(0, max_differences + 1):
        matching_list.append([])# initialize the matching list
    for i in range(0, len(database)):
        dif_num = count_differences(license, database[i])
        if dif_num <= max_differences:
            matching_list[dif_num].append(database[i])# put the similar plate numbers into matching list
        else:
            pass
    return matching_list


#9
def answer_yes_or_no(question) :
    'Get a response from the user, using the question as a prompt'
    user_input = raw_input(question)
    user_input = user_input.strip() # delete spaces in user_input
    #check responces [yes, y, no, n] or other inputs (requires recursion)
    if (user_input[0] == 'y') or (user_input[0] == 'Y') :
        return True
    elif (user_input[0] == 'n') or (user_input[0] == 'N') :
        return False
    else :
        print "Please anser with 'yes' or 'no'. "
        return answer_yes_or_no(question)


#10
def main():
    '''Creates user interface of the program.'''
    database_original = create_database_from_list(generate_license_plate_numbers(10000))
    database = database_original[:]
    while True:
        license = raw_input('Please input the plate numbers: ')
        license = make_simple_corrections(license)

        ## catch if input plate is shorter than 4 chars OR longer than 6 chars
        while (len(license) < 4) or (len(license) > 6) :
            if len(license) < 4 :
                print 'Your input is shorter than 4 characters. Please Re-enter. '
            if len(license) > 6 :
                print 'Your input is longer than 6 characters. Please Re-enter. '
            license = raw_input('Please input the plate numbers: ')
            license = make_simple_corrections(license)

        
        if has_exact_match(license, database):
            print 'The license plate number exactly matches some number in the database: '
            print license
        else:
            print 'We can\'t find an exactly matching plate! But:'
            best_matches = find_best_match(license, database, 2)
            print 'these are the numbers that differ by one: '
            print best_matches[1],';'
            print 'these are the numbers that differ by two: '
            print best_matches[2],'.'
        answer = answer_yes_or_no('Do you want to enter another license plate number? ')
        if answer:
            pass
        else:
            print 'Done'
            break


### ========= unittest below =========== ###

class TestPlateGenerator(unittest.TestCase):

    #0
    def test_uniqueness(self):
        plates = generate_license_plate_numbers(10000)
        for i in range (1 , len(plates)):
            self.assertNotEqual(plates[0],plates[i])
            

    #1
    def test_create_database_from_list(self) :
        plates = generate_license_plate_numbers(10000)
        copy = create_database_from_list(plates)
        for i in range (0, len(plates)) :
            self.assertEqual(copy[i], plates[i])
            

    #2
    def test_make_simple_corrections(self) :
        self.assertEqual(make_simple_corrections('  3D562 '), 'BD562')
        self.assertEqual(make_simple_corrections(' A888Z '), 'AB882')
        self.assertEqual(make_simple_corrections('93QST'), 'PB057')
        self.assertNotEqual(make_simple_corrections('93QST'), 'PA058')
        self.assertNotEqual(make_simple_corrections('A888Z'), 'KC302')

            
    #3
    def test_change_digits_to_letters(self) :
        plate1 = change_digits_to_letters('5C986')
        plate2 = change_digits_to_letters('T2012')
        plate3 = change_digits_to_letters('94168')
        self.assertEqual(plate1, 'SC986')
        self.assertEqual(plate2, 'TZ012')
        self.assertEqual(plate3, 'PA168')


    #4
    def test_change_letters_to_digits(self) :
        plate1 = change_letters_to_digits('ACC99')
        plate2 = change_letters_to_digits('QZ0Z0')
        plate3 = change_letters_to_digits('ABCDS')
        self.assertEqual(plate1, 'AC099')
        self.assertEqual(plate2, 'QZ020')
        self.assertEqual(plate3, 'AB005')
        

    #5
    def test_has_exact_match(self) :
        plates = generate_license_plate_numbers(10000)
        self.assertTrue(has_exact_match(plates[7362], plates))
        self.assertTrue(has_exact_match(plates[3210], plates))
        self.assertTrue(has_exact_match(plates[9990], plates))


    #6
    def test_count_nonmatching_characters(self) :
        self.assertTrue(count_nonmatching_characters('CX831', 'CA821') == 2)
        self.assertTrue(count_nonmatching_characters('SQ001', 'AQ321') == 3)
        self.assertTrue(count_nonmatching_characters('BA926', 'CA815') == 4)
        
        
    #7
    def test_count_differences(self) :
        self.assertEqual(count_differences('ABC123', 'AB123'), 1)
        self.assertEqual(count_differences('CAB830', 'CB836'), 2)
        self.assertEqual(count_differences('BA926', 'CA815'), 4)
        

    #8
    def test_find_best_match(self) :
        database = ['AA178','AC006','UA838','CA866','CI038','QA076','CO168','BA008','CX830','SQ006']
        result_VX012 = [ [], [], [], [], ['AC006','CI038','QA076','BA008','CX830','SQ006'], ['AA178','UA838','CA866', 'CO168'], []]
        result_CX830 = [['CX830'],[],[],['UA838','CA866','CI038'],['CO168'],['AA178','AC006','QA076','BA008','SQ006'],[]]
        result_QF086 = [[],[],['QA076'],['AC006','SQ006'],['CA866','CI038','BA008'],['AA178','UA838','CO168','CX830'],[]]
        self.assertEqual(find_best_match('VX012', database, 6), result_VX012)
        self.assertEqual(find_best_match('CX830', database, 6), result_CX830)
        self.assertEqual(find_best_match('QF086', database, 6), result_QF086)

    #9 & 10 test mannually.
        


    
                            
##if __name__ == '__main__':
##    unittest.main()
if __name__ == '__main__':
    main()
