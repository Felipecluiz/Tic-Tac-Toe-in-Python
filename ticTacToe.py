cont=0
proceed=True

while(proceed):
	size=int(input("\nsize of the tic-tac-toe, plx number even and > 1\n"))
	if size%2==0 and size>0:
		proceed=False
	else:
		print("this number is not even or < 0")
proceed=True

meuVetor = [[ '-' for y in range(size) ] for x in range(size) ]
#print(len(meuVetor))

#print(meuVetor)

while (cont != size*size):
    	x=0
	x1=0
	o=0
	o1=0
    	
	while(proceed):   
		x=int(input("\nenter the line of x\n"))
		x1=int(input("\nenter the column of x\n"))
		if meuVetor[x][x1]=='-':
			proceed=False
		else: 
			print("another character are occupying this position")
		
	meuVetor[x][x1]="x"
	proceed=True
	#print(meuVetor)
	while(proceed):
		o=int(input("\nenter the line of o\n"))
		o1=int(input("\nenter the column of o\n"))
		if meuVetor[o][o1]=='-':
			proceed=False
		else: 
			print("another character are occupying this position")
		


	meuVetor[o][o1]="o"
	proceed=True

	for i in range(size):	
		print (meuVetor[i])
	contWinvariable=0
	
	

	variable="x"
	for k in range(2):
	###verifying of the column of variable

		for j in range(size):
		
			for i in range(size):
				if meuVetor[i][j]==variable:
					contWinvariable+=1
	
	    		if contWinvariable==size:
				print(variable,"win")
				exit()
			contWinvariable=0
		#####end of verifying
		contWinvariable=0


		###verifying of the lines of variable

		for j in range(size):
		
			for i in range(size):
				if meuVetor[j][i]==variable:
					contWinvariable+=1
	
	    		if contWinvariable==size:
				print(variable," win")
				exit()
			contWinvariable=0
		#####end of verifying
		contWinvariable=0
	
		####verifying of the main diagonal 
		for l in range(size):
			if meuVetor[l][l]==variable:
				contWinvariable+=1
		if contWinvariable==size:
			print(variable," win")
			exit()
		###end of main diagonal	

		contWinvariable=0
	



		####verifying of the secondary diagonal 
		contSec=size-1
		for i in range(size):
			if meuVetor[contSec][i]==variable:
				contWinvariable+=1
			contSec-=1
		if contWinvariable==size:
			print(variable," win")
			exit()
		###end of secondary diagonal	

		contWinvariable=0
		variable="o"

	############################### end of verifying of variable



	cont+=1    
print("break even")	

