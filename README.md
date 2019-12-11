# LarkPaint
Implementação de uma linguagem de domínio específico(DSL) chamada Paint-code , usando um parser voltado para qualquer linguagem livre de contexto chamado lark.

## Autores: 
Rafael Afonso dos Anjos, Emanuel Rampinneli.

## Ferramentas ultilizadas:
Python 3.7.5(LP), JetBrains Pycharm Community Edition 2019(IDE)

## Lark:
Segundo os autores o Lark é um parser que consegue entender qualquer gramática que for inserida nele, não importa quão complicada ou ambígua seja, ele também controi um parser-tree, além de ser simples e fácil de usar

## Turtle:
Turtle é um módulo do python que permite fazer desenhos na tela com comandos simples, ele segue a idéia da programação LOGO e é bem popular na introdução da programação à crianças.

## LarkPaint:
Esse trabalho consiste na criação de uma DSL chamada LarkPaint, que utiliza o módulo turtle e permite o usuario a criar desenhos através de código.

## Estrutura do Código Fonte:
LarkPaint-Master
|   Readme.md
|   Relatório.pdf
|   turtle_dsl.py
|

## Gramática:
A gramática foi desenvolvida dentro do código do turtle_dsl.py
start: instruction+
    instruction: MOVEMENT NUMBER            -> movement
               | "c" COLOR [COLOR]          -> change_color
               | "fill" code_block          -> fill
               | "repeat" NUMBER code_block -> repeat
               |  reset                     -> reset
               |  dcircle NUMBER            -> draw_circle
               |  home                      -> origem
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
   
  ## Como executar?
  
  O primeiro passo é criar um ambiente virtual com o comando:
      virtualenv venv --python=python3
  Para ativar o ambiente virtual dê o comando abaixo:
      source venv/bin/activate
  Agora instale o lark usando o comando:
      pip install lark
  Por ultimo execute o código da dsl atravéz do comando:
      python turtle_dsl.py
  Logo em seguida aparecerá a seguinte instrução:
      insira um comando ->
  Para desativar o virtualenv é só dar a seguinte instrução:
         $ deactivate
      
## Comandos de Testes:
    Segue abaixo os códigos de alguns testes feitos, sendo nescessário copiar e colar no prompt durante a execução do código, lembre-se de a cada teste inserir um comando limpar para limpar a tela.
    
    Square: repeat 4 {f 100 r 90}
    Circle: dcircle 80
    Star: c gold yellow fill{repeat 5{ f100 r145}}
    Ouriço: c blue purple fill {repeat 36{f300 r 170}}
    
    exemplo: insira um comando -> c blue purple fill {repeat 36{f300 r 170}}

## Referências
   
   https://github.com/lark-parser/lark/blob/master/README.md

