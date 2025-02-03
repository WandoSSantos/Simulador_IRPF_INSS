import tkinter as tk
from tkinter import ttk

def calcular_inss():
    try:
        salario_bruto = float(entry_salario.get())
        tipo_contribuinte = combobox_tipo.get()

        if salario_bruto <= 0:
            raise ValueError("Salário deve ser maior que zero.")

        # Cálculo do INSS (tabela de 2024)
        if tipo_contribuinte == "Empregado":
            aliquota = calcular_aliquota_empregado(salario_bruto)
        elif tipo_contribuinte == "Contribuinte Individual":
            aliquota = calcular_aliquota_contribuinte_individual(salario_bruto)
        elif tipo_contribuinte == "Pro Labore":
            aliquota = calcular_aliquota_pro_labore(salario_bruto)
        else:
            raise ValueError("Tipo de contribuinte inválido.")

        valor_inss = salario_bruto * aliquota
        
        # Aplica o teto de contribuição
        teto_contribuicao = 1631.48
        if valor_inss > teto_contribuicao:
            valor_inss = teto_contribuicao

        label_resultado.config(text=f"Valor do INSS: R$ {valor_inss:.2f}")

    except ValueError as e:
        label_resultado.config(text=f"Erro: {e}")
    except Exception as e:
        label_resultado.config(text=f"Erro inesperado: {e}")

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
    

# Janela principal
janela = tk.Tk()
janela.title("Cálculo de INSS")

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

botao_calcular = ttk.Button(janela, text="Calcular", command=calcular_inss)
botao_calcular.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

label_resultado = ttk.Label(janela, text="")
label_resultado.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

janela.mainloop()