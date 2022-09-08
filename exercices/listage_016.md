# Lambda

---

1. Faça um programa para calcular o valor das parcelas de um financiamento no regime de juros compostos com capitalização mensal para uma quantidade indeterminada de pessoas. O programa deverá ler o valor do financiamento e o número de parcelas, calcular e exibir o valor da parcela. O programa termina quando o valor do financiamento for igual a zero. Abaixo apresentamos a tabela contendo os prazos de financiamentos e a taxa de juros anual:
    ```Prazo      taxa a.a.
    6             	 7%
    12           	10%
    18           	12%
    24           	15%
    36           	18%
    ```
    Fazer duas funções:
    Função lambda que calcula o valor da prestação. Argumentos de entrada: financiamento, prazo e taxa; saída: prestação
    função local que seleciona o percentual do financiamento. Argumento de entrada: prazo; saída: taxa. A taxa da tabela é anual, mas como a capitalização é mensal, é necessário dividir a taxa por 12. A fórmula de cálculo da prestação é:
    prestacao=valorfinanciamento×(1+taxa)^p×taxa(1+taxa)^p−1

    **obs**: p = número de parcelas

2. A padaria Sópão vende diariamente uma certa quantidade de pães franceses e uma quantidade de broas. Cada pãozinho custa R$ 0,80 e a broa custa R$ 2,50. Do total arrecadado, 43% corresponde aos custos de fabricação. Do restante, Seu joão guarda 15% numa conta de poupança e 15% ele converte em Euros para sua viagem Anual. Sabe-se que 1 Euro custa R$ 4,60. Com base nestes fatos, faça um programa para ler as quantidades de pães e de broas, calcular a venda total de pãos e broas, o custo de fabricação, quanto irá guardar na poupança e quantos euros irá comprar. Ao final exibir os dados calculados.
