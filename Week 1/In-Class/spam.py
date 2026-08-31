spam_prediction = 0.95

if spam_prediction >= 0.85:
    classification = "BLOCKED"
elif spam_prediction >= 0.50:
    classification = "HUMAN_REVEIW"
else:
    classification = "APPROVED"

print(classification)