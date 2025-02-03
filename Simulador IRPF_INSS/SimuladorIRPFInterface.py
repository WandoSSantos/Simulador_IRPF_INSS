import tkinter as tk
from tkinter import ttk

def calcular_irpf():
    try:
        salario_bruto = float(entry_salario.get())
        tipo_contribuinte = combobox_tipo.get()
        outras_deducoes = float(entry_outras_deducoes.get())

        if salario_bruto <= 0:
            raise ValueError("Salário deve ser maior que zero.")

        # Cálculo do INSS (teto de R$ 1631,48)
        valor_inss = calcular_inss(salario_bruto, tipo_contribuinte)

        # Base de cálculo do IRPF
        base_calculo = salario_bruto - valor_inss - outras_deducoes

        # Dedução fixa
        deducao_fixa = 584.80

        # Cálculo do IRPF
        irpf = calcular_irpf_faixas(base_calculo - deducao_fixa)

        label_resultado.config(text=f"Valor do IRPF: R$ {irpf:.2f}")

    except ValueError as e:
        label_resultado.config(text=f"Erro: {e}")
    except Exception as e:
        label_resultado.config(text=f"Erro inesperado: {e}")

def calcular_inss(salario_bruto, tipo_contribuinte):
    if tipo_contribuinte == "Empregado":
        aliquota = calcular_aliquota_empregado(salario_bruto)
    elif tipo_contribuinte == "Contribuinte Individual":
        aliquota = calcular_aliquota_contribuinte_individual(salario_bruto)
    elif tipo_contribuinte == "Pro Labore":
        aliquota = calcular_aliquota_pro_labore(salario_bruto)
    else:
        raise ValueError("Tipo de contribuinte inválido.")

    valor_inss = salario_bruto * aliquota
    teto_contribuicao = 1631.48
    return min(valor_inss, teto_contribuicao)

def calcular_aliquota_empregado(salario_bruto):
    if salario_bruto <= 1518.00:
        return 0.075
    elif salario_bruto <= 2793.88:
        return 0.09
    elif salario_bruto <= 4190.83:
        return 0.12
    elif salario_bruto <= 8157.41:
        return 0.14
    else:
        return 0.14  # Teto

def calcular_aliquota_contribuinte_individual(salario_bruto):
    if salario_bruto < 1518.00  or salario_bruto <= 8157.40 :
        return 0.20

def calcular_aliquota_pro_labore(salario_bruto):
    if salario_bruto < 1518.00  or salario_bruto <= 14831.63 :
        return 0.11

    try:
        num_dependentes = int(entry_dependentes.get())
        if num_dependentes < 0:
            raise ValueError("Número de dependentes inválido.")
    except ValueError:
        raise ValueError("Número de dependentes deve ser um número inteiro.")

    deducao_dependentes = num_dependentes * 189.59  # Valor da dedução por dependente em 2025
    base_calculo = salario_bruto - valor_inss - outras_deducoes - deducao_dependentes

def calcular_irpf_faixas(base_calculo):
    if base_calculo <= 2112.00:
        return 0.00
    elif base_calculo <= 2826.65:
        return (base_calculo * 0.075) - 158.40
    elif base_calculo <= 3751.05:
        return (base_calculo * 0.15) - 370.40
    elif base_calculo <= 4664.68:
        return (base_calculo * 0.225) - 651.73
    else:
        return (base_calculo * 0.275) - 884.96

# Janela principal
janela = tk.Tk()
janela.title("Simulação de IRPF Mensal 2025")

# Labels e campos
label_salario = ttk.Label(janela, text="Salário Bruto:")
label_salario.grid(row=0, column=0, padx=5, pady=5)

entry_salario = ttk.Entry(janela)
entry_salario.grid(row=0, column=1, padx=5, pady=5)

label_tipo = ttk.Label(janela, text="Tipo de Contribuinte:")
label_tipo.grid(row=1, column=0, padx=5, pady=5)

combobox_tipo = ttk.Combobox(janela, values=["Empregado", "Contribuinte Individual", "Pro Labore"])
combobox_tipo.current(0)  # Define "Empregado" como padrão
combobox_tipo.grid(row=1, column=1, padx=5, pady=5)

label_outras_deducoes = ttk.Label(janela, text="Outras Deduções:")
label_outras_deducoes.grid(row=2, column=0, padx=5, pady=5)

entry_outras_deducoes = ttk.Entry(janela)
entry_outras_deducoes.grid(row=2, column=1, padx=5, pady=5)

botao_calcular = ttk.Button(janela, text="Calcular", command=calcular_irpf)
botao_calcular.grid(row=4, column=0, columnspan=2, padx=6, pady=10)

label_resultado = ttk.Label(janela, text="")
label_resultado.grid(row=5, column=0, columnspan=3, padx=7, pady=7)

label_dependentes = ttk.Label(janela, text="Número de Dependentes:")
label_dependentes.grid(row=3, column=0, padx=5, pady=5)

entry_dependentes = ttk.Entry(janela)
entry_dependentes.grid(row=3, column=1, padx=5, pady=5)

janela.mainloop()