import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

def translate_text():
    try:
        text = text_box.get("1.0", tk.END).strip()

        lang_dict = {
            "Hindi": "hi",
            "French": "fr",
            "Spanish": "es",
            "German": "de",
            "English": "en",
            "Arabic": "ar",
            "Japanese": "ja",
            "Russian": "ru"
        }

        target_lang = lang_dict[target_combo.get()]

        translated = GoogleTranslator(
            source='auto',
            target=target_lang
        ).translate(text)

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, translated)

    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Error: {e}")

def save_translation():
    try:
        text = output_box.get("1.0", tk.END).strip()

        with open("translations.txt", "a", encoding="utf-8") as file:
            file.write(text + "\n\n")

        output_box.insert(tk.END, "\n\n✓ Translation Saved")

    except Exception as e:
        output_box.insert(tk.END, f"\nError: {e}")

root = tk.Tk()
root.title(" AI Language Translator")
root.geometry("700x550")

title = tk.Label(
    root,
    text="AI Language Translator",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

tk.Label(root, text="Enter Text").pack()

text_box = tk.Text(root, height=6, width=70)
text_box.pack(pady=5)

tk.Label(root, text="Select Target Language").pack()

target_combo = ttk.Combobox(
    root,
    values=[
        "Hindi",
        "French",
        "Spanish",
        "German",
        "English",
        "Arabic",
        "Japanese",
        "Russian"
    ]
)

target_combo.pack(pady=5)
target_combo.current(0)

translate_btn = tk.Button(
    root,
    text="Translate",
    command=translate_text
)
translate_btn.pack(pady=10)

save_btn = tk.Button(
    root,
    text="Save Translation",
    command=save_translation
)
save_btn.pack(pady=5)

tk.Label(root, text="Translated Text").pack()

output_box = tk.Text(root, height=8, width=70)
output_box.pack(pady=10)

root.mainloop()