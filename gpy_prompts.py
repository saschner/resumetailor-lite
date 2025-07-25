# gpt_prompts.py
"""
Simple GPT prompt helper to rewrite resume bullets based on job keywords.
Run with OpenAI API or paste prompts manually in playground.
"""

import os
import openai

# Set your OPENAI_API_KEY in environment variables before running
openai.api_key = os.getenv("OPENAI_API_KEY")

def rewrite_bullet(bullet, keywords):
    prompt = f"""
    Rewrite this resume bullet to better match the following job keywords,
    using professional tone and concise wording. Keep the original meaning.

    Job Keywords: {', '.join(keywords)}

    Original Bullet: {bullet}

    Rewritten Bullet:
    """

    response = openai.Completion.create(
        engine="text-davinci-003",  # or use "gpt-3.5-turbo" with chat API if preferred
        prompt=prompt,
        max_tokens=100,
        temperature=0.5,
        n=1,
        stop=None,
    )

    rewritten = response.choices[0].text.strip()
    return rewritten

if __name__ == "__main__":
    # Example usage
    example_bullet = "Led asset audits across departments, improving accuracy by 25%"
    example_keywords = ["ServiceNow", "IT Asset Management", "process improvement"]

    new_bullet = rewrite_bullet(example_bullet, example_keywords)
    print("Original:", example_bullet)
    print("Rewritten:", new_bullet)
