#!usr/bin/env python
# _*_ encoding: utf-8 _*_
# logParser.py - le linhas interessantes de um determinado arquivo e escreve outro com este subconjunto

import os
import glob

cadeiaProcurada = raw_input("Escolha o padrao que deseja parsear: ")

nomeArquivoSaida = cadeiaProcurada.replace(" ", "_")
arquivoSaida = file(nomeArquivoSaida + ".txt", "w")

for nomeArquivoEntrada in glob.glob(os.path.join(".", "*.log*")):
	arquivoEntrada = file(nomeArquivoEntrada)
	for linha in arquivoEntrada.readlines(): 
		if cadeiaProcurada in linha:
			arquivoSaida.write(linha)

arquivoEntrada.close()
arquivoSaida.close()
