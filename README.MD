# Manual de Uso - Discord Crypto Bot

## 📌 Sobre o Bot
Este bot foi desenvolvido para **farmar XP de forma automática no Discord**, simulando um usuário real digitando mensagens relacionadas ao mundo cripto. Ele é ideal para quem deseja subir de nível em servidores que possuem sistemas de XP baseados em atividade.

⚠️ **Importante**: Enquanto o bot estiver rodando, você **não poderá mexer no PC**, pois ele utiliza o teclado e cliques automáticos para enviar mensagens.

## 📌 Requisitos
Antes de rodar o bot, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x instalado ([Baixar Python](https://www.python.org/downloads/))
- Bibliotecas necessárias:
  ```sh
  pip install pyautogui keyboard
  ```

## 🚀 Como Usar

### 1️⃣ **Abra o Terminal ou Prompt de Comando**
Navegue até a pasta onde o bot está localizado. Exemplo:
```sh
cd C:\Users\SeuUsuario\Downloads\spambot
```

### 2️⃣ **Execute o bot**
Para iniciar o bot, use o comando:
```sh
python bot.py
```

O bot começará a enviar mensagens automaticamente no Discord.

### 3️⃣ **Parar o Bot**
Pressione a tecla `Space` no teclado para parar o bot a qualquer momento.

## 🔧 Como Alterar o Tempo Entre as Mensagens
Se quiser modificar o tempo de espera entre o envio das mensagens, edite o código do bot:

1. **Abra o arquivo** `bot.py` em qualquer editor de texto ou código.
2. **Encontre esta linha no código:**
   ```python
   time.sleep(300)  # Tempo de espera entre as mensagens (em segundos)
   ```
3. **Altere o valor** `300` para o tempo desejado, em segundos. Por exemplo:
   ```python
   time.sleep(120)  # Agora o bot enviará mensagens a cada 2 minutos
   ```
4. **Salve o arquivo** e execute o bot novamente.

## ⚠️ Observações
- O bot deve ser rodado com o Discord aberto e o cursor posicionado no campo de mensagens.
- **Você não poderá usar o PC enquanto o bot estiver em execução.** Ele controla o teclado e executa cliques automáticos.
- Certifique-se de que o terminal esteja rodando como **Administrador**, caso tenha problemas com permissões.
- O tempo de envio de mensagens é configurado para evitar banimentos, mas use com responsabilidade.

---

Caso tenha dúvidas, entre em contato! 🚀

