# 🌍 Real-Time Currency Converter (Python + Tkinter + API)

A clean and user-friendly **Currency Converter** application built using Python, Tkinter, and a live exchange rate API.  
It supports 160+ currencies, real-time conversion accuracy, currency swapping, conversion history, and more.

---

## 🚀 Features

- 🔁 **Live Currency Conversion**  
  Fetches and converts using real-time exchange rates.

- 💱 **Swap Currencies**  
  Instantly switch between "from" and "to" currencies.

- 📈 **Refresh Exchange Rates**  
  Get updated market values whenever needed.

- 🧾 **Conversion History**  
  Keeps track of all your past conversions within the session.

- 📋 **Copy Result**  
  Copy converted value directly to the clipboard.

- ✨ **Clean Tkinter UI**  
  Organized layout with dropdowns, buttons, and display sections.

- 🛡️ **Error Handling**  
  Prevents crashes from invalid inputs or API connectivity issues.

- ⏱️ **Last Updated Display**  
  Shows the timestamp of the latest exchange rate fetch.

---

## 🧠 How It Works

- The app fetches real-time currency data from  
  **https://api.exchangerate-api.com/v4/latest/USD**

- The conversion formula is handled internally:  
  ```
  amount_in_usd = amount / rate[from_currency]
  converted_amount = amount_in_usd * rate[to_currency]
  ```

- The Tkinter GUI displays:
  - Input amount
  - Source currency
  - Target currency
  - Converted output
  - Last update date
  - Conversion history

---

## ▶️ Usage

1. Install Python 3.10+
2. Install dependencies (only `requests`)
   ```bash
   pip install requests
   ```
3. Run the application:
   ```bash
   python currency_converter.py
   ```

---

## 💡 Improvements You Can Add Later

- Export history to CSV  
- Integrate live graphs of currency trends  
- Add dark/light theme toggle  
- Flag icons for each currency  
- Multi-window layout  
- Offline cache mode  

---

## 🤝 Contributing

Pull requests and feature suggestions are always welcome!

---

## ⭐ Support

If this project helped you, please give it a **⭐ star on GitHub**!

