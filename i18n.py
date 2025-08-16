import locale

def format_currency(amount, currency=\"د.م\"):
    try:
        locale.setlocale(locale.LC_ALL, \"ar_MA.UTF-8\") # Moroccan Arabic locale
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, \"ar_MA\")
        except locale.Error:
            pass # Fallback to default locale if not found

    # Format with thousands separator and two decimal places
    formatted_amount = locale.format_string(\"%.2f\", amount, grouping=True)
    return f\"{formatted_amount} {currency}\"

def format_number(number):
    return str(number)



