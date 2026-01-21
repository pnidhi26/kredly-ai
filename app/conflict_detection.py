def detect_refund_conflict(docs, metas, distances):
    positive = []
    negative = []

    for doc, meta in zip(docs, metas):
        text = doc.lower()

        if "refund" in text and "gift card" in text:
            if "not available" in text:
                negative.append({"file": meta["file"], "text": doc})
            elif "available" in text:
                positive.append({"file": meta["file"], "text": doc})

    if positive and negative:
        return {"positive": positive, "negative": negative}

    return None
