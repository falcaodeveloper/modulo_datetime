'''Referências: https://pydetodos.com/python-datetime/
https://www.w3schools.com/python/python_datetime.asp
https://docs.python.org/pt-br/3/library/datetime.html#module-datetime'''

import datetime

dataAtualCompleta = datetime.datetime.now()
dataAtual = datetime.date.today()
criandoObjetoDeData = datetime.datetime(2009, 5, 25, 15, 54, 12) #Ano, mês e dia obrigatórios. Os demais são opcionais.

cincoDiasAMais = dataAtual + datetime.timedelta(days = 5) #Adicioando 5 dias à data atual
cemDiasAMenos = dataAtual - datetime.timedelta(days = 100) #Subtraindo 100 dias da data atual
vinteHorasAMais = dataAtualCompleta + datetime.timedelta(hours = 20)
vinteHorasAMais = vinteHorasAMais.strftime('Data: %d/%m/%y Hora: %H:%M:%S - %f')
duasSemanasAMais = dataAtual + datetime.timedelta(weeks = 2) #Adicioando 2 semanas à data atual
duasSemanasAMais = duasSemanasAMais.strftime('%d-%m-%Y')

print('Data e hora atuais: {}\n' .format(dataAtualCompleta)) #2024-02-02 10:45:35.793979
print('Data atual: {}\n' .format(dataAtual)) #2024-02-02
print('Data de hoje: {}\n' .format(dataAtual.day)) #Mostra o dia atual
print('Estamos no mês {}\n' .format(dataAtual.month)) #Mostra o mês atual
print('Estamos no ano de {}\n' .format(dataAtual.year)) #Mostra o ano atual
print('Hora: {}\n' .format(dataAtualCompleta.hour)) #Mostra a hora atual
print('Minutos: {}\n' .format(dataAtualCompleta.minute)) #Mostra os minutos atuais
print('Segundos {}\n' .format(dataAtualCompleta.second)) #Mostra os segundos atuais
print('Microsegundos: {}\n' .format(dataAtualCompleta.microsecond)) #Mostra os microsegundos atuais

print('Criando objeto de data: {}\n' .format(criandoObjetoDeData)) #Mostra a data e hora criadas.

print('Data formatada: {}\n' .format(dataAtualCompleta.strftime('%d-%m-%Y %H:%M:%S'))) #A reference of all the legal format codes: https://www.w3schools.com/python/python_datetime.asp

print('Data atual com mais 5 dias: {}\n' .format(cincoDiasAMais))
print('100 dias a menos da data atual: {}\n' .format(cemDiasAMenos))
print('20 horas a mais na data atual formatada: {}\n' .format(vinteHorasAMais))
print('2 semanas a mais na data atual: {}\n' .format(duasSemanasAMais))