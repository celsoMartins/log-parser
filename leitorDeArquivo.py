#!usr/bin/env python
# _*_ encoding: utf-8 _*_
# leitorDeArquivo.py- Leitor de arquivos

spam = file("teste.txt")
for linha in spam.readlines(): print linha,
