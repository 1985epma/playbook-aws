import boto3
from datetime import datetime, timedelta

# Configuração das credenciais
session = boto3.Session(profile_name='default')
ce_client = session.client('ce')

# Obtém o faturamento diário
start = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
end = datetime.now().strftime('%Y-%m-%d')

try:
    response = ce_client.get_cost_and_usage(
        TimePeriod={
            'Start': start,
            'End': end
        },
        Granularity='DAILY',
        Metrics=[
            'BlendedCost'
        ]
    )
    cost = response['ResultsByTime'][0]['Total']['BlendedCost']['Amount']
    print("Faturamento diário: ${}".format(cost))
except Exception as e:
    print("Erro ao obter faturamento diário: {}".format(e))

