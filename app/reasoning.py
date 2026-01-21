import re


def answer_numerical_question(question, structured_data):
    q = question.lower()

    if "refund window" in q or "how many days" in q:
        for item in structured_data:
            policy = item.get("refund_policy", {})
            days = policy.get("window_days")

            if days:
                return f"{days} days", True

    return None, False
