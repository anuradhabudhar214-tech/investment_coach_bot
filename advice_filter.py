def is_advice_request(message: str) -> bool:
    advice_keywords = [
        "buy",
        "sell",
        "invest",
        "best stock",
        "which stock",
        "should i buy",
        "recommend",
        "intraday",
        "profit",
        "returns",
        "safe stock",
        "multibagger"
    ]

    message = message.lower()

    for keyword in advice_keywords:
        if keyword in message:
            return True

    return False
