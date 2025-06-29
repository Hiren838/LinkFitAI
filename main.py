from search_profiles import search_linkedin_profiles_google
from fit_score import compute_fit_score
from message_generator import generate_message
import json

job = {
    "title": "Data Scientist",
    "location": "San Francisco",
    "company": "AI Corp",
    "keywords": ["machine learning", "python", "data analysis"]
}

results = search_linkedin_profiles_google(job["title"], job["location"])

scored_candidates = []
for candidate in results:
    score, breakdown = compute_fit_score(candidate['snippet'], job["keywords"])
    message = generate_message(candidate, job["title"], job["company"])
    candidate.update({
        "fit_score": score,
        "score_breakdown": breakdown,
        "outreach_message": message
    })
    scored_candidates.append(candidate)

with open("output/scored_candidates.json", "w") as f:
    json.dump(scored_candidates, f, indent=2)
