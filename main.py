import random

def pedeInfPessoais(l_nome, l_idade):
  nome = input('Nome completo: ')
  l_nome.append(nome)
  idade = int(input('Idade: '))
  l_idade.append(idade)
  return l_nome, l_idade

def pedeFaculdade(l_curso):
  faculdade = ""
  while faculdade != 'sim' and faculdade!= 'não':
    faculdade = input('Está fazendo alguma faculdade? (sim/não) ')
    if faculdade == 'sim' or faculdade == 'não':
      l_curso.append(faculdade)
      break
  return l_curso

def infFaculdade(l_facu, l_curso):
  for i in range(len(l_curso)):
    if l_curso[i] == 'sim':
      curso = input('Qual curso? '.title())
      l_facu.append(curso)
    else:
      curso = ""
      l_facu.append(curso)
  return l_facu

def pedePeriodo(l_curso, l_periodo):
  for i in range(len(l_curso)):
    if l_curso[i] == 'sim':
      periodo = int(input('Está em qual periodo? '))
      l_periodo.append(periodo)
    else:
      periodo = ""
      l_periodo.append(periodo)
  return l_periodo

def pedeTelefone(l_telefone):   
  telefone = 0
  while telefone < 10000000: 
    telefone = int(input('Numero de contato: '))
    if telefone > 10000000:
      l_telefone.append(telefone)  
  return l_telefone

def numCurriculo(curriculo):
  for i in range(1):
    curriculo = random.randint(1, 20)
  return curriculo 

def media(l_curso, l_periodo, l_soma, l_facu):  
  media = 0
  for i in range(len(l_periodo)):
    if l_curso[i] == 'sim' and l_periodo[i] >= 3 and l_facu[i] == 'sistemas de informação':
      media = 100
      l_soma.append(media)
    elif l_curso[i] == 'sim' and l_periodo[i] <= 2 and l_facu[i] == 'sistemas de informação':
      media = 50
      l_soma.append(media)
    elif l_curso[i] == 'sim' and l_periodo[i] >= 3 and l_facu[i] == 'analise e desenvolvimento de sistemas':
      media = 100
      l_soma.append(media)
    elif l_curso[i] == 'sim' and l_periodo[i] <= 2 and l_facu[i] == 'analise e desenvolvimento de sistemas':
      media = 50
      l_soma.append(media)
    else:
      media = 0
      l_soma.append(media)
  return l_soma

def exibirTudo(l_nome, l_idade, l_curso, l_periodo, l_telefone, curriculo, l_soma, l_facu):
  for i in range(len(l_curso)):
    print('Obrigado por participar!')
    print("")
    print('-------Dados fornecidos-------')
    print(f'Nome completo: {l_nome[i].title()}')
    print(f'Idade: {l_idade[i]}')
    print(f'Telefone: {l_telefone[i]}')
    print(f'Possui faculdade: {l_curso[i].title()}')
    if l_curso[i] == 'sim':
      print(f'Curso: {l_facu[i].title()}')
      print(f'Periodo: {l_periodo[i]}')
      print("")
      print('-------Informação extra-------')
    else: 
      print("")
      print('-------Informação extra-------') 
      print('Possuir faculdade nos cursos desejados é fundamental para ser contratado!')
    print(f'Curriculo n° {curriculo}')
    print(f'Chance de ser chamado: {l_soma[i]}%')

def Principal():
  lista_nome = []
  lista_idade = []
  lista_curso = []
  lista_facu = []
  lista_periodo = []
  lista_telefone = []
  num_curriculo = []
  lista_media = []
  lista_nome, lista_idade = pedeInfPessoais(lista_nome, lista_idade)
  lista_curso = pedeFaculdade(lista_curso)
  lista_facu = infFaculdade(lista_facu, lista_curso)
  lista_periodo = pedePeriodo(lista_curso, lista_periodo)
  lista_telefone = pedeTelefone(lista_telefone)
  num_curriculo = numCurriculo(num_curriculo)
  lista_media = media(lista_curso, lista_periodo, lista_media, lista_facu)
  exibirTudo(lista_nome, lista_idade, lista_curso, lista_periodo, lista_telefone, num_curriculo, lista_media, lista_facu)

Principal()