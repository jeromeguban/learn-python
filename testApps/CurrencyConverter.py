import tkinter as tk
import tkinter.ttk as ttk
import requests

# https://api.exchangeratesapi.io/latest?base=USD&symbols=USD,INR
base_url = "https://api.apilayer.com/currency_data/convert"


def convert_pressed():
    amount = input_text.get()
    from_curr = source_value.get()
    to_curr = target_value.get()
    headers = {
        "apikey": "6TDfsfm40OAFy5Kzigzyfzov7BbW2yes"
    }
    main_url = base_url + "?to=" + to_curr + "&from=" + from_curr + "&amount=" + amount
    req = requests.get(main_url,headers=headers)
    result = req.json()
    # print(result)
   
    
    from_result = result["result"]
    to_result = result["result"]
    converted_amount = round(float(amount) * to_result, 2)
    conversion_label.config(text=str(converted_amount) + " " + to_curr)


if __name__ == '__main__':
    main_window = tk.Tk()
    main_window.title("Currency converter")
    main_window.geometry("350x200")

    intro_label = tk.Label(main_window, text="Welcome to Live Currency Converter",
                           fg="white", bg="blue", relief=tk.RAISED, borderwidth=3)
    intro_label.config(font=("Courier", 15, "bold"))
    main_window.grid_columnconfigure(0, weight=1)
    intro_label.grid(row=1)

    input_text = tk.StringVar()
    currency_field = tk.Entry(main_window, justify="right", textvariable=input_text)
    currency_field.grid(row=2, padx=5, pady=5)

    country_code = ["PHP","INR", "USD", "CAD", "CNY", "DKK", "EUR"]
    source_value = tk.StringVar()
    source_value_selection = ttk.Combobox(main_window, values=country_code,
                                          textvariable=source_value)
    source_value_selection.current(0)
    source_value_selection.grid(row=3)

    target_value = tk.StringVar()
    target_value_selection = ttk.Combobox(main_window, values=country_code,
                                          textvariable=target_value)
    target_value_selection.current(1)
    target_value_selection.grid(row=4)

    convert_button = tk.Button(main_window, text="Convert", height=1, width=7,
                               command=lambda: convert_pressed())
    convert_button.grid(row=5)

    conversion_label = tk.Label(text="")
    conversion_label.grid(row=6)

    main_window.mainloop()
