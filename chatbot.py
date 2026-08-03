import pandas as pd
from rapidfuzz import process 

# Load the CSV file
data = pd.read_csv("data.csv")
print(data)
print(data["QUESTIONS"])
print(data["ANSWERS"])

print("=== College Chatbot ===")
print("Type 'exit' to quit.\n")
print("=" * 40)
print("     College Intelligent Chatbot")
print("=" * 40)
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ").strip().lower()

    if user == "exit":
        print("Bot: Goodbye!")
        break

    found = False

    for index, row in data.iterrows():
        question = str(row["QUESTIONS"]).strip().lower()

        if user == question:
            print("Bot:", row["ANSWERS"])
            found = True        
            break

    if not found:
        questions = data["QUESTIONS"].astype(str).tolist()

    match = process.extractOne(user, questions)

    if match and match[1] >= 60:
        matched_question = match[0]
        answer = data.loc[data["QUESTIONS"] == matched_question, "ANSWERS"].values[0]
        print("Bot:", answer)
    else:
        print("Bot: Sorry, I don't know the answer.")
