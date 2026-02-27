# ai_service.py
import requests
from serpapi import GoogleSearch
from JARVIS.conapi import API_KEY, DEEPSEEK_URL, SERP_API_KEY

def get_real_time_info(query):
    params = {"engine": "google", "q": query, "api_key": "b617196eb05a566be4e3ff71f20180ca4ca2c16ce192130209a195d0fcec2dd0"}
    search = GoogleSearch(params)
    results = search.get_dict()
    if "answer_box" in results:
        return results["answer_box"].get("answer") or results["answer_box"].get("snippet")
    if "organic_results" in results:
        return results["organic_results"][0].get("snippet")
    return "No live info found."

def get_ai_response(prompt):
    headers = {"Authorization": f"Bearer {"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"}", "Content-Type": "application/json"}
    data = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [
            {"role": "system", "content": "You are Jarvis, an intelligent AI assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(DEEPSEEK_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    return "Could not connect to AI service."
