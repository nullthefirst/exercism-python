def modular_check(source_number, checking_number, string_output):
    output_result = ""
    if source_number % checking_number == 0:
        output_result += string_output
    return output_result

def convert(number):
    output = ""

    output += modular_check(number, 3, "Pling")

    output += modular_check(number, 5, "Plang")
    
    output += modular_check(number, 7, "Plong")

    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        output += str(number)
    
    return output