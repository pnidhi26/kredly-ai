import re
from typing import Dict, List

def extract_refund_policy(text: str) -> Dict:
    """
    Extract structured data from a refund policy document.
    Rule-based, deterministic, explainable.
    """

    data = {
        "refund_window_days": None,
        "processing_days": None,
        "gift_cards_refundable": None,
        "support_email": None,
    }

    # Refund window
    m = re.search(r"within (\d+) days", text, re.IGNORECASE)
    if m:
        data["refund_window_days"] = int(m.group(1))

    # Processing time
    m = re.search(r"processed within (\d+) (business )?days", text, re.IGNORECASE)
    if m:
        data["processing_days"] = int(m.group(1))

    # Gift cards
    if "not available for digital gift cards" in text.lower():
        data["gift_cards_refundable"] = False

    # Email
    m = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    if m:
        data["support_email"] = m.group(0)

    return data


def extract_bank_transactions(text: str) -> List[Dict]:
    """
    Extract bank transactions from statement-like text.
    Very common fintech pattern.
    """

    transactions = []

    lines = text.splitlines()
    for line in lines:
        # Example line:
        # 2024-01-12 Starbucks -5.75 1200.50
        m = re.search(
            r"(\d{4}-\d{2}-\d{2})\s+(.*?)\s+(-?\d+\.\d{2})\s+(\d+\.\d{2})",
            line
        )

        if m:
            transactions.append({
                "date": m.group(1),
                "description": m.group(2),
                "amount": float(m.group(3)),
                "balance": float(m.group(4)),
            })

    return transactions
