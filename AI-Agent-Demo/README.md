## Prototype Validation

The agent was tested using representative customer requests, adversarial phrasing, and novel conversational paraphrases designed to expose weaknesses in both rule-based and semantic intent handling.

### Development Progression

- Version 1 established the initial ANSWER / CLARIFY / ESCALATE decision framework.
- Adversarial testing identified weaknesses in scheduling, pricing, vulnerable-customer escalation, diagnosis requests, and conversational phrasing.
- Version 2 improved the rule-based classification layer based on observed failures.
- Version 3 improved verified-response retrieval for service-area questions, AC-not-cooling complaints, and thermostat issues.
- Version 4 introduced semantic intent recognition using Sentence Transformers (`all-MiniLM-L6-v2`) and cosine similarity to recognize novel customer phrasing beyond deterministic keyword matching.
- Version 5 integrated semantic intent recognition with governance controls and verified-information retrieval, creating an end-to-end governed agent pipeline.

### Semantic Intent Validation

The semantic classifier was tested against eight novel customer requests that differed from the examples used to define the intent categories.

Results:

- 6 of 8 novel requests were correctly classified.
- 2 requests fell below the confidence threshold and returned `UNKNOWN`.
- Neither low-confidence request was confidently misclassified.
- The confidence threshold was retained rather than lowered simply to increase classification coverage.

This demonstrates explicit uncertainty handling: when semantic confidence is insufficient, the system defaults to clarification rather than guessing.

### Governed Agent Pipeline

The final prototype uses the following architecture:

**Customer Request → Semantic Intent Recognition → Confidence Threshold → Governance Policy → Verified Information Retrieval → ANSWER / CLARIFY / ESCALATE**

Governance rules remain authoritative over semantic classification.

Examples include:

- Routine informational intents may proceed to verified-information retrieval.
- Scheduling requests return `CLARIFY` because the prototype has no access to live appointment availability.
- Pricing and definitive diagnosis requests return `ESCALATE`.
- Potential safety concerns return `ESCALATE` with safety-oriented guidance.
- Low-confidence semantic matches return `CLARIFY` rather than generating an unsupported answer.

During integration testing, semantic classification correctly recognized several novel customer phrasings, but the existing keyword-based response retrieval layer could not reliably consume those results. The retrieval architecture was therefore refactored so verified responses are selected by semantic intent rather than by repeating keyword matching downstream.

### Demonstrated Capabilities

The prototype demonstrates:

- Semantic intent recognition using sentence embeddings.
- Confidence-based uncertainty handling.
- Verified-information retrieval.
- Separation of language understanding from governance policy.
- Guardrails against unsupported pricing and definitive diagnosis.
- Human escalation for potentially dangerous or sensitive situations.
- Safe clarification when semantic confidence is insufficient.
- Adversarial and novel-phrasing testing.
- Iterative testing, failure analysis, remediation, and regression checking.

## Limitations

This remains a learning and portfolio prototype rather than a production system.

Current limitations include:

- Semantic intent recognition is based on a small manually defined set of intent examples.
- The prototype does not use large language model reasoning.
- It does not include retrieval-augmented generation (RAG).
- It has no live scheduling access.
- It has no CRM or production business-system integration.
- It does not include production-grade authentication, observability, monitoring, or safety infrastructure.
- Semantic similarity scores and thresholds would require substantially broader evaluation before real-world deployment.

The project is intended as a portfolio demonstration of responsible AI architecture, semantic intent recognition, governance controls, evaluation, uncertainty handling, verified-information retrieval, and human-escalation principles rather than a deployable production system.
