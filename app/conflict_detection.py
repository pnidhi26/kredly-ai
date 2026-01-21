from typing import List, Dict


def detect_refund_conflict(
    docs: List[str],
    metas: List[Dict],
    distances: List[float],
    threshold: float = 0.7
):
    """
    Detect conflicts about gift card refundability.
    Returns None if no conflict, otherwise structured conflict info.
    """

    positive = []
    negative = []

    for doc, meta, dist in zip(docs, metas, distances):
        text = doc.lower()

        # Ignore weakly related sentences
        if dist > threshold:
            continue

        if "gift card" in text:
            if "not available" in text or "not refundable" in text:
                negative.append({
                    "file": meta["file"],
                    "text": doc
                })
            elif "available" in text or "refundable" in text:
                positive.append({
                    "file": meta["file"],
                    "text": doc
                })

    if positive and negative:
        return {
            "type": "refund_policy_conflict",
            "positive": positive,
            "negative": negative
        }

    return None
