mem = 0 #global variable mem used as memory of the calculator

def to_decimal(ndn):
    '''Turns a negadecimal number into decimal.'''
##    negadecimal = eval(ndn)
##    #get the digits of the negadecimal input
##    digits = []
##    while negadecimal > 0:
##        digit = negadecimal % 10
##        digits.append(digit)
##        negadecimal = negadecimal / 10
##    #'%' and '/' are a pair of operators, '%' gets the remainder while '/' gets the quotient
##    #use the digits to form the decimal resulit
##    decimal = 0
##    for i in range(0, len(digits)):
##        decimal += digits[i] * ((-10) ** i)
    decimal = 0
    p = len(ndn) - 1
    for i in ndn:
        decimal += eval(i) * ((-10)**p)
        p -= 1
    return decimal
        
def to_negadecimal(dec):
    '''Turns a decimal number into negadecimal.'''
    #get the negadecimal digits of the decimal input 
    digits = []
    while abs(dec) > 0:
        digit = dec % 10
        digits.append(digit)
        dec = - (dec / 10)
    #use the digits to form the negadecimal result
    negadecimal = 0
    for i in range(0, len(digits)):
        negadecimal += digits[i] * ((10) ** i)
    return str(negadecimal)

def int_check(decimal):#not used!!!!!!!
    '''Checks whether the input is an integer.'''
    if not isinstance(decimal, int):
        raise Exception, 'Wrong data type detected!'
    else:
        pass

def sign_check(negadecimal):#not used!!!!!!!
    '''Checks whether the input is a negative integer'''
    if negadecimal < 0:
        raise Exception, "'-' before a decimal number detected!"
    else:
        pass
    
def add(ndn_1, ndn_2):
    '''Calculates ndn_1 + ndn_2 and store the result in mem'''
    dn_1 = to_decimal(ndn_1)
    dn_2 = to_decimal(ndn_2)
    dn_sum = dn_1 + dn_2
    ndn_sum = to_negadecimal(dn_sum)
    store(ndn_sum)
    return ndn_sum

def subtract(ndn_1, ndn_2):
    '''Calculates ndn_1 - ndn_2 and store the result in mem'''
    dn_1 = to_decimal(ndn_1)
    dn_2 = to_decimal(ndn_2)
    dn_dif = dn_1 - dn_2
    ndn_dif = to_negadecimal(dn_dif)
    store(ndn_dif)
    return ndn_dif

def multiply(ndn_1, ndn_2):
    '''Calculates ndn_1 * ndn_2 and store the result in mem'''
    dn_1 = to_decimal(ndn_1)
    dn_2 = to_decimal(ndn_2)
    dn_product = dn_1 * dn_2
    ndn_product = to_negadecimal(dn_product)
    store(ndn_product)
    return ndn_product

def divide(ndn_1, ndn_2):
    '''Calcualtes ndn_1 / ndn_2 and store the result in mem'''
    dn_1 = to_decimal(ndn_1)
    dn_2 = to_decimal(ndn_2)
    dn_quotient = dn_1 / dn_2
    ndn_quotient = to_negadecimal(dn_quotient)
    store(ndn_quotient)
    return ndn_quotient

def remainder(ndn_1, ndn_2):
    '''Calculates ndn_1 % ndn_2 and store the result in mem'''
    dn_1 = to_decimal(ndn_1)
    dn_2 = to_decimal(ndn_2)
    dn_remainder = dn_1 % dn_2
    ndn_remainder = to_negadecimal(dn_remainder)
    store(ndn_remainder)
    return ndn_remainder

def negate(negadecimal):
    '''Returns the number added to the input resulting in 0.'''
    neg = subtract('0', negadecimal)
    store(neg)
    return neg

def store(ndn):
    '''Stores a value into the global variable mem.'''
    global mem
    mem = ndn

def fetch():
    '''Gets the value of the global variable mem.'''
    return mem

def REPL():
    start = True
    while start == True:
        expression = raw_input('Compute:')
        result = evaluate(expression)
        if result == 'Error':
            print 'I don\'t understand:' + expression
        elif result == 'Divided by 0!':
            print 'You cannot divide a number by 0!'
        elif result == 'Quit':
            print 'Done'
            start = False
        else:
            print result

