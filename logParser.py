#!usr/bin/env python
# _*_ encoding: utf-8 _*_
# logParser.py - le linhas interessantes de um determinado arquivo e escreve outro com este subconjunto

cadeiaProcurada = raw_input("Escolha o padrao que deseja parsear: ")
arquivoDeBusca = raw_input("Nome do arquivo de busca: ")

arquivoEntrada = file(arquivoDeBusca)
nomeArquivoSaida = cadeiaProcurada.replace(" ", "_")
arquivoSaida = file(nomeArquivoSaida + ".txt", "w")

for linha in arquivoEntrada.readlines(): 
	print linha,
	if cadeiaProcurada in linha:
		arquivoSaida.write(linha)

arquivoEntrada.close()
arquivoSaida.close()
