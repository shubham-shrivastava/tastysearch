def average_rating(reviews):
    total = sum(r["rating"] for r in reviews)
    return total / len(reviews)


def top_reviews(reviews, n=5):
    return sorted(reviews, key=lambda r: r["rating"])[:n]
