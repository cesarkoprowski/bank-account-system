from datetime import datetime

def formata_data(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        data_formatada = (data.year, data.month, data.day)
        return data_formatada
    except ValueError:
        return None