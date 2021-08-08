#Realize o cadastro de um aluno, com as seguintes informações: Nome, endereço, cidade e idade

nome = str(input('Digite o seu nome: '))
endereco = str(input('Digite o seu endereço: '))
cidade  = str(input('Digite a sua cidade: '))
idade = int(input('Digite a sua idade: '))

print(f'{nome}, tem {idade}anos e reside em {endereco}, na cidade de {cidade}. ')