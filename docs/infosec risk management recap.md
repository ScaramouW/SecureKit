# InfoSec Governance & Risk Management — Study Notes

> 📖 Daily reading notes from: *CISSP All-in-One Exam Guide* — Matt Walker  
> 🎯 Goal: Build a solid foundation in security governance and risk management ahead of a cybersecurity internship.  
> 🗓️ Format: One recap per reading session, progressively covering each domain.

---

## Recap — Domain: Information Security Governance & Risk Management

---

**What is the Information Security Governance and Risk Management domain?**

The Information Security Governance and Risk Management domain entails:

- The **identification** of an organization's information assets, and the development, documentation, implementation, and updating of **policies, standards, procedures, and guidelines** that protect the **confidentiality, integrity, and availability** of those assets.

- The use of management tools such as **data classification**, **risk assessment**, and **risk analysis** to identify **threats**, classify assets, and rate vulnerabilities — so that effective security measures and controls can be implemented.

> [!TIP]
>
> New knowledge requirements introduced for 2012 & 2013 *(Source: CISSP CBK)*:
>
> - **Management knowledge** in budget, metrics, and resources for security programs.
> - **Privacy requirements compliance** *(covered further in the Legal, Regulations, Investigations and Compliance domain)*.

---

## Core Security Objectives (CIA Triad)

- **Confidentiality** — Preserving authorized restrictions on information **access** and **disclosure**, including protecting personal privacy and proprietary information. *(44 U.S.C. § 3542)*
- **Integrity** — Guarding against improper information **modification** or **destruction**, and ensuring information **non-repudiation** and **authenticity**.
- **Availability** — Ensuring **timely** and **reliable** access to and use of information.

---

## Security Controls

**Security controls** are the management, operational, and technical safeguards used to protect the **confidentiality, integrity, and availability** of an information system.

---

### Classes of Security Controls

- **Management (Administrative) Controls**
  - Risk Assessment (RA)
  - Planning (PL)
  - System and Service Acquisition (SA)
  - Security Assessment and Authorization (CA)
  - Program Management (PM)

- **Operational (and Physical) Controls**
  - Personnel Security (PS)
  - Physical and Environmental Protection (PE)
  - Contingency Planning (CP)
  - Configuration Management (CM)
  - Maintenance (MA)
  - System and Information Integrity (SI)
  - Media Protection (MP)
  - Incident Response (IR)
  - Awareness and Training (AT)

- **Technical (Logical) Controls**
  - Identification and Authentication (IA)
  - Access Control (AC)
  - Audit and Accountability (AU)
  - System and Communications Protection (SC)

> [!NOTE]
>
> Security Categorization (post-Risk Assessment) for National Security Systems:
>
> SC = { (**confidentiality**, *impact*), (**integrity**, *impact*), (**availability**, *impact*) }
>
> where the acceptable values for potential impact are: **low**, **moderate**, or **high**.

---

## Categories of Security Controls

### ISO/IEC 27001:2005 — *Information Technology – Security Techniques – Information Security Management System – Requirements*

- **Security Policy**
  - Information Security Policy
- **Organization of Information Security**
  - Internal Organization / External Parties
- **Asset Management**
  - Responsibility for Assets / Information Classification
- **Human Resources Security**
  - Prior to / During / Termination or Change of Employment
- **Physical and Environmental Security**
  - Secure Areas / Equipment Security
- **Communication and Operations Management**
  - Operational Procedures and Responsibilities
  - Third-Party Service Delivery Management
  - Backup / Network Security Management, etc.
- **Information System Acquisition, Development, and Maintenance**
  - Security Requirements of Information Systems
  - Cryptographic Controls
  - Technical Vulnerability Management
- **Access Control**
  - Business Requirements for Access Control
  - User, Network, System, Application, and Information Access Control
- **Information Security Incident Management**
  - Reporting Information Security Events and Weaknesses
  - Management of Information Security Incidents and Improvement
- **Business Continuity Management**
  - Information Security Aspects of Business Continuity Management
- **Compliance**
  - Compliance with Legal Requirements
  - Compliance with Security Policies and Standards
  - Technical Compliance / Audit Considerations

---

## Security Requirements Concepts

There are two main concepts for security requirements:

- **Functional Requirements** — Define the security behavior of an IT product or system.
- **Assurance Requirements** — Establish confidence that the security functions will perform as intended.

---

## Types of Security Controls

There are five main types of security controls:

1. **Directive Controls** — Direct, confine, or control the actions of subjects to enforce security policy.
2. **Preventive Controls** — Avoid security incidents before they occur.
3. **Detective Controls** — Identify and record security incidents or violations.
4. **Corrective Controls** — Restore systems to normal after a security incident.
5. **Recovery Controls** — Restore capabilities or services after a disaster or incident.

---

## Key Definitions

- **Due Care** — The *policies and implemented actions* that an organization **has taken** to minimize risk to its tangible and intangible assets.
- **Due Diligence** — The *continual actions* that an organization **is actively doing** to protect and minimize risk to its tangible and intangible assets.