def evaluate(string):
    '''Evaluates user input.'''
    str_list = list(string)
    return explain(str_list)
    

def remove_blank(str_list):
    '''Removes the blanks in the list.'''
    i = 0
    while i < len(str_list):
        if str_list[i] == ' ' or str_list[i] == '\t':
            str_list[i : i+1] = []
        else:
            i += 1
    return str_list

def has_operator(str_list):
    '''Decides whether the input contains one operator and which it is.'''
    operator_num = 0
    operator = ''
    operators = ['+', '-', '*', '/', '%']
    for i in str_list:
        if i in operators:
            operator_num += 1
            operator = i
        else:
            pass
    if operator_num == 0:
        return 0
    elif operator_num == 1:
        return operator
    else:
        return None

def has_command(str_list):
    '''Decides whether the input has any commands such as dec, neg and quit.'''
    if str_list[0 : 3] == ['d', 'e', 'c'] or str_list[0 : 3] == ['n', 'e', 'g']:
        return ''.join(str_list[0 : 3])
    elif str_list[0 : 4] == ['q', 'u', 'i', 't']:
        return ''.join(str_list[0 : 4])
    else:
        return None
    
def explain(str_list):
    '''Explain the meaning of the input.'''
    remove_blank(str_list)
    if has_operator(str_list) == None:
        return 'Error'
    elif has_operator(str_list) == '+':
        return eval_operator(str_list, '+')
    elif has_operator(str_list) == '-':
        i = str_list.index('-')
        if ''.join(str_list[: i]) == 'neg':
            return eval_command(str_list, 'neg')
        elif ''.join(str_list[: i]) == 'dec':
            return 'Error'
        else:
            return eval_operator(str_list, '-')
    elif has_operator(str_list) == '*':
        return eval_operator(str_list, '*')
    elif has_operator(str_list) == '/':
        return eval_operator(str_list, '/')
    elif has_operator(str_list) == '%':
        return eval_operator(str_list, '%')
    elif has_operator(str_list) == 0:
        if has_command(str_list) == 'dec':
            return eval_command(str_list, 'dec')
        elif has_command(str_list) == 'neg':
            return eval_command(str_list, 'neg')
        elif has_command(str_list) == 'quit':
            return eval_command(str_list, 'quit')
        else:
            return 'Error'
    else:
        return 'Error'
        
def eval_operator(str_list, operator):
    '''Evaluates input with "+".'''
    operator_pos = str_list.index(operator)
    if operator_pos == len(str_list) - 1:
        return 'Error'
    else:
        operand_1 = parse_operand(str_list[: operator_pos])
        operand_2 = parse_operand(str_list[operator_pos + 1 :])
        if operand_1 == None:
            if operand_2 != None and operator == '-':
                    return negate(operand_2)
            else:
                return 'Error'
        elif operand_2 != None:
            if operator == '+': 
                return add(operand_1, operand_2)
            elif operator == '-':
                return subtract(operand_1, operand_2)
            elif operator == '*':
                return multiply(operand_1, operand_2)
            elif operator == '/':
                if eval(operand_2) != 0:
                    return divide(operand_1, operand_2)
                else:
                    return 'Divided by 0!'
            elif operator == '%':
                if eval(operand_2) != 0:
                    return remainder(operand_1, operand_2)
                else:
                    return 'Divided by 0!'
            else:
                return 'Error'
        
def eval_command(str_list, command):
    if command == 'dec':
        operand = parse_operand(str_list[3 :])
        if operand != None:
            return to_decimal(operand)
        else:
            return 'Error'
    if command == 'neg':
        operand = parse_operand(str_list[3 :])
        if operand != None:
            return to_negadecimal(eval(operand))
        else:
            return 'Error'
    if command == 'quit':
        if len(str_list) == 4:
            return 'Quit'
        else:
            return 'Error'

def parse_operand(str_list):
    '''Decides whether a list stands for an integer.'''
    is_minus = False
    if str_list != []:
        if str_list[0] == '-':
            str_list = str_list[1 :]
            is_minus = True
        else:
            pass
        string = ''.join(str_list)
    else:
        return None
    for i in string:
        if i >= '0' and i <= '9':
            pass
        else:
            if string == 'mem':
                return str(fetch())
            else:
                return None
    if is_minus:
        return '-' + string
    else:
        return string  
    
