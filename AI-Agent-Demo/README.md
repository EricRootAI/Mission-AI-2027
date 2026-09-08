# Customer Service AI Agent

## Project Overview

This project demonstrates a responsible AI customer-service agent for a fictional HVAC company, Summit Climate Systems.

The agent is designed to:

- Answer routine customer questions using verified company information.
- Recognize when available information is insufficient.
- Avoid inventing company policies, pricing, or technical information.
- Identify potentially urgent customer situations.
- Escalate appropriate cases to a human representative.

## Decision Framework

Every customer request should result in one of three primary actions:

1. ANSWER — The request can be answered using verified information.
2. CLARIFY — Additional information is required before the request can be handled safely or accurately.
3. ESCALATE — The request requires human review or involves an urgent or unsupported situation.

## Development Status

**Sprint 1:** Business scenario and decision framework defined.
