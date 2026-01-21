from typing import List, Dict


def answer_numerical_question(
    question: str,
    structured_data: List[Dict]
):
    """
    Try to answer numeric / factual questions from structured data.
    Returns (answer, handled: bool)
    """

    q = question.lower()

    # ---- Refund policy questions ----
    for item in structured_data:
        policy = item.get("refund_policy", {})

        if "refund window" in q or "how many days refund" in q:
            if policy.get("refund_window_days") is not None:
                return (
                    f"The refund window is {policy['refund_window_days']} days.",
                    True
                )

        if "processing time" in q:
            if policy.get("processing_days") is not None:
                return (
                    f"Refunds are processed within {policy['processing_days']} days.",
                    True
                )

    # ---- Bank transaction questions ----
    transactions = []
    for item in structured_data:
        transactions.extend(item.get("transactions", []))

    if "total debit" in q or "total spent" in q:
        total = sum(
            abs(t["amount"]) for t in transactions if t["amount"] < 0
        )
        return (f"Total debit amount is {total:.2f}", True)

    if "total credit" in q or "total income" in q:
        total = sum(
            t["amount"] for t in transactions if t["amount"] > 0
        )
        return (f"Total credit amount is {total:.2f}", True)

    if "starbucks" in q:
        total = sum(
            abs(t["amount"])
            for t in transactions
            if "starbucks" in t["description"].lower()
        )
        return (f"Total spent at Starbucks is {total:.2f}", True)

    return (None, False)
