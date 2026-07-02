from ai_engine import get_ai_analysis

test_summary = "Health: Warning, Errors: 3, Top Error: Connection Refused"

print("AI responding... plz wait...")
response = get_ai_analysis(test_summary)
print("\n--- AI Response ---\n")
print(response)

