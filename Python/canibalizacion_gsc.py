# Importamos las librerías necesarias
import pandas as pd
import searchconsole  # Para conectar a la API de GSC
from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_gsc_data(site_url):
    # Autenticación
    account = searchconsole.authenticate(client_config='apps.googleusercontent.com.json')
    
    # Obtener la propiedad del sitio
    webproperty = account[site_url]  # Usar el site_url directamente
    
    # Cambia las fechas a un rango válido
    report = webproperty.query.range('2024-07-01', '2024-10-01').dimension('page', 'query').get()
    
    # Convertir el informe en un DataFrame
    df = pd.DataFrame(report)
    return df

def find_cannibalized_queries(df):
    # Agrupar por 'query' y contar cuántas páginas están posicionadas
    kw_summary = (
        df.groupby('query')
        .agg({'page': 'nunique'})  # Contar las páginas únicas
        .rename({'page': 'n_pages'}, axis=1)
        .reset_index()
    )
    
    # Unir los datos originales con el resumen de canibalización
    cannibalized_kw = df.merge(kw_summary, on='query', how='left')
    
    # Filtrar para obtener solo las consultas con más de una URL
    cannibalized_kw = cannibalized_kw[cannibalized_kw['n_pages'] > 1]
    
    return cannibalized_kw

# Definir la URL del sitio
site_url = 'https://tudominio.com/'  # Asegúrate de que este sea el correcto

# Llamar a la función para obtener datos
if __name__ == "__main__":
    df = get_gsc_data(site_url)
    print("Datos crudos:")
    print(df)  # Muestra los datos obtenidos
    
    # Encontrar las consultas canibalizadas
    cannibalized_results = find_cannibalized_queries(df)
    print("\nResultados de canibalización:")
    print(cannibalized_results)  # Muestra los resultados de canibalización
    
    # Guardar los DataFrames en archivos CSV
    df.to_csv('/gsc_data.csv', index=False)  # Datos originales
    cannibalized_results.to_csv('/cannibalization_results.csv', index=False)  # Resultados de canibalización
