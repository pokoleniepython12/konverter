from tkinter import *
from tkinter import messagebox as mb
import requests
from tkinter import ttk


def exchange():
    code=combobox.get()
    if code:
        try:
            response=requests.get("https://open.er-api.com/v6/latest/USD")
            data=response.json()
            print(data)
            if code in data["rates"]:
                exchange_rates=data["rates"][code]
                mb.showinfo("Курс обмена",
                            f"Курс к доллару: {exchange_rates} {code} за 1 доллар")
        except Exception as error:
            mb.showerror("Ошибка",f"Произошла ошибка {error}")



window=Tk()
window.title("Конвертер валют")
window.geometry("400x500")

ttk.Label(text="Введите код валюты").pack(pady=10)


popular_cur = ["EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "RUB", "KZT",
"UZS"]
combobox=ttk.Combobox(values=popular_cur)
combobox.pack(pady=10)

ttk.Button(text="Получить курс обмена к доллару", command=exchange).pack(pady=10)

window.mainloop()