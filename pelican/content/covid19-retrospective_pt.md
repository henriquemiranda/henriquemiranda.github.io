Title: COVID-19: uma breve retrospetiva
Date: 2026-09-16 20:30
Category: Others

Em abril de 2020 ajustei modelos SIR e SIR-X aos casos ativos de COVID-19 reportados. As figuras abaixo reproduzem o procedimento de ajuste original, utilizando apenas os dados disponíveis na altura; a série de dados a azul é prolongada com os [relatórios diários](https://github.com/CSSEGISandData/COVID-19) posteriores da Johns Hopkins, até 7 de julho de 2020, o fim da janela original de 90 dias.

<a href="{static}/scripts/generate_covid19_retrospective.py" download>Descarregar o script Python usado para gerar estas figuras.</a>

Os pontos a azul mostram o número oficial de casos ativos em cada dia, calculado da mesma forma que na publicação original.

- **Áustria:** o ajuste SIR-X captou bem o pico inicial e o declínio que se seguiu.
- **Itália:** captou o abrandamento, mas subestimou e antecipou o pico (cerca de 91 000 previstos, contra 108 000 reportados).
- **Portugal, Espanha e Bélgica:** o ajuste captou a escala do patamar inicial, mas previu o declínio demasiado cedo.
- **EUA:** o ajuste falhou para além do seu curto horizonte: o número de casos ativos reportados continuou a aumentar muito depois do pico previsto.

Embora o modelo SIR-X não seja perfeito, é certamente muito melhor do que o modelo SIR.

![Retrospetiva de Portugal]({static}/images/covid19-retrospective/portugal-retrospective.png)
![Retrospetiva da Áustria]({static}/images/covid19-retrospective/austria-retrospective.png)
![Retrospetiva de Itália]({static}/images/covid19-retrospective/italy-retrospective.png)
![Retrospetiva de Espanha]({static}/images/covid19-retrospective/spain-retrospective.png)
![Retrospetiva da Bélgica]({static}/images/covid19-retrospective/belgium-retrospective.png)
![Retrospetiva dos EUA]({static}/images/covid19-retrospective/us-retrospective.png)
