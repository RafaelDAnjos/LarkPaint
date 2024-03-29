
try:
    input = raw_input   # For Python2 compatibility
except NameError:
    pass

import turtle

from lark import Lark

turtle_grammar = """
    start: instruction+
    instruction: MOVEMENT NUMBER            -> movement
               | "c" COLOR [COLOR]          -> change_color
               | "fill" code_block          -> fill
               | "repeat" NUMBER code_block -> repeat
               |  reset                     -> reset
               |  dcircle NUMBER            -> draw_circle
               |  home                      -> origin
               |  speed   NUMBER            -> set_speed
               |  clear                     -> limpar

    clear: "limpar"           
    speed: "speed"         
    home: "home"
    dcircle: "dcircle"
    reset: "reset"
    code_block: "{" instruction+ "}"
    MOVEMENT: "f"|"b"|"l"|"r"
    COLOR: LETTER+
    %import common.LETTER
    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
"""

parser = Lark(turtle_grammar)

def run_instruction(t):
    if t.data == 'change_color':
        turtle.color(*t.children)   # We just pass the color names as-is

    elif t.data == 'movement':
        name, number = t.children
        { 'f': turtle.fd,
          'b': turtle.bk,
          'l': turtle.lt,
          'r': turtle.rt, }[name](int(number))

    elif t.data == 'repeat':
        count, block = t.children
        for i in range(int(count)):
            run_instruction(block)

    elif t.data == 'fill':
        turtle.begin_fill()
        run_instruction(t.children[0])
        turtle.end_fill()

    elif t.data == 'code_block':
        for cmd in t.children:
            run_instruction(cmd)

    elif t.data == 'reset':
        turtle.reset()

    elif t.data == 'draw_circle':
        number = t.children[1]
        turtle.circle(int(number))

    elif t.data == 'origin':
        turtle.home()
    elif t.data == 'set_speed':
        numero = int(t.children[1])
        if numero<1 or numero>10:
            turtle.speed(0)
        else:
            turtle.speed(numero)
    elif t.data == 'limpar':
        turtle.clear()


    else:
        raise SyntaxError('Unknown instruction: %s' % t.data)


def run_turtle(program):
    parse_tree = parser.parse(program)
    for inst in parse_tree.children:
        run_instruction(inst)

def main():
    while True:
        code = input('> ')
        try:
            run_turtle(code)
        except Exception as e:
            print(e)

def test():
    text = """
        c red yellow
        fill { repeat 36 {
            f200 l170
        }}
    """
    run_turtle(text)

if __name__ == '__main__':
     #test()

     main()