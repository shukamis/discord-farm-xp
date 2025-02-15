import pyautogui
import time
import keyboard
import random

# List of messages with crypto context
phrases = [
    "GM fam! Another day, another chance to stack sats! LFG!",
    "Bull or bear, real degens always find a way! Who’s trading today?",
    "WAGMI, just keep stacking and vibing!",
    "DCA all day, never chasing tops! Smart money moves!",
    "Remember, not your keys, not your coins! Stay safe out there!",
    "Patience = gains. The best trades take time!",
    "Airdrop season is coming! Who’s hunting the next big one?",
    "Layer 2 is the future! Who’s already deep into zk-rollups?",
    "Who’s farming those sweet sweet APYs today?",
    "Always DYOR! Don’t be exit liquidity, anon!",
    "Bear market builds legends. Who’s here for the long game?",
    "NGMI if you panic sell every dip! Stay strong, anon!",
    "The whales are playing games. Watch the order books!",
    "BTC or ETH, or are you all in on alts? What’s the play?",
    "On-chain alpha never lies! Time to do some wallet digging!",
    "The bull run is inevitable. Just a matter of time!",
    "Who’s still holding their NFTs? Diamond hands or paper hands?",
    "Wen moon? Wen Lambo? Only time will tell!",
    "Crypto Twitter is wild today. Who’s got the best takes?",
    "CT influencers shilling again? Careful out there, anon!",
    "Staking vs farming – which one’s the real passive income king?",
    "Nothing like a good dip to buy more bags! BTFD!",
    "Big news incoming? Time to load up! LFG!",
    "Just another 1000x gem waiting to be discovered! Who’s got alpha?",
    "WAGMI only if you survive the bear market!",
    "If you’re reading this, you’re still early!",
    "The market moves fast, stay ahead or get left behind!",
    "GM, GN, and everything in between – 24/7 grind!",
    "NFTs dead? Lol, just wait till the next cycle!",
    "You either make it or you become exit liquidity. Choose wisely!",
    "One good play can change your whole portfolio! LFG!",
    "Crypto never sleeps, and neither do true degens!",
    "Who else checking their portfolio 100 times a day?",
    "Regulations incoming! Will it be good or bad for the space?",
    "New narrative, new gains! What’s the next big trend?",
    "The best time to buy was yesterday, the second-best time is now!",
    "Bridge risk is real! Stay safe when moving funds around!",
    "Sentiment flips faster than a 5-minute chart! Be ready!",
    "Crypto is just TradFi but with better memes!",
    "Making it in crypto isn’t just about money, it’s about freedom!",
    "Those who build now will be the ones winning next cycle!",
    "Bulls make money, bears make money, pigs get slaughtered!",
    "Alphas don’t share alpha for free. Who’s got the real gems?",
    "Crypto maxis vs multi-chain believers – who’s winning?",
    "Liquidity is king! Don’t get rugged in low caps!",
    "Big brain plays only! What’s the move this week?",
    "Another day, another opportunity. Stay sharp!",
    "The best communities stick together! We’re all gonna make it!",
    "High risk, high reward – but only if you survive the volatility!",
]

def type_phrase(phrase):
    for char in phrase:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.1))

def check_for_stop():
    return keyboard.is_pressed('space')

def random_click():
    pyautogui.click()
    time.sleep(random.uniform(1, 3))

time.sleep(5)

try:
    while True:
        remaining_phrases = phrases.copy()
        random.shuffle(remaining_phrases)

        while remaining_phrases:
            if check_for_stop():
                print("Bot stopped!")
                break

            selected_phrase = remaining_phrases.pop()
            type_phrase(selected_phrase)
            pyautogui.press('enter')
            
            random_click()
            
            time.sleep(1)
            print("Waiting 300 seconds before the next message...")
            time.sleep(300)
        
        if check_for_stop():
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Program terminated.")
