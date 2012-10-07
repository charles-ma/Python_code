def get_num(decimal):
    digits = []
    while decimal > 0:
            digit = decimal % 10	
            digits.append(digit)
            decimal = decimal / 10
    print digits
