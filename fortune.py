# fortune.py (v1.0)
print("🔮 Welcome to Piyush Mishra's Fortune Teller (21JE0654) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ")

if mood.lower() == "happy":
    print("✨ Your fortune: Great things await you, Piyush! Keep smiling. ✨")
elif mood.lower() == "sad":
    print("💧 Your fortune: Storms don't last forever. Better days are ahead.")
elif mood.lower() == "neutral":
    print("🌀 Your fortune: Stay curious — surprises are on the horizon.")
else:
    print("Hmm... that's a mood I don't recognize. Try again later!")