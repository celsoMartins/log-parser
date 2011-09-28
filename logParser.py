#!usr/bin/env python
# _*_ encoding: utf-8 _*_
# logParser.py - le linhas interessantes de um determinado arquivo e escreve outro com este subconjunto

arquivoEntrada = file("teste.txt")
linhasInteressantes = list()
cadeiaProcurada = raw_input("Escolha o padrao que deseja parsear: ")
for linha in arquivoEntrada.readlines(): 
	print linha,
	if cadeiaProcurada in linha:
		linhasInteressantes.append(linha)

arquivoEntrada.close()

nomeArquivoSaida = cadeiaProcurada.replace(" ", "_")

arquivoSaida = file(nomeArquivoSaida + ".txt", "w")

for linhaInteressante in linhasInteressantes:
	arquivoSaida.write(linhaInteressante)

arquivoSaida.close()

