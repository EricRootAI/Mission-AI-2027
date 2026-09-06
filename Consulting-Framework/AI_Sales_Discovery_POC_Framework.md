# AI Sales Discovery & POC Framework

## Purpose

This framework provides a structured approach for evaluating potential AI opportunities with enterprise customers, moving from initial business discovery through a proof of concept (POC) and ultimately to a responsible go/no-go or scale decision.

The goal is not to force AI into every business problem. It is to understand the customer's actual need, determine whether AI can create measurable value, identify risks and constraints early, and design an evaluation that gives stakeholders enough evidence to make an informed decision.

## Framework Stages

1. Business Discovery
2. AI Use-Case Qualification
3. Stakeholder & Risk Assessment
4. POC Design
5. Success Metrics & Evaluation
6. Go / No-Go / Scale Decision
---

---

## 1. Business Discovery

Before determining whether AI is appropriate, establish a clear understanding of the business problem, the current workflow, and the outcome the customer is trying to achieve.

### Discovery Questions

- What is your current average call-handling time, and has that changed as customer-service demand has increased?
- Are calls consistently reaching the correct department, or are customer-service representatives handling calls that should be routed elsewhere?
- What are your current staffing levels, and how do they compare with call volume during peak and non-peak periods?
- Do you currently provide after-hours coverage or an answering service for calls received outside normal business hours?
- On average, how many customer-service calls per day involve repetitive or routine requests?
- Can you break down those repetitive calls by request type so we can identify which issues account for the greatest share of volume?

### Initial Automation Assessment

| Request Type | Initial Recommendation | Rationale |
|---|---|---|
| Order status | Automate with verification and human escalation | AI may retrieve and communicate verified order information, but missing, conflicting, stale, or unusual order data should be escalated to a human representative. |
| Appointment confirmation/rescheduling | Potential automation candidate | Routine, rules-based requests may be handled automatically when the AI has access to accurate scheduling data and defined boundaries. |
| Basic account questions | Potential automation candidate | Routine informational requests may be automated when the AI is limited to authorized, verified account information. |
| Product/service information | Potential automation candidate | AI may answer routine questions using approved and current product or service information. |
| Billing disputes | Human oversight required | Disputes may require investigation, judgment, account changes, or financial decisions and should be routed to an authorized human representative. |

### Data & System Readiness Questions

Before recommending automation or beginning a POC, determine whether the AI can reliably access the systems and data required to provide accurate customer information.

Key questions include:

- How are customer orders received, processed, and fulfilled from initial purchase through final delivery?
- Which systems contain the authoritative order, fulfillment, and customer information?
- What shipping, carrier, or delivery methods does the company currently use?
- How does the company currently track an order once it enters the fulfillment or delivery process?
- Can the proposed AI solution securely access current and verified information from those systems?
- How frequently is order and tracking information updated, and could stale or conflicting information be presented to a customer?
- What should happen when the AI cannot retrieve sufficient information or encounters conflicting, missing, or unusual data?
- Which exceptions should automatically trigger escalation to a human representative?

## 2. AI Use-Case Qualification

Once a potential automation opportunity has been identified, determine whether the expected business value is significant enough to justify further evaluation and whether AI is an appropriate solution.

### Qualification Questions

- How much employee time is currently spent handling repetitive or routine customer requests?
- What operational cost or lost productivity is associated with that workload?
- What improvement in service levels does the organization expect from reducing repetitive call volume?
- Could automating routine requests allow employees to focus on higher-value activities such as sales, service, repairs, complex customer issues, or other revenue-supporting work?
- Are the targeted requests sufficiently predictable and rules-based to be handled safely through automation?
- Does the organization have the systems, data, integrations, and business rules required for the AI to complete those tasks reliably?
- Is AI actually necessary for the identified problem, or could a simpler process or traditional automation solution achieve the desired outcome?
- What measurable business outcome would justify proceeding with an AI proof of concept?

### Qualification Principle

A repetitive task should not be automated simply because AI is capable of performing it. The use case should demonstrate sufficient business value, operational readiness, measurable improvement potential, and an acceptable level of risk before moving forward to a POC.

## 3. Stakeholder & Risk Assessment

Before designing a POC, identify the stakeholders responsible for the affected workflows, systems, data, policies, and business outcomes. Each stakeholder should have clearly defined responsibilities for implementation, oversight, and escalation.

### Key Stakeholders

- **Customer Service / Operations:** Owns the customer-service workflow, service expectations, and human escalation process.
- **Scheduling:** Maintains accurate appointment availability, scheduling rules, blackout periods, and other operational constraints required by the AI.
- **IT:** Owns technical integration, authorized system access, security, reliability, maintenance, and technical support for the AI solution.
- **Accounting / Finance:** Defines boundaries around billing, payment information, credits, refunds, and other financially sensitive customer interactions.
- **Legal / Compliance / Risk:** Establishes privacy, regulatory, acceptable-use, and organizational policy requirements.
- **Human Resources / Training:** Supports employee training, change management, workflow changes, and adoption requirements.
- **Executive Sponsor / COO:** Owns the business outcome, provides executive sponsorship, evaluates operational impact and ROI, and participates in the final decision to scale, revise, or discontinue the initiative.

### Initial Risk Assessment

Two high-priority risks in the proposed customer-service use case are inaccurate customer information and improper scheduling actions.

#### Risk 1: Incorrect Order Information

The AI could provide an inaccurate order status because of stale, missing, conflicting, or incorrectly interpreted data.

