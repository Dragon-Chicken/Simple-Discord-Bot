import random
import jokes

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message[0] == '!':

        p_message = p_message[1:]

        if p_message == 'hello':
            return 'Hay there'

        if p_message == 'roll':
            return str(random.randint(1,6))

        if p_message == 'joke':
            return jokes.jokes[random.randint(1, len(jokes.jokes))-1]

        if p_message == 'brainfk_help':
            return '`+` Adds one to the current cell\n`-` Substracts one from the current cell\n`>` Goes right by one cell\n`<` Goes left by one cell\n' \
                   '`.` Prints out what is at the current cell\n`*` multiplys the current cell by 2\n`/` divides the current cell by 2\n' \
                   'Here is a short program that prints 255 4 times  \n`-.>-.>-.>-.`\n' \
                   'Use `!brainfk` to run the code'

        if p_message[:5] == 'say `' and p_message[len(p_message)-1] == '`':
            message = message.replace('`', '')
            return message[5:]

        return 'Commands list\n`!hello` What am I soposed to put here\n`!joke` Tells a joke\n`!brainfk` BrainF**k interpreter\n`!roll` Rolls a 6 sided dice\n`!say` You can make it say whaterer you want (Rember to use ` before and after your text)'
