import pyautogui
import time
import keyboard
import random

# Lista de mensagens curtas e aleatórias
frases = [
    "Good morning! Hope everyone has an amazing day filled with success!",
    "Let's go! Big things are coming, stay tuned!",
    "The future is bright, and we're just getting started! Who’s ready for the journey?",
    "Never underestimate the power of consistency. Small steps lead to big results!",
    "Keep the positive vibes up! Today might be the day that changes everything!",
    "Hard work, dedication, and a little bit of luck… that’s the formula for success!",
    "Opportunities don’t wait. If you see an open door, walk through it with confidence!",
    "Success comes to those who refuse to quit! Stay focused, stay hungry!",
    "Surround yourself with people who inspire you to grow and push your limits!",
    "Every great achievement started as a simple idea. Keep dreaming, keep building!",
    "Innovation happens when we step out of our comfort zones. Take the leap!",
    "Your only limit is the one you set for yourself. Dream big, take action!",
    "The best investment you can make is in yourself. Keep learning, keep evolving!",
    "Remember: those who stand still miss the wave! Keep moving forward!",
    "Nothing can resist continuous effort. Keep pushing, keep growing!",
    "Stay patient, stay persistent. The best things take time to build!",
    "Believe in yourself and your vision. Others will follow!",
    "Everything you want is on the other side of fear. Step forward with confidence!",
    "Consistency beats motivation. Show up every single day!",
    "Success is not an accident, it's the result of hard work and determination!",
    "Make today count! Each day is a chance to get closer to your goals!",
    "The road to success is always under construction. Keep going!",
    "One step at a time. Progress is still progress, no matter how small!",
    "The best time to start was yesterday. The second-best time is now!",
    "Chase your dreams with the same energy you chase distractions!",
    "Don't wait for the perfect moment, take the moment and make it perfect!",
    "Failure is just another step toward success. Learn, adapt, and keep moving!",
    "Your future self will thank you for the effort you put in today!",
    "Great things take time. Trust the process and stay focused!",
    "Winners focus on winning, losers focus on winners. Stay in your lane!",
    "Take risks, make mistakes, and grow. That's how success is built!",
    "Surround yourself with those who lift you higher!",
    "Your mindset determines your success. Keep it positive and powerful!",
    "Action beats hesitation. Do it now and refine later!",
    "The grind may be hard, but the results will be worth it!",
    "The only bad day is the one where you give up. Keep pushing!",
    "You're stronger than your excuses. Keep moving forward!",
    "Every moment is a fresh beginning. Start today with a winning mindset!",
    "If you’re not making mistakes, you’re not trying hard enough!",
    "Be the reason someone smiles today. Positivity is contagious!",
    "Work hard in silence, let your success make the noise!",
    "Small daily improvements lead to massive long-term results!",
    "Discipline is doing what needs to be done, even when you don’t feel like it!",
    "Your energy introduces you before you even speak. Make it count!",
    "No shortcuts to success. Only hustle, patience, and consistency!",
    "Visualize success and then go make it happen!",
]

# Função para simular a digitação de forma mais realista
def digitar_frase(frase):
    for char in frase:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.1))  # Tempo aleatório entre caracteres

# Função para verificar se a tecla 'space' foi pressionada
def check_for_stop():
    return keyboard.is_pressed('space')

# Aguarde 60 segundos antes de começar
time.sleep(5)

try:
    while True:
        if check_for_stop():  # Verifica se a tecla 'space' foi pressionada para parar o bot
            print("Bot parado!") 
            break

        # Sorteia uma frase aleatória
        frase_sorteada = random.choice(frases)

        # Envia a mensagem
        digitar_frase(frase_sorteada)

        # Pressiona "enter" para enviar a mensagem
        pyautogui.press('enter')

        # Aguarda 1 segundo para garantir que a mensagem tenha sido enviada
        time.sleep(1)

        # Aguarda 50 segundos antes de enviar a próxima mensagem
        print("Aguardando 50 segundos antes do próximo envio...")
        time.sleep(120)

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    print("Programa encerrado.")
