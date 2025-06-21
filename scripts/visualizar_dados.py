import matplotlib.pyplot as plt

def plotar_cotacoes(media_usd, media_eur):
    plt.figure(figsize=(10,5))
    media_usd.plot(label='USD/BRL', marker='o')
    media_eur.plot(label='EUR/BRL', marker='x')
    plt.title('Cotação Média Diária - USD e EUR')
    plt.xlabel('Data')
    plt.ylabel('Cotação (R$)')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
