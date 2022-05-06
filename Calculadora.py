


class bcolors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'

def calculator():

    print(f'{bcolors.RED}===CALCULADORA {bcolors.GREEN}2000==={bcolors.RESET}')
  
    try:
      number_1 = int(input('Primeiro número: '))
    except ValueError:
       print('''
       	Somente números!''')
       calculator()
    
    simbol = input('''
Selecione o operador matemático:
    + para adição
    - para subtração
    x para multiplicação
    ÷ para divisão
''')


    try:
        number_2 = int(input('Segundo número: '))
    except ValueError:
        print('''
        	  Somente números!''')
        
 
  #####       
    
    if simbol == '+':
       print('{} + {} = '.format(number_1, number_2))
       print(number_1 + number_2)
    elif simbol == '-':
      print('{} - {} = '.format(number_1, number_2))
      print(number_1 - number_2)

    elif simbol == 'x':
      print('{} x {} = '.format(number_1, number_2))
      print(number_1 * number_2)
      
    elif simbol == '÷':
      print('{} ÷ {} = '.format(number_1, number_2))
      print(number_1 / number_2)

   
    else:
        print('''
         	Operador inválido''')
        calculator()
    again()
        

       
       


def again():
    dnv = input(''' 
    	Quer fazer outro calculo?
    	Y or N 
    	''')
    	
    if dnv == 'Y':
        calculator()
    elif dnv == 'N':
        print('Até logo!')
        
calculator()
        
        



        
        	
    
