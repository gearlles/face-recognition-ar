# face-recognition-ar

## Requisitos ##
* Python 2.7
* [PIL](http://www.pythonware.com/products/pil/)
* [NumPy](http://www.numpy.org/)
* [SciPy](http://sourceforge.net/projects/scipy/files/latest/download?source=files)
* [matplotlib](http://matplotlib.org/)
* [facerec](https://github.com/bytefish/facerec) - [instruções de instalação](http://bytefish.de/dev/facerec/install/index.html)

## Instalação (Windows) ##
1. Certifique-se que sua instalação do Python está correta. Digite "python" e "pip" na linha de comando. Caso dê algum erro, adicione `C:\Python27` e `C:\Python27\Script` na variável de ambiente `PATH`. 
2. Baixe e instale o SciPy.
3. Abra a linha de comando e navegue até a página raiz do projeto (onde você deu checkout).
4. Execute `pip setup.py install`.

## IDE recomendada ##
[Pycharm](https://www.jetbrains.com/pycharm/)

## Configuração ##
Só é necessário configurar os caminhos para a base de treino e teste. No arquivo `main.py`, configure as variáveis `train_database_path` e `test_database_path`.

## Formato esperado da base ##
Cada amostra deve estar agrupada em pastas, que serão as classes. Ou seja, cada pessoa é uma pasta e dentro dela estão todas as imagens do indivíduo. Ambas bases de treino e teste devem seguir esse formato.

```
.
|-- person1
|   |-- 1.jpg
|   |-- 2.jpg
|   |-- 3.jpg
|   |-- 4.jpg
|-- person2
|   |-- 1.jpg
|   |-- 2.jpg
|   |-- 3.jpg
|   |-- 4.jpg
```

## Execução ##
Apenas execute o arquivo `main.py`.

## Links úteis ##

* http://bytefish.de/pdf/facerec_python.pdf
* http://www.bytefish.de/blog/fisherfaces/
