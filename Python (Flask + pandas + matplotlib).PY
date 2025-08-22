from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Carregar CSV
    df = pd.read_csv('data/vendas.csv')
    
    # Agrupar vendas por produto
    resumo = df.groupby('Produto').Quantidade.sum()
    
    # Gerar gráfico de barras
    plt.figure(figsize=(8,5))
    resumo.plot(kind='bar', color='skyblue')
    plt.title('Vendas por Produto')
    plt.ylabel('Quantidade')
    plt.tight_layout()
    
    # Converter gráfico para imagem base64
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    
    return render_template('index.html', plot_url=plot_url, resumo=resumo.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
