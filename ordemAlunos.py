from random import shuffle

def inicio():
    
    print('''
    	===ORDEM=== 
    		''')
	
    try:
   
        totalalunos = int(input('Quantidade de Alunos: '))
    except ValueError:
    	
    	print('''
    	 Somente números!
    	 ''')
    	quit()
    	
    oqseria = input('''
    Ordem para oque?
    (exp: Apresentação, Chamada, etc. : ''')
    
    	
    count = 0
    numa = 1
    
    lista = []
    
    while count < totalalunos:
    	
    
    	aluno = input(f'''
    	
    	Nome {numa}: ''')
    	
    	lista.append(aluno)
    	
    	count += 1
    	numa +=1
    	
    	ordem = 1
    	contagem = 0
    	count2 = 0
    	
    shuffle(lista)
    
    print(f'A ordem de {oqseria} é')
    	
    while count2 < totalalunos:
        print(f'{ordem}: {lista[contagem]}')
        contagem += 1
        ordem += 1
        count2 += 1
        
        
    
    shuffle(lista)
    
inicio()

def novamente():
    
    	
    	dnv = input('''
    	Resetar?
    	Y / N: ''')
    	
    	if dnv == 'Y':
        	
        	inicio()
    		
    	elif dnv == 'y':
        	
        	inicio()
    	
    	elif dnv == 'N':
        	
    		   print('Ate Mais!')
    		  
    		
    	elif dnv == 'n':
        	
        	print('Ate mais!')
    		   
    		
    	else:
        	
    		   print('''
    		Opcao invalida!''')
    		
    		   novamente()
    		
novamente()