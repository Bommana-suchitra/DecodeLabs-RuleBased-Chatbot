import re


def sanitize_input(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s+\-*/]", "", text)
    return text


def calculate_expression(expression):
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception:
        return "Invalid calculation."


def extract_name(user_input):
    if "my name is" in user_input:
        return user_input.replace("my name is", "").strip()
    return None