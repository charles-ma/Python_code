mem = 0

def to_decimal(ndn):
    '''Turns a negadecimal number to a decimal one.'''
    ls = list(ndn)
    ls.reverse()
    ls_num = []
    dec = 0
    for i in ls:
        num = eval(i)
        ls_num.append(num)
    for j in range(0, len(ls_num)):
        dec += ls_num[j] * ((-10)**j)
    return dec

def to_negadecimal(dec):
    '''Turns a decimal number into a negadecimal one.'''
    digits = []
    while abs(dec) > 0:
        digit = dec % 10	
        digits.append(digit)
        dec = - (dec / 10)
    for i in range(0, len(digits)):
        digits[i] = str(digits[i])
    digits.reverse()
    return ''.join(digits)
    
def store(ndn):
    '''Stores ndn into mem.'''
    global mem
    mem = ndn

def fetch():
    '''Gets the value of mem.'''
    global mem
    if type(mem) == type('a'):
        return mem
    else:
        pass

def add(ndn_1, ndn_2):
    '''Adds two negadecimals together.'''
    dec_1 = to_decimal(ndn_1)
    dec_2 = to_decimal(ndn_2)
    summ = dec_1 + dec_2
    summ_neg = to_negadecimal(summ)
    store(summ_neg)
    return summ_neg

def subtract(ndn_1, ndn_2):
    dec_1 = to_decimal(ndn_1)
    dec_2 = to_decimal(ndn_2)
    difference = dec_1 - dec_2
    diff_neg = to_negadecimal(difference)
    store(diff_neg)
    return diff_neg

def multiply (ndn_1, ndn_2):
    dec_1 = to_decimal(ndn_1)
    dec_2 = to_decimal(ndn_2)
    product = dec_1 * dec_2
    prod_neg = to_negadecimal(product)
    store(prod_neg)
    return prod_neg

def divide (ndn_1, ndn_2):
    dec_1 = to_decimal(ndn_1)
    dec_2 = to_decimal(ndn_2)
    quotient = dec_1 / dec_2
    quot_neg = to_negadecimal(quotient)
    store(quot_neg)
    return quot_neg

def remainder (ndn_1, ndn_2):
    dec_1 = to_decimal(ndn_1)
    dec_2 = to_decimal(ndn_2)
    remain = dec_1 % dec_2
    remain_neg = to_negadecimal(remain)
    store(remain_neg)
    return remain_neg

def negate (negadecimal):
    dec_1 = to_decimal(negadecimal)
    negative = to_negadecimal(0 - dec_1)
    store (negative)
    return negative

def remove_spaces (string):
    nospace = list(string)
    result = []
    for i in range(0, len(nospace)):
        if nospace [i] == ' ' or nospace [i] == '   ' :
            pass
        else :
            result.append (nospace[i])
    return  ''.join(result)

def find_operators (string):
    number = 0
    for i in range (0, len(string)):
        if string [i] in ['+', '-', '/', '*', '%']:
            operator = string [i]
            number = number + 1
    if number > 1:
        print "Error: This is too complicated! Evaluate again."
    elif number == 1:
        return operator
    else:
        print "Error: Where is the operator? Evaluate again."

def evaluate (string):
    string = remove_spaces (string)
    operator = find_operators (string)
    operands = string.split(operator)
    operand_1 = operands[0]
    operand_2 = operands [1]
    if operator == '+':
        return add (operand_1, operand_2)
    elif operator == '-':
        return subtract (operand_1, operand_2)
    elif operator == '*':
        return multiply (operand_1, operand_2)
    elif operator == '/':
        return divide (operand_1, operand_2)
        #Does not check for 0 in denominator.
    elif operator == '%':
        return remainder (operand_1, operand_2)
    else:
        print "There's no operator- we'll deal with this later."
        

    


