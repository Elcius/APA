"""
Aluno: Elcius Ferreira 
Matrícula: 11400968
Disciplina: Análise de Projetos e Algoritmos

SUB SET SUM PROBLEM

"""

# Função que recebe o vetor a ser analisado, a soma a ser encontrada e retorna verdadeiro ou falso caso encontre.
def isSubsetSum(set, total_sum):

	length_set  = len(set)

	subset = [[x for x in range(length_set+1)] for y in range(total_sum+1)]		# Declarando o array bidimensional

	for numb in range(0, length_set+1):	# Sendo a soma 0, true será retornado
		subset[0][numb] = True

	for numb in range(1, total_sum+1):	# Soma não sendo 0 e set vazio, a resposta será falso
		subset[numb][0] = False

	# Preenchendo o array bidimensional de baixo para cima
	for i in range(1, total_sum+1):
		for j in range(1, length_set+1):
			subset[i][j] = subset[i][j-1]

			if(i >= set[j-1]):
				subset[i][j] = subset[i][j] or subset[i - set[j-1]][j-1]	# Divide o problema em dois subproblemas.
																			# Exclui o último elemento ou inclui o mesmo.

	"""# Para printar a tabela basta descomentar esta parte do código.
	s = [[str(e) for e in row] for row in subset]
	lens = [max(map(len, col)) for col in zip(*s)]
	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	print ('\n'.join(table))"""


	return subset[total_sum][length_set]


# Vetores de entrada a serem testados e as devidas somas a serem analisadas. 
# Nos índices pares se encontram os vetores e nos ímpares o somatório a ser procurado.
vecs_and_sums = []
vecs_and_sums.append([3, 34, 4, 12, 5, 2])
vecs_and_sums.append(12)
vecs_and_sums.append([3, 34, 4, 33, 55, 11, 1, 12, 5, 2])
vecs_and_sums.append(0)
vecs_and_sums.append([7, 2, 68, 3, 3, 34, 4, 12, 5, 2])
vecs_and_sums.append(34)
vecs_and_sums.append([234, 45, 123, 6675, 3, 2])
vecs_and_sums.append(100)
vecs_and_sums.append([345, 45, 563, 5, 4, 12, 5, 2])
vecs_and_sums.append(44)
vecs_and_sums.append([3, 34, 4, 12, 5, 2])
vecs_and_sums.append(56)
vecs_and_sums.append([3, 34, 4, 33, 55, 11, 1, 12, 5, 2])
vecs_and_sums.append(345)
vecs_and_sums.append([7, 2, 68, 3, 3, 34, 4, 12, 5, 2])
vecs_and_sums.append(2)
vecs_and_sums.append([234, 45, 123, 6675, 3, 34, 5, 2])
vecs_and_sums.append(6675)
vecs_and_sums.append([345, 45, 563, 5,56])
vecs_and_sums.append(200)


for i in range(0,len(vecs_and_sums),2):
	if(isSubsetSum(vecs_and_sums[i], vecs_and_sums[i+1]) == True):
		print("Subset com a soma '" + str(vecs_and_sums[i+1]) + "' encontrado no array:" + str(vecs_and_sums[i]))
	else:
		print("Soma '" + str(vecs_and_sums[i+1]) + "' nao encontrada no array:" + str(vecs_and_sums[i]))
