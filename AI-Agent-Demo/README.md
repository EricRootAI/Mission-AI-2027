## Prototype Validation

The agent was tested using both representative customer requests and adversarial phrasing designed to expose weaknesses in the initial rule-based implementation.

### Development Progression

- Version 1 established the initial ANSWER / CLARIFY / ESCALATE decision framework.
- Adversarial testing identified weaknesses in scheduling, pricing, vulnerable-customer escalation, diagnosis requests, and conversational phrasing.
- Version 2 improved the classification layer based on observed failures.
- Version 3 improved verified-response retrieval for service-area questions, AC-not-cooling complaints, and thermostat issues.

### Validation Results

The final Version 3 adversarial test produced:

- 9 requests handled as intended.
- 1 unsupported request handled with a safe fallback rather than an invented answer.

The prototype demonstrates:

- Verified-information retrieval.
- Guardrails against unsupported pricing and diagnosis.
- Human escalation for potentially dangerous or sensitive situations.
- Safe fallback behavior when verified information is unavailable.
- Iterative testing and remediation based on observed failure modes.

## Limitations

This prototype uses deterministic keyword-based rules and is intentionally limited.

It does not yet include:

- Semantic intent recognition.
- Large language model reasoning.
- Retrieval-augmented generation.
- Live scheduling access.
- CRM integration.
- Production-grade safety or monitoring.

The project is intended as a portfolio demonstration of responsible AI design, evaluation, and human-escalation principles rather than a deployable production system.
