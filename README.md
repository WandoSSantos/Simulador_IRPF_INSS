# Simulador_IRPF_INSS
Aplicação para simulação de IRPF e INSS

## Estrutura do Aplicativo:

O aplicativo terá a seguinte estrutura:

Uma janela principal com os campos para o salário bruto e o tipo de contribuinte.
Um menu suspenso (combobox) para selecionar o tipo de contribuinte.
Um botão para acionar o cálculo.
Labels (rótulos) para identificar os campos e o resultado.

## Explicação do Código:

Funções de cálculo de alíquota:
calcular_aliquota_empregado(): Implementa a lógica de cálculo para empregados, utilizando a tabela do INSS de 2024.
calcular_aliquota_contribuinte_individual(): Esta função precisa ser implementada de acordo com as regras específicas para contribuintes individuais (autônomos). 
calcular_aliquota_pro_labore(): Esta função precisa foi implementada de acordo com as regras para pro labore. 
Combobox: O widget ttk.Combobox permite selecionar o tipo de contribuinte.
Tratamento de erros: O código inclui tratamento de erros para entradas inválidas (salário menor ou igual a zero e tipo de contribuinte inválido).