**Controls:**
- Retrieve order information only from authorized systems of record.
- Verify that required information is available and current before responding.
- Do not allow the AI to infer or invent missing order information.
- Escalate to a human representative when information is missing, stale, conflicting, or otherwise uncertain.

#### Risk 2: Appointment Overbooking

The AI could schedule an appointment into a time period that is already full or violate existing scheduling rules.

**Controls:**
- Require real-time access to the authoritative scheduling system before confirming availability.
- Validate availability immediately before completing an appointment.
- Apply existing scheduling rules, capacity limits, and blackout periods.
- Escalate exceptions or conflicting scheduling information to an authorized employee.

### Human Oversight Principle

AI should handle routine interactions only when it has sufficient authorized and verified information to operate within clearly defined business rules. When required information is unavailable, conflicting, stale, or outside those boundaries, the AI should stop the automated workflow and escalate the interaction to a human representative.

## 4. POC Design

The proof of concept should begin with a limited set of customer interactions that provide measurable operational value while keeping the initial level of risk manageable.

### Initial 30-Day POC Scope

The POC will evaluate three customer-service use cases:

1. **Order-Status Inquiries**
   - Retrieve current order information from an authorized system of record.
   - Communicate verified status information to the customer.
   - Escalate when order information is missing, stale, conflicting, or requires additional research.

2. **Appointment Confirmations**
   - Verify existing appointment information using the authoritative scheduling system.
   - Communicate the confirmed date, time, and other approved appointment details.
   - Do not create, cancel, or reschedule appointments during the initial POC.
   - Escalate discrepancies or unavailable appointment information to a human representative.

3. **Basic Account Questions**
   - Answer predefined routine questions using authorized and verified account information.
   - Limit AI access and responses to information approved for the POC.
   - Escalate requests involving disputes, financial decisions, account changes, sensitive exceptions, or information outside the approved scope.

### POC Boundaries

The initial POC will not include:

- Billing disputes, refunds, credits, or other financial decisions.
- Appointment scheduling, cancellation, or rescheduling.
- Complex customer complaints or service escalations.
- Actions requiring employee judgment or authorization.
- Responses based on information that cannot be verified through an approved system.

### POC Operating Principle

The purpose of the POC is not to demonstrate that AI can handle every customer interaction. It is to determine whether AI can reliably handle a small group of well-defined, repetitive interactions while maintaining accuracy, appropriate human escalation, and a positive customer experience.

Successful performance within this limited scope can provide evidence for considering additional use cases in a future phase.

## 5. Success Metrics & Evaluation

The POC should be evaluated using predefined measures that assess accuracy, appropriate escalation, customer-service impact, and operational value.

### Core Success Metrics

- **Order-Status Accuracy:** Were customers provided with accurate and current order information based on verified system data?
- **Appointment Confirmation Accuracy:** Were customers provided with the correct appointment date, time, and approved appointment details?
- **Basic Account Resolution:** How many basic account inquiries were successfully resolved within the approved AI scope?
- **Appropriate Escalation:** Did the AI correctly identify customer requests that exceeded the approved scope and transfer those interactions to a human representative?
- **Containment Rate:** What percentage of eligible routine interactions were successfully completed without requiring human intervention?
- **Employee Time Recovered:** How much employee handling time was potentially recovered by automating eligible repetitive interactions?
- **Customer Experience:** Did the POC maintain or improve customer-service quality while introducing automation?
- **AI Error and Exception Rate:** How frequently did the AI provide incorrect information, fail to retrieve required information, or encounter an exception requiring review?

### Evaluation Principle

Success should not be measured solely by the number of interactions automated. The POC should demonstrate that automation can provide accurate information, recognize its operational boundaries, escalate appropriately, and create measurable business value without introducing unacceptable customer or operational risk.

## 6. Go / No-Go / Scale Decision

At the end of the POC, results should be reviewed against the predefined success metrics, operational risks, customer impact, and business value.

The final recommendation should fall into one of three categories:

- **Go / Scale:** The POC demonstrates strong accuracy, appropriate escalation, acceptable risk, measurable business value, and sufficient operational readiness to justify expansion.
- **Revise / Retest:** The POC demonstrates meaningful potential, but identified weaknesses or risks should be corrected and tested again before expansion.
- **No-Go:** The POC does not demonstrate sufficient value, reliability, safety, or operational readiness to justify continued deployment.

### Example Decision

Using the following hypothetical POC results:

- Order-status accuracy: 98%
- Appointment-confirmation accuracy: 99%
- Basic account inquiries successfully resolved: 82%
- Appropriate human escalation: 96%
- Eligible interactions handled without employee intervention: 72%
- Estimated employee time recovered: 27 hours per day
- Customer satisfaction: essentially unchanged
- Serious privacy or security incidents: 0

The recommended decision would be:

**REVISE / RETEST**

The POC demonstrates meaningful operational value through reduced employee handling time and successful automation of routine interactions. However, unchanged customer-service levels indicate an opportunity for further improvement, and instances of inaccurate order information create a reliability risk that should be addressed before the solution is expanded.

The next phase should focus on improving data verification, preventing unsupported delivery estimates, strengthening exception handling, and retesting order-status accuracy before considering broader deployment.

### Decision Principle

Operational efficiency alone is not sufficient justification for scaling an AI solution. Expansion should occur only when measurable business value is supported by reliable performance, appropriate human oversight, acceptable risk, and maintained or improved customer outcomes.
