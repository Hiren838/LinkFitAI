from fuzzywuzzy import fuzz

def compute_fit_score(candidate_snippet, job_keywords):
    score = 0
    breakdown = {}

    for key in job_keywords:
        match = fuzz.partial_ratio(key.lower(), candidate_snippet.lower())
        score += match / 20  # Normalize match (5 = perfect score per keyword)
        breakdown[key] = round(match / 20, 2)

    total_score = round(min(score, 10), 2)  # Max out at 10
    return total_score, breakdown
