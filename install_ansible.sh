#!/bin/bash

# Instala o Ansible via pip
echo "Instalando o Ansible..."
pip install ansible

# Verifica se o ssh-keygen está instalado e o instala se necessário
if ! command -v ssh-keygen &> /dev/null
then
    echo "ssh-keygen não encontrado. Instalando o OpenSSH..."
    sudo apt-get install -y openssh-client
fi

# Gera a chave SSH automaticamente
echo "Gerando chave SSH..."
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ""

echo "Instalação e configuração do Ansible concluídas."
