import json


def load_knowledge_base():
    with open("knowledge_base.json", "r", encoding="utf-8") as file:
        return json.load(file)


def classify_request(customer_request):
    request = customer_request.lower()

    urgent_keywords = [
        "burning",
        "smoke",
        "sparks",
        "electrical smell",
        "carbon monoxide",
        "96 degrees",
        "elderly",
        "infant"
    ]

    pricing_keywords = [
        "exactly how much",
        "final quote",
        "replacement cost",
        "repair cost"
    ]

    scheduling_keywords = [
        "reschedule",
        "appointment availability",
        "available tomorrow",
        "book an appointment"
    ]

    if any(keyword in request for keyword in urgent_keywords):
        return "ESCALATE"

    if any(keyword in request for keyword in pricing_keywords):
        return "ESCALATE"

    if any(keyword in request for keyword in scheduling_keywords):
        return "CLARIFY"

    return "ANSWER"


def process_request(customer_request, knowledge_base):
    decision = classify_request(customer_request)

    return {
        "customer_request": customer_request,
        "decision": decision
    }


if __name__ == "__main__":
    knowledge_base = load_knowledge_base()

    test_requests = [
        "What areas do you service?",
        "My AC is running but the house isn't getting cold.",
        "Can I reschedule my appointment?",
        "I smell something burning coming from my HVAC unit.",
        "Can you tell me exactly how much replacing my compressor will cost?"
    ]

    for request in test_requests:
        result = process_request(request, knowledge_base)
        print(result)
