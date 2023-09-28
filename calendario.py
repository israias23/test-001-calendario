from datetime import datetime, timedelta
import calendar
import random

def obter_nome_dia_semana(data):
    nomes_dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    return nomes_dias_semana[data.weekday()]

def obter_ultimo_dia_mes(ano, mes):
    return calendar.monthrange(ano, mes)[1]

def escolher_funcionario_e_funcao(funcionarios, historico_funcionarios, ano, mes, dia_mes):
    while True:
        funcionario = random.choice(funcionarios)
        ultima_data_escolha = historico_funcionarios.get(funcionario)
        # Informar com quantos dias mínimos o nome do funcionario deve aparecer de novo na lista
        if ultima_data_escolha is None or (datetime(ano, mes, dia_mes) - ultima_data_escolha).days >= 15:
            return funcionario, atribuir_funcao(dia_mes)

def atribuir_funcao(dia_mes):
    dia_semana = obter_nome_dia_semana(datetime(ano_escolhido, mes_escolhido, dia_mes))
    funcoes_por_dia = {
        "Segunda-feira": "kiosk",
        "Terça-feira": "check-in",
        "Quarta-feira": "desembarque ",
        "Quinta-feira": "loja",
        "Sexta-feira": "kiosk",
        "Sábado": "check-in",
        "Domingo": "desembarque"
    }
    return funcoes_por_dia[dia_semana]

def gerar_programacao(ano, mes):
    funcionarios = ["AGNALIA", "ANDREIA", "ANGELA", "BEATRIZ", "DENNER", "EINER", "ELEN", "FELIPE SILVA", "EMMANUEL",
                   "LUAN", "RODRIGO", "SAVIO", "BRENDOW", "JESSIKA", "DEBORA", "GABRIELLA", "ISACC", "LARA", "STEPHANIE"]

    num_dias_no_mes = obter_ultimo_dia_mes(ano, mes)

    historico_funcionarios = {}
    programacao_mes = []

    for dia_mes in range(1, num_dias_no_mes + 1):
        funcionario, funcao = escolher_funcionario_e_funcao(funcionarios, historico_funcionarios, ano, mes, dia_mes)

        historico_funcionarios[funcionario] = datetime(ano, mes, dia_mes)
        data = datetime(ano, mes, dia_mes)
        dia_semana = obter_nome_dia_semana(data)
        data_formatada = data.strftime("%d/%m")

        programacao_mes.append({'dia': dia_semana, 'data': data_formatada, 'funcionario': funcionario, 'funcao': funcao})

    return programacao_mes

if __name__ == "__main__":
    ano_escolhido = int(input("Digite o ano desejado: "))
    mes_escolhido = int(input("Digite o número do mês desejado (1 a 12): "))

    if mes_escolhido < 1 or mes_escolhido > 12:
        print("Mês inválido. Por favor, escolha um número de mês entre 1 e 12.")
    elif ano_escolhido <= 0:
        print("Ano inválido. O ano deve ser maior que zero.")
    else:
        programacao = gerar_programacao(ano_escolhido, mes_escolhido)
        for item in programacao:
            print(f"{item['dia']} ({item['data']}): {item['funcionario']} - Função: {item['funcao']}")
