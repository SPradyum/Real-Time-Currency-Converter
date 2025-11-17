import requests
import tkinter as tk
from tkinter import ttk, messagebox
import re
from datetime import datetime

# ============================================================
#                REAL-TIME CURRENCY CONVERTER CLASS
# ============================================================

class RealTimeCurrencyConverter():
    def __init__(self, url):
        try:
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']
            self.date = self.data["date"]
        except:
            messagebox.showerror("Error", "Unable to fetch data. Check your internet connection.")
            self.currencies = {"USD": 1}
            self.date = "N/A"

    def convert(self, from_currency, to_currency, amount):
        if from_currency != "USD":
            amount = amount / self.currencies[from_currency]
        return round(amount * self.currencies[to_currency], 4)

# ============================================================
#                        MAIN APP CLASS
# ============================================================

class App(tk.Tk):

    def __init__(self, converter):
        super().__init__()
        self.converter = converter

        self.title("Currency Converter")
        self.geometry("650x500")
        self.configure(bg="#0d1117")
        self.resizable(False, False)

        self._create_styles()
        self._create_ui()
        self.history = []

    # ------------------------ STYLES -------------------------
    def _create_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("TLabel", background="#0d1117", foreground="white", font=("Segoe UI", 11))
        style.configure("TCombobox", padding=5, relief="flat", borderwidth=0, font=("Segoe UI", 11))
        style.configure("TButton", padding=6, font=("Segoe UI", 10, "bold"))
        style.map("TButton", background=[("active", "#238636")])

    # ------------------------ UI SETUP ------------------------
    def _create_ui(self):
        title = ttk.Label(self, text="🌐 Real-Time Currency Converter 💰", font=("Segoe UI", 18, "bold"), foreground="#58a6ff")
        title.pack(pady=10)

        subtitle = ttk.Label(self, text=f"Last Updated: {self.converter.date}", foreground="#8b949e")
        subtitle.pack()

        # Frame container
        frame = tk.Frame(self, bg="#161b22")
        frame.pack(pady=20, padx=20, fill="x")

        # Currency dropdowns
        currency_list = list(self.converter.currencies.keys())

        self.from_currency = ttk.Combobox(frame, values=currency_list, width=15, state="readonly")
        self.from_currency.set("INR")
        self.from_currency.grid(row=0, column=0, padx=10, pady=10)

        swap_btn = ttk.Button(frame, text="⇆ Swap", command=self.swap)
        swap_btn.grid(row=0, column=1, padx=10)

        self.to_currency = ttk.Combobox(frame, values=currency_list, width=15, state="readonly")
        self.to_currency.set("USD")
        self.to_currency.grid(row=0, column=2, padx=10)

        # Amount Entry
        self.amount_entry = tk.Entry(frame, font=("Segoe UI", 14), justify="center", width=15, bd=0, bg="#0d1117", fg="white", insertbackground="white")
        self.amount_entry.grid(row=1, column=0, columnspan=3, pady=15)

        # Convert Button
        convert_btn = ttk.Button(frame, text="Convert", command=self.convert)
        convert_btn.grid(row=2, column=0, columnspan=3, pady=10)

        # Output Box
        self.output_label = tk.Label(frame, text="Converted Value Will Appear Here", bg="#161b22", fg="#58a6ff", font=("Segoe UI", 14, "bold"))
        self.output_label.grid(row=3, column=0, columnspan=3, pady=10)

        # Extra Buttons
        btn_frame = tk.Frame(self, bg="#0d1117")
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Copy", command=self.copy_output).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="Refresh Rates", command=self.refresh_rates).grid(row=0, column=1, padx=10)
        ttk.Button(btn_frame, text="Clear", command=self.clear_all).grid(row=0, column=2, padx=10)

        # History List
        history_title = ttk.Label(self, text="Conversion History", foreground="#58a6ff")
        history_title.pack(pady=5)

        self.history_list = tk.Listbox(self, width=50, height=8, bg="#161b22", fg="white", bd=0, font=("Consolas", 10))
        self.history_list.pack()

        # Status Bar
        self.status = tk.Label(self, text="Ready", bg="#0d1117", fg="#8b949e", anchor="w")
        self.status.pack(side="bottom", fill="x")

    # ------------------------ FUNCTIONS -------------------------
    def convert(self):
        try:
            amount = float(self.amount_entry.get())
        except:
            messagebox.showwarning("Invalid Input", "Please enter a valid amount.")
            return

        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()

        result = self.converter.convert(from_curr, to_curr, amount)
        self.output_label.config(text=f"{amount} {from_curr} = {result} {to_curr}")
        self.status.config(text="Converted Successfully")

        # Add to history
        entry = f"{amount} {from_curr} → {result} {to_curr}"
        self.history.append(entry)
        self.history_list.insert(tk.END, entry)

    def swap(self):
        a = self.from_currency.get()
        b = self.to_currency.get()

        self.from_currency.set(b)
        self.to_currency.set(a)

        self.status.config(text="Currencies Swapped")

    def refresh_rates(self):
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        self.converter = RealTimeCurrencyConverter(url)
        messagebox.showinfo("Success", "Exchange rates updated successfully!")
        self.status.config(text="Rates Refreshed")

    def clear_all(self):
        self.amount_entry.delete(0, tk.END)
        self.output_label.config(text="Converted Value Will Appear Here")
        self.history_list.delete(0, tk.END)
        self.status.config(text="Cleared")

    def copy_output(self):
        value = self.output_label.cget("text")
        self.clipboard_clear()
        self.clipboard_append(value)
        self.status.config(text="Copied to Clipboard")

# ============================================================
#                    RUN APPLICATION
# ============================================================

if __name__ == "__main__":
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    converter = RealTimeCurrencyConverter(url)
    App(converter).mainloop()
