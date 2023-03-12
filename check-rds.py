import boto3

# Configuração das credenciais
session = boto3.Session(profile_name='default')
rds_client = session.client('rds')

# Obtém a versão do banco de dados
try:
    response = rds_client.describe_db_instances()
    for db in response['DBInstances']:
        print("DB Instance Identifier: {}".format(db['DBInstanceIdentifier']))
        print("DB Engine Version: {}".format(db['EngineVersion']))
except Exception as e:
    print("Erro ao obter informações do banco de dados RDS: {}".format(e))

