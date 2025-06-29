from serpapi import GoogleSearch

def search_linkedin_profiles_google(job_title, location, num_results=10):
    params = {
        "engine": "google",
        "q": f'site:linkedin.com/in "{job_title}" "{location}"',
        "num": num_results,
        "api_key": "API IS HERE" 
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    profiles = []
    for result in results.get("organic_results", []):
        link = result.get("link")
        if link and link.startswith("https://www.linkedin.com/in/"):
            profiles.append({
                "linkedin_url": link,
                "title": result.get("title", ""),
                "snippet": result.get("snippet", "")
            })

    return profiles

# profiles = search_linkedin_profiles_google("Data Scientist", "San Francisco")
# for profile in profiles:
#     print(profile)
