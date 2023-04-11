
bf_input = None

def run_code(code):

    tape = [0]
    output = []

    extra_input = 0
    tape_index = 0
    code_index = 0

    t = 0

    while code_index < len(code):

        if tape_index >= len(tape):
            tape.append(0)

        if code[code_index] == '+':
            tape[tape_index] += 1

        elif code[code_index] == '-':
            tape[tape_index] -= 1

        elif code[code_index] == '>':
            tape_index += 1

        elif code[code_index] == '<':
            tape_index -= 1

        elif code[code_index] == '.':
            output.append(tape[tape_index])

        elif code[code_index] == '*':
            tape[tape_index] *= 2

        elif code[code_index] == '/':
            tape[tape_index] = int(tape[tape_index] / 2)

        elif code[code_index] == ',':
            print('PLZ WORK')
            bf_input = 1
            print(bf_input)

        while tape[tape_index] > 255:
            tape[tape_index] -= 255

        while tape[tape_index] < 0:
            tape[tape_index] += 255

        code_index += 1

    f_output = str(output).replace('[', '')
    f_output = f_output.replace(',', '')
    f_output = f_output.replace(']', '')

    if f_output == '':
        return 'Use `!brainfk_help` to see how to use Brainfk'

    return f_output

#print("what you wrote: ", tape)
#print(code)