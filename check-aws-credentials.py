import boto3
from botocore.exceptions import ClientError

# Configuração das credenciais
session = boto3.Session(profile_name='default')
sts_client = session.client('sts')

# Obtém as credenciais da sessão
try:
    response = sts_client.get_caller_identity()
    print("Credenciais da AWS:")
    print("- ID do usuário: {}".format(response['UserId']))
    print("- ARN do usuário: {}".format(response['Arn']))
    print("- Nome da conta: {}".format(response['Account']))
except ClientError as e:
    print("Erro ao obter credenciais: {}".format(e))

# Obtém o tempo de sessão restante
try:
    response = sts_client.get_session_token(DurationSeconds=3600)
    remaining_time = response['Credentials']['Expiration'] - response['Credentials']['Expiration']
    print("Tempo de sessão restante: {} segundos".format(remaining_time))
except ClientError as e:
    print("Erro ao obter tempo de sessão restante: {}".format(e))

