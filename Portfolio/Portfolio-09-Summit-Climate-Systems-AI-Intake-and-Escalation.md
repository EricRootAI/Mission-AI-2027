# Summit Climate Systems — AI Intake, Verification, and Escalation Design

## Purpose

This document defines how an AI-assisted intake system should extract customer-request data, identify missing or potentially stale information, recommend urgency levels, and escalate potentially critical cases while preserving human authority over consequential operational decisions.

The goal is to improve intake speed, consistency, and routing accuracy without allowing the AI to make unsupported assumptions or independently override human judgment in high-impact situations.

---

## 1. Core Intake Fields

When a customer request is received, the AI should attempt to extract the following information:

| Intake Field | AI Action | Why It Matters |
|---|---|---|
| Contact Name | Extract if provided | Identifies the customer point of contact |
| Business Name | Extract if provided | Associates the request with the correct customer account |
| Phone Number | Extract if provided | Enables rapid customer follow-up |
| Service Address | Extract if provided | Determines service location and routing |
| Unit Serial Number | Extract if provided | Helps identify the affected equipment |
| Reported Issue | Summarize the customer’s description | Gives the operations team immediate context |
| Urgency | Recommend a P1–P4 priority level | Supports routing and escalation |
| Additional Information | Capture relevant context such as repeat failures, deadlines, occupancy, or customer impact | Helps refine priority and next actions |

---

## 2. Missing Information Handling

The AI must not invent missing customer information.

If required information is not present in the incoming request, the system should clearly flag it as missing.

Example:

- Missing business name
- Missing phone number
- Missing complete service address
- Missing unit serial number

The goal is to make missing-data gaps visible without creating false confidence.

---

## 3. CRM Verification Safeguard

Customer and employee information can become outdated.

In industries where salespeople, account representatives, and contacts frequently move between competing organizations, existing CRM data may no longer reflect the customer’s current employer, location, or role.

Because of this, the AI should not automatically treat a potential CRM match as verified truth.

### Customer Data Verification Rule

When required intake information is missing, the AI may identify potentially matching data from existing CRM records, but that information should be flagged as **unverified**.

Human or customer verification should occur before the information is used for consequential routing or service decisions.

Example:

**Possible CRM Match**

- Contact: Michelle
- Business: ABC Hospitality
- Service Address: Existing CRM address
- Registered Equipment: Existing system record
- Status: Customer verification required

This allows the AI to assist with retrieval while preventing stale data from being treated as current without review.

---

## 4. Priority Classification

The AI should recommend an initial urgency classification using Summit Climate Systems’ P1–P4 priority framework.

The recommendation should be based on operational impact, safety indicators, business disruption, timing, and customer-provided context.

### Example Scenario

Customer message:

> Hi, our main AC unit stopped cooling sometime overnight. It's already getting warm inside and we open to customers at 10 AM. This is the second time we've had trouble with this unit this month. Can someone please get out here as soon as possible?

### Initial Classification

**P2 — Urgent**

Reasoning:

- Main cooling system is down
- Business operations may be affected
- Indoor conditions are worsening
- Customer opens at 10 AM
- This is a repeat equipment issue
- No explicit life-safety condition has yet been confirmed

---

## 5. Time-Based Escalation

Priority should not always remain static.

A situation that begins as urgent but manageable can become critical as conditions worsen.

For the example above, the case should remain P2 initially, but if service has not arrived by 11:00 AM, the system should trigger an escalation review.

### Escalation Rule

If the technician has not arrived by the defined threshold, the AI should alert the dispatcher and recommend reassessment.

The AI should also recommend earlier reassessment if new information indicates:

- Rising indoor temperature
- Vulnerable occupants
- Health or safety concerns
- Customer-facing disruption
- Worsening equipment conditions
- Additional business impact

The AI should support escalation decisions with observable evidence wherever possible rather than relying on vague assumptions.

---

## 6. Human Dispatcher Gate

The AI should not independently upgrade a service request from P2 to P1 in high-impact situations.

Instead, it should alert a human dispatcher and present the reasons an escalation may be necessary.

### Human Escalation Gate

When new information suggests that a P2 request may require P1 escalation, the AI should:

1. Alert the dispatcher immediately
2. Summarize the escalation indicators
3. Recommend a reassessment
4. Present relevant customer and service details
5. Wait for human review before changing the priority

The dispatcher then becomes responsible for:

- Contacting the customer
- Verifying the reported conditions
- Reassuring the customer that assistance is being coordinated
- Confirming or changing the priority
- Re-routing technicians if necessary
- Becoming the customer’s operational point of contact

This preserves human authority over consequential service decisions while still allowing the AI to detect risk quickly.

---

## 7. Example Escalation Alert

### Current Situation

At 10:35 AM, the customer sends an update:

> It's 84 degrees inside now and customers are complaining. We have several elderly guests here. Please tell me someone is actually coming.

The assigned technician is now expected to arrive at 11:20 AM.

### AI Alert

**P1 REVIEW RECOMMENDED — HUMAN ACTION REQUIRED**

**Current Priority:** P2  
**Indoor Temperature:** 84°F reported  
**Vulnerable Occupants:** Elderly guests reported  
**Customer Impact:** Complaints occurring  
**Technician ETA:** 11:20 AM  
**Original Escalation Threshold:** 11:00 AM  

**Recommended Action:**  
Dispatcher should contact the customer, verify current conditions, reassess priority, and determine whether technician reassignment is necessary.

---

## 8. Role of the AI vs. Role of the Human

### AI Responsibilities

The AI may:

- Extract intake data
- Identify missing information
- Retrieve possible CRM matches
- Flag stale or unverified data
- Summarize the reported issue
- Recommend an urgency level
- Monitor time-based escalation conditions
- Detect new risk indicators
- Alert the dispatcher
- Present reasons for escalation

### Human Responsibilities

The human dispatcher should:

- Verify uncertain or potentially stale information
- Confirm consequential priority changes
- Contact the customer
- Reassure the customer
- Reassign technicians if needed
- Resolve resource conflicts
- Make final operational decisions

---

## 9. Governance Principle

The core design principle is:

**AI should detect, summarize, recommend, and alert. Humans should verify, decide, communicate, and override when necessary.**

This creates a practical human-in-the-loop model where AI improves speed and consistency without being given unchecked authority over consequential service decisions.

---

## 10. Key Takeaways

This intake and escalation design demonstrates several responsible AI principles:

- Structured intake
- Missing-data visibility
- Stale-data awareness
- Human verification
- Dynamic escalation
- Explainable recommendations
- Human-in-the-loop control
- Clear separation of AI authority and human authority
- Operational accountability

The system is designed to improve customer response and technician coordination while reducing the risk of automation making unsupported or high-impact decisions without human oversight.
