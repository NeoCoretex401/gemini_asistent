import os
import google.generativeai as genai
from colorama import Fore, Back, Style

genai.configure(api_key="YOUR_APIKEY") //dapatkan apikey -. https://aistudio.google.com/

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 5000,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Fungsi bersihkan layar
def clear_screen():
    # Bersihkan layar tergantung pada sistem operasi
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

def chat():
    print(Fore.BLUE + "Welcome! Please ask your question or type 'exit' to quit.")
    while True:
        user_input = input(Fore.YELLOW + "Masukkan teks: ")
        if user_input.lower() == "exit":
            print(Fore.RED + "Thank you, goodbye!")
            break
        elif user_input.lower() == "clean":
            clear_screen()
            continue  # Melanjutkan loop tanpa menjalankan respons model
        response = model.generate_content(user_input)
        print(Fore.BLUE + "GEMINI:")
        print(Fore.GREEN + response.text)

if __name__ == "__main__":
    chat()
