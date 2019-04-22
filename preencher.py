def main():

	'''primeiro vou abrir os arquivos'''
	arquivo1 = open("teste.txt", "w") #abrindo arquivo existente
	arquivo2 = open("teste2.txt","w") #criando e abrindo arquivo

	'''agora vamos preencher o arquivo1'''
	arquivo1.append(input('Escreva o conteúdo: /n'))
	arquivo2.append(arquivo1)
