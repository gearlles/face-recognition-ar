# face-recognition-ar
Projeto desenvolvido para a disciplina de Visão Computacional da Universidade de Pernambuco. O objetivo é realizar o reconhecimento de faces e verificar a taxa de classificação utilizando a [base AR](http://www2.ece.ohio-state.edu/~aleix/ARdatabase.html).

## Requisitos ##
* Python 2.7
* [PIL](http://www.pythonware.com/products/pil/)
* [NumPy](http://www.numpy.org/)
* [SciPy](http://sourceforge.net/projects/scipy/files/latest/download?source=files)
* [matplotlib](http://matplotlib.org/)
* [facerec](https://github.com/bytefish/facerec) - [instruções de instalação](http://bytefish.de/dev/facerec/install/index.html)

## Instalação (Windows) ##
1. Certifique-se que sua instalação do Python está correta. Digite "python" e "pip" na linha de comando. Caso dê algum erro, adicione `C:\Python27` e `C:\Python27\Script` na variável de ambiente `PATH`. 
2. Baixe e instale as dependências.
3. Abra a linha de comando e navegue até a página raiz do projeto (onde você deu checkout).
4. Execute `pip setup.py install`.

## IDE recomendada ##
[Pycharm](https://www.jetbrains.com/pycharm/)

## Configuração ##
Só é necessário configurar os caminhos para a base de treino e teste. No arquivo `main.py`, configure a variável `database_path`.

## Formato esperado da base ##
É utilizada a AR database. Então, o formato da base deve seguir o mesmo formato da AR.

```
.
|-- M-001-01.bmp
|-- M-001-02.bmp
|-- M-001-03.bmp
|-- M-001-04.bmp
|-- M-001-05.bmp
|-- M-001-06.bmp
|-- ...
|-- W-050-26.bmp
```

## Execução ##
Apenas execute o arquivo `main.py`.

## Links úteis ##

* http://bytefish.de/pdf/facerec_python.pdf
* http://www.bytefish.de/blog/fisherfaces/
