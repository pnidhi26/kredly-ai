def compute_consensus(metas, distances, threshold=0.6):
    file_hits = {}

    for meta, dist in zip(metas, distances):
        if dist <= threshold:
            fname = meta["file"]
            file_hits[fname] = file_hits.get(fname, 0) + 1

    count = len(file_hits)

    if count >= 3:
        level = "strong"
    elif count == 2:
        level = "partial"
    elif count == 1:
        level = "weak"
    else:
        level = "none"

    return {
        "level": level,
        "files": list(file_hits.keys()),
        "count": count
    }
