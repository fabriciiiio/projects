def inicio():
    
    import os
    
    class bcolors:
        
        
        HEADER = '\033[95m'
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        RESET = '\033[0m' 
    
    
    
    print(''' 
--------Cronômetro Pika B)-------- ''')

    import time

    try:
        
        min = int(input(''' 
        	Minutos:  '''))
    except ValueError:
        print('''
        	Somente números!''')
        inicio()
     
    
    
    try:
        seg = int(input('''
    	    Segundos: '''))
    	    
    	  
    except ValueError:
        
        print('''
        	Somente números!''')
        	
        	
        inicio()
    
    count = 0
     
    
    while seg or min > count:
        
        
        time.sleep(1)
        
        
        if seg > 59:
            min += seg // 60
            seg = seg % 60

        elif min > 0 and seg == 0:
            min -= 1
            seg = 59         
       
        if seg == 0 and min > 0:
        
        
            seg = 59
            min -= 1
            
        if min == 0 and seg > 0:
            seg -= 1
            
        if min and seg > 0:
            seg -=1
            
        
        
        os.system('clear')
            
        print(f' Cronômetro {bcolors.RESET} {bcolors.GREEN}Ligado!{bcolors.RESET}')
        
        print('''
        	{}:{}seg'''.format(min, seg))
        	
    if min and seg == 0:
        again()
        
    again()
        	
        	
        
    
    
    
    


def again():
    
    
    dnv = input('''
    	Deseja cronometrar de novo?
    	
    	Y or N: ''')
    	
    if dnv == 'Y':
        inicio()
    elif dnv == 'y':
        inicio()
    elif dnv == 'N':
        quit()
    elif dnv == 'n':
        quit()
        
    else:
        print('Comando Invalido!')
        again()
        

inicio()



        

    
    
    
    
    
    
    
    
    
    
 
        
    
    
        
        
    
    

    

