
print("Simulação contribuição previdenciaria ")
tipo_contribuinte = input("Digite o tipo de contribuinte (empregado,contribuinte individual ou pro labore): ").lower()
renda_tributavel = float(input("Digite o salário: "))

def calcular_inss(renda_tributavel, tipo_contribuinte):
    """Calcula a contribuição mensal do INSS com base no salário e tipo de contribuinte."""

    if tipo_contribuinte == "empregado":
        if renda_tributavel <= 1518.00 or renda_tributavel <=2793.87:
            contribuicao_INSS = renda_tributavel * 0.075    
        elif renda_tributavel <= 2793.88 or renda_tributavel <=4190.82:
            contribuicao_INSS = renda_tributavel * 0.09
        elif renda_tributavel <= 4190.83 or renda_tributavel <=8157.40:
            contribuicao_INSS = renda_tributavel * 0.12
        elif renda_tributavel <= 8157.41:
            contribuicao_INSS = renda_tributavel * 0.14
        else:
            contribuicao_INSS = 1631.48

    elif tipo_contribuinte == "contribuinte individual":
        if renda_tributavel < 1518.00  or renda_tributavel <= 8157.40 :
            contribuicao_INSS = renda_tributavel* 0.20
        else:
            contribuicao_INSS = 1634.48
        
    else: 
        tipo_contribuinte == "pro labore"
        if renda_tributavel < 1518.00  or renda_tributavel <= 14831.63 :
           contribuicao_INSS = renda_tributavel* .11
        else:
            contribuicao_INSS = 1634.48
    return contribuicao_INSS

contribuicao_INSS = calcular_inss(renda_tributavel, tipo_contribuinte)
valor_INSS = round(contribuicao_INSS, 2)
print("O valor da contribuição da Previdência Social é R$ ", contribuicao_INSS)