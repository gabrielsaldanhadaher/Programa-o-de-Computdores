import pandas as pd
import matplotlib.pyplot as plt

#parâmetro de investimento

aporte_inicial = 1000
aporte_mensal = 500
taxa_juros = 0.01 #1% ao mês
meses = 24
dados = []

saldo = aporte_inicial
for mes in range(1, meses + 1):
  rendimento = saldo * taxa_juros
  saldo += rendimento + aporte_mensal
  dados.append({"Mês": mes, "Saldo": round(saldo, 2), "Rendimento": round(rendimento, 2)})
round(rendimento, 2)
df = pd.DataFrame(dados)

#salvar no excel

arquivo = "investimento.xlsx"
df.to_excel(arquivo, index=False)
print("Planilha criada com sucesso!")

#gráfico1

plt.figure()
plt.plot(df["Mês"], df["Saldo"])
plt.title("Evolução do Saldo")
plt.xlabel("Meses")
plt.ylabel("Saldo (R$)")
plt.grid()
plt.show()

#gráfico2

plt.figure()
plt.plot(df["Mês"], df["Rendimento"])
plt.title("Evolução do Rendimento")
plt.xlabel("Meses")
plt.ylabel("Rendimento (R$)")
plt.grid()
plt.show()