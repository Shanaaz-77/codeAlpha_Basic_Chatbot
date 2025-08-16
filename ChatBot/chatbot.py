import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import random

# Send message function
def send_message():
    user_message = user_entry.get("1.0", tk.END).strip()
    if user_message:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"You: {user_message}\n", "user")
        
        bot_reply = get_bot_reply(user_message)
        chat_area.insert(tk.END, f"Bot: {bot_reply}\n\n", "bot")
        
        chat_area.config(state=tk.DISABLED)
        chat_area.see(tk.END)
        user_entry.delete("1.0", tk.END)

# Bot reply logic with random responses
def get_bot_reply(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return random.choice([
            "Hello! 👋 How can I help you?",
            "Hi there! 😊 What’s up?",
            "Hey! 👋 How's it going?"
        ])
    
    elif user_input in ["how are you", "how r u", "how are u"]:
        return "I'm fine, thanks! 😊."
            
    
    elif user_input in ["bye", "goodbye"]:
        return random.choice([
            "Goodbye! Have a great day! 👋",
            "Bye! Take care! 🌟"
        ]) 
    elif user_input in ["your name", "what's your name"]:
        return "I'm a codealpha basic ChatBot."
    
    elif user_input in ["what can you do", "help"]:
        return "I can answer simple questions."
    
    elif user_input == "time":
        return "⏰ Current time is " + datetime.now().strftime("%I:%M %p")
    
    elif user_input == "date":
        return "📅 Today's date is " + datetime.now().strftime("%d-%m-%Y")
    
    elif user_input in ["creator", "who made you"]:
        return "I was created by Shaik Shanaaz."
    
    elif user_input in ["joke", "tell me a joke"]:
        jokes = [
            "Why did the computer go to the doctor? Because it caught a virus! 🖥️🤒",
            "Why was the math book sad? Because it had too many problems. 📚😢",
            "Why was the computer cold? It left its Windows open! 🥶",
        ]
        return random.choice(jokes)
    
    else:
        return "Sorry i didn't understand that."

# Main window
root = tk.Tk()
root.title("Chatbot")
root.geometry("450x550")
root.configure(bg="#62c1f0")

# Chat display area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#db2583", fg="white",
                                      font=("Arial", 12), height=20, width=50)
chat_area.pack(padx=10, pady=10)
chat_area.config(state=tk.DISABLED)

# Frame for input and button
input_frame = tk.Frame(root, bg="#ea96d4")
input_frame.pack(pady=10)

# Larger text box for user input
user_entry = tk.Text(input_frame, height=2, width=35, font=("Arial", 12), bg="#FDDAE8", fg="black")
user_entry.grid(row=0, column=0, padx=5)

# Send button
send_button = tk.Button(input_frame, text="Send", command=send_message, bg="#4CAF50", fg="white",
                        font=("Arial", 12, "bold"), relief="raised", width=8, height=2)
send_button.grid(row=0, column=1, padx=5)

root.mainloop()
