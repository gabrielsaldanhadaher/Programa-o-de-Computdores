from openpyxl import Workbook
import matplotlib.pyplot as plt
ARQUIVO = "Investimento.xlsx"

#cria planilha

wb = Workbook()
ws = wb.active
ws.title = "Simulação"
#cabeçalho
ws.append(["Mês", "Saldo"])

#parâmetros do investimento

VP = 1000
aporte = 200
taxa = 0.01
meses = 24
saldo = VP
saldos = []
for mes in range(1, meses + 1):
  saldo = saldo * (1+taxa) + aporte
  saldos.append(saldo)
  ws.append([mes, round(saldo, 2)])
wb.save(ARQUIVO)
print("Planilha criada com sucesso!")

#gráfico automático

plt.figure()
plt.plot(range(1, meses + 1),saldos)
plt.xlabel("Meses")
plt.ylabel("Saldo (R$)")
plt.title("Evolução do Investimentos")
plt.grid()
plt.show()