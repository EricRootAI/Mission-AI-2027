# AI Agent Governance & Deployment Readiness Review

## Summit Climate Systems Customer Service AI Agent

### Purpose

This review evaluates the governance controls, operational risks, human oversight requirements, and deployment readiness of the Summit Climate Systems Customer Service AI Agent prototype.

### 1. Autonomous vs. Human Decisions
The agent should be allowed to respond autonomously when a customer request matches a verified and approved response path within its existing decision framework. In cases such as basic troubleshooting, business hours, or service-area questions, the agent can provide information without human approval because the response is drawn from predefined, validated knowledge and does not require diagnosis, pricing authority, or policy interpretation.

Human review should not be required for every routine interaction, because doing so would remove much of the efficiency benefit of the system. However, autonomous responses should remain limited to clearly defined low-risk scenarios.

If a customer reports a potential safety hazard, such as a burning smell, smoke, sparks, or visible electrical damage, the agent should immediately move the interaction into the ESCALATE path.

The agent may provide approved immediate safety guidance and gather limited information needed to support the human handoff, such as whether smoke is present or whether there are other signs of an active hazard. It should not attempt to diagnose the equipment failure or continue routine troubleshooting.

This boundary exists because the consequences of an incorrect recommendation are substantially higher in a potential safety event. In these situations, human judgment and established emergency procedures take priority over the efficiency of autonomous resolution.

Final repair pricing should remain a human-controlled decision. Even if the agent has access to general pricing information, it should not represent an estimated or historical price as a final customer quote.

The final cost of a repair may depend on factors the agent cannot independently assess, including equipment condition, labor requirements, additional parts, applicable rebates or incentives, and other costs discovered during inspection. Material and equipment pricing may also change because of supply-chain conditions, tariffs, vendor pricing, or other market factors.

The agent may eventually be permitted to provide clearly identified general pricing information if that information comes from a current, verified source. However, final pricing should require human assessment and authorization.

When a customer requests a definitive repair price, the agent should follow the ESCALATE path rather than creating an unsupported expectation.

#### Governance Principle

The level of autonomy granted to the agent should be proportional to the risk and consequence of an incorrect action. Low-risk, verified informational requests may be handled autonomously. As uncertainty, safety risk, financial consequence, or the need for professional judgment increases, the system should transition from ANSWER to CLARIFY or ESCALATE and preserve human authority.

### 2. Key Risks

#### Contextual Health and Safety Risk

Risk should be evaluated using the context of the customer's situation, not only explicit hazard keywords. A routine equipment failure can become a health and safety concern when vulnerable individuals or dangerous environmental conditions are involved.

For example, an air-conditioning failure in a home that has reached 89 degrees with an elderly resident present should trigger an immediate ESCALATE response. The agent should recognize that age, indoor temperature, and the loss of cooling collectively increase the potential health risk.

In these circumstances, the agent should prioritize rapid human intervention rather than continuing routine troubleshooting. The absence of smoke, fire, or an electrical hazard does not mean that the situation is low risk.

#### Risk Principle

Risk classification should consider the combination of circumstances surrounding a request. Individual details that appear low risk in isolation may create a high-risk situation when considered together. The agent should therefore be designed to recognize contextual risk and escalate when the potential consequence of delay or an incorrect response becomes significant.

#### Privacy and Unauthorized Data Collection Risk

The agent should collect and retain only customer information that is necessary and explicitly authorized for the service workflow. Information such as a customer's name, service address, and contact information may be appropriate when required to create or manage a service request.

If a customer attempts to provide sensitive information that the agent is not authorized to process, such as payment-card information, the agent should tell the customer not to provide that information and redirect them to the company's approved payment process.

Whenever technically possible, unauthorized sensitive information should be prevented from being stored, logged, or unnecessarily reproduced in subsequent responses.

For example, the agent could inform the customer:

"Only the information necessary to arrange your service request will be retained. Payment information is not collected through this chat and will be handled through the company's approved payment process."

The system should follow the principle of data minimization: collect only what is required, retain only what is authorized, and avoid exposing sensitive customer information unnecessarily.

#### Knowledge Accuracy and Change-Control Risk

An agent can provide an incorrect response even when it functions exactly as designed if its approved knowledge source is outdated. For that reason, maintaining the accuracy of the agent's knowledge must be treated as an operational responsibility, not solely as a technical responsibility.

Each category of business information should have a designated human owner. For example, the team responsible for establishing business hours should also be responsible for ensuring that finalized scheduling changes are communicated to the AI system.

When a change is approved, the corresponding knowledge should be updated with its effective date before or as part of implementing the operational change. This helps prevent the agent from continuing to provide information that was previously correct but is no longer valid.

The organization should also establish periodic reviews of AI-accessible knowledge to identify outdated information that may not have been captured through the normal change process.

This creates accountability for both the information itself and the process used to keep the agent's verified knowledge current.

### 3. Human Oversight and Escalation

#### Closed-Loop Human Escalation

When the agent determines that human intervention is required, escalation should create an operational handoff rather than simply instructing the customer to contact someone else.

The customer should be clearly informed that the request has been escalated, why human assistance is required when appropriate, and what they should expect next. For routine escalations, the company should establish an approved response-time window that the agent may communicate to the customer.

The customer should receive a case or reference number and, when appropriate, the direct contact information for customer service. This gives the customer a way to follow up or leave a message while referencing the existing case rather than beginning the interaction again.

The human representative receiving the escalation should have access to the relevant conversation history, customer contact information, reason for escalation, case number, and assigned priority level. The system should also record that the escalation was successfully delivered so that requests do not disappear between the AI and human workflow.

Escalation priority should reflect the potential consequence of delay. Routine matters may follow the company's normal response-time standard, while potential health or safety situations should enter an urgent escalation pathway with appropriate approved safety guidance.

The agent should never promise a specific response time unless that service level has been formally established and can reasonably be fulfilled by the organization.

### 4. Deployment Readiness Assessment

#### Decision: CONDITIONAL APPROVAL

The Summit Climate Systems Customer Service AI Agent should not immediately receive unrestricted production approval. I would recommend conditional approval for a controlled pilot after the organization verifies that the agent has access to complete, current, and approved business information required for its authorized responsibilities.

Before the pilot begins, the organization should verify the accuracy of the agent's knowledge base, establish ownership for maintaining that information, confirm escalation pathways and human response responsibilities, define approved customer communications, and ensure that privacy and safety controls are functioning as intended.

I would recommend an initial 30-day controlled pilot with active monitoring. During this period, the organization should track agent responses, clarification requests, human escalations, customer interactions, knowledge failures, safety-related events, and unexpected behavior.

The purpose of the pilot would not be to demonstrate that the system is "bug free." Instead, it would provide evidence that the agent performs reliably within its approved scope, appropriately recognizes uncertainty, escalates higher-risk situations, and does not create unacceptable operational or customer risk.

At the conclusion of the pilot, designated business, operational, and technical stakeholders should review the results before authorizing broader deployment. Any significant safety, privacy, governance, or accuracy failures should require remediation and additional testing before approval is expanded.

#### Pilot Stop Conditions and Incident Response

Conditional approval should include predefined conditions under which the pilot may be paused or suspended.

If the agent experiences a significant safety, privacy, or governance failure, such as failing to escalate a legitimate potential fire or electrical hazard, the affected capability or system should be temporarily suspended while the incident is investigated.

The absence of customer harm does not make a safety-critical failure acceptable. Once a significant failure mode has been identified, allowing the system to continue operating unchanged would effectively treat that behavior as an acceptable risk.

The organization should determine why the failure occurred, correct the underlying issue, test the remediation against the original scenario and related edge cases, and perform regression testing to ensure that the correction did not introduce new failures elsewhere.

The agent should return to the pilot only after designated human reviewers determine that the failure has been sufficiently understood, remediated, and tested.

Permanent termination of the project would not automatically be required after a single correctable incident. The appropriate response should be proportional to the severity, recurrence, and ability to mitigate the identified risk.

### 5. Final Governance Recommendation

The Summit Climate Systems Customer Service AI Agent demonstrates that routine customer-service interactions can be automated while preserving meaningful boundaries around safety, uncertainty, privacy, financial decisions, and human judgment.

The agent should operate autonomously only within clearly defined, low-risk scenarios supported by verified information. Requests involving uncertainty should trigger clarification, while situations involving safety concerns, diagnosis, final pricing, unauthorized sensitive information, or other higher-risk decisions should preserve human authority through escalation.

Responsible deployment also requires governance beyond the AI system itself. Business teams must own the accuracy of the information provided to the agent, escalation must result in a complete and traceable human handoff, and significant failures must trigger investigation, remediation, testing, and human authorization before normal operation resumes.

Based on the current prototype, my recommendation is CONDITIONAL APPROVAL for a controlled pilot after required operational, knowledge, privacy, safety, and escalation controls have been validated.

A successful deployment should not be measured simply by how many customer interactions the agent resolves autonomously. Success should also include whether the system recognizes its limitations, escalates appropriately, protects customers and their information, maintains accurate knowledge, and produces measurable value without removing necessary human judgment.

The objective is not maximum automation.

The objective is responsible automation that the business, its employees, and its customers can trust.

