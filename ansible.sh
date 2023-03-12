# Instala o módulo Chocolatey (se ainda não estiver instalado)
if (!(Get-Command choco -ErrorAction SilentlyContinue)) {
    Set-ExecutionPolicy Bypass -Scope Process -Force
    iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
}
# Rodar em Modo Administrator
# Instala o Ansible usando o Chocolatey
choco install ansible -y
