import subprocess

# Configuração do domínio e dos diretórios para armazenar o certificado
domain = "epmait.com"
cert_path = "/etc/letsencrypt/live/{}/".format(domain)
webroot_path = "/var/www/{}".format(domain)

# Executa o comando do certbot para criar ou renovar o certificado
command = "certbot certonly --webroot --webroot-path {} -d {}".format(webroot_path, domain)
subprocess.call(command.split())

# Verifica se o certificado foi criado com sucesso
if os.path.exists(cert_path + "fullchain.pem") and os.path.exists(cert_path + "privkey.pem"):
    print("Certificado criado com sucesso!")
else:
    print("Não foi possível criar o certificado.")

