import pandas as pd
import joblib

def recomendar_produtos_para_cliente(dados_cliente: dict, modelo_path='app/models/modelo_cluster.pkl', perfil_path='app/models/perfil_produtos_por_cluster.xlsx', top_n=5):
    # Carrega o modelo de clusterização treinado
    modelo = joblib.load(modelo_path)
    # Carrega o perfil de produtos por cluster
    perfil_produtos = pd.read_excel(perfil_path)

    # Converte os dados do cliente em um DataFrame
    dados_df = pd.DataFrame([dados_cliente])

    # Realiza a previsão do cluster para o cliente
    previsao_cluster = modelo.predict(dados_df)[0]

    # Seleciona os produtos mais recomendados para o cluster previsto
    produtos_recomendados = perfil_produtos[perfil_produtos['Cluster'] == previsao_cluster] \
                                        .sort_values('Frequencia', ascending=False)['Produto'].head(top_n).tolist()
    
    # Retorna o cluster previsto e a lista de produtos recomendados
    return {
        'Cluster previsto': int(previsao_cluster),
        'Produtos recomendados': produtos_recomendados
    }
