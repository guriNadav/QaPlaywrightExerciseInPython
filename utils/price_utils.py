import re
from typing import Optional

def extract_price(price_text: str) -> Optional[float]:
    """Extract the highest numeric price from a string.
    Returns ``None`` if no price can be found.
    """
    if not price_text:
        return None
    cleaned = price_text.replace(",", "")
    matches = re.findall(r"\d+(?:\.\d+)?", cleaned)
    if not matches:
        return None
    prices = [float(num) for num in matches]
    return max(prices)
