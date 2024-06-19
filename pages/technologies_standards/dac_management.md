---
title: Data Access Committee Management
page_id: dac_management
type: technologies_standards
toc: true
description: Description of various tools to assist with DAC management.
contributors: [Irene Hung]
affiliations: [GA4GH]
---

## What is a Data Access Committee?

A Data Access Committee (DAC) consists of a group of individuals who are responsible for reviewing and assessing data access requests to particular datasets. There are a range of roles and stages involved in the data access request process. Some examples are listed below:

| Role                  | Description in the Context of Data Access Control                                                                                                                                                           |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Principal Applicant**  | Person who is the primary applicant for access to data and who in many cases leads a research project as the Principal Investigator (PI).                                                                    |
| **Co-applicant**         | A person invited, by the Principal Applicant, to join a research project, and who may need access to the same data in the data access request.                                                               |
| **Data Owner**           | The representative of an institution that owns the data collection. The Data Owner may report on how often the data is used and what outputs result from its use.                                              |
| **Data Custodian**       | Person who is responsible for a data collection. Reports to a Data Owner. May report on how often the data is used and what outputs result from its use. May curate the data collection and perform technical tests to ensure its integrity. |
| **DAC Coordinator**      | Person who receives and evaluates data access requests, sometimes in conjunction with a colleague or as a lead role on a DAC Committee.                                                                      |
| **DAC Committee Member** | Person who reviews data access applications and provides recommendations on granting access as part of a committee led by a Data Access Coordinator (DAC Coordinator).                                         |
| **Authorised Officer**   | Person who is authorised to sign data sharing agreements with another organisation on behalf of their own organisation (e.g. board member, executive officer or CEO).                                          |
| **Data Distributor**     | Person who arranges for the provision of the approved data on a successful data access application with a signed data sharing agreement in place. This role may sit within a variety of teams in an organisation and data is provided using various methods. |

### System use cases

Below are some examples of use cases for the roles participating in the data access application process. These interactions and capabilities may be manual or automated, and may differ depending on the organisation.

## How are Data Access Committees managed?

A major challenge to human genome data sharing is navigating restrictions on data use. Decisions on how and to whom to grant access to data typically require significant human effort by DACs to ensure data doesn’t end up in the wrong hands and/or for the wrong purpose. Historically, DAC activities have consisted of numerous manual steps to assess the merits of applications and make a decision about whether to grant data access, making the process slow, burdensome, and largely hidden from the applicant.

The main methods that exist for DAC management include but are not limited to:

- **Resource Entitlement Management System (REMS)**
- **Data Use Oversight System (DUOS)**
- **Bespoke forms / ticketing such as REDCap, Jotform, Jira or Trello**
- **Ad hoc solutions, such as email or paper forms**

These methods vary from being largely manual (email/paper forms and bespoke ticketing) to more automated end-to-end solutions like REMS and DUOS. Below, we have summarised each of these systems, detailing the key features and advantages, as well as some limitations to consider.

### REMS

Resource Entitlement Management System (REMS {% tool "rems" %})  is an open-source software tool that facilitates the management of requesting and approving access rights to different types of resources, including research datasets and biological samples. It was created and is maintained by the CSC, IT Centre for Science in Finland.

REMS enables applicants to use their federated user IDs (e.g. existing institution user account) to log into REMS, complete the data access application and agree to the dataset's conditions and terms of use. The REMS system then circulates the application to the resource owner or designated representative for review and approval. It enables flexibility in how involved a resource owner wants to be in the approval process and keeps an audit trail of all actions against an application for traceability and transparency. REMS also produces reports on the applications and the granted data access rights.

Some key features and advantages of REMS include:

- Clear and functional user interface that allows applicants to see all of their applications in one place and follow the application process easily
- Open source code and comprehensive API that enables almost all operations available via the user interface
- Ability to modify and customise the application forms
- Allows for group members to be added to an application vs everyone applying for access separately
- Enables collaboration and transparency between applicants and DAC members regarding their application

There are some current limitations identified with the tool relating to its limited native reporting functionality, locking of applications once approved and inability to incorporate other research identifiers e.g. ORCID and ROR.

### DUOS

DUOS ({% tool "duos" %}) is a semi-automated data access management service, created by the Broad Institute.

DUOS leverages Data Use Ontology, which is a standardised vocabulary for data use limitations and proposed research that is also computer-readable. Using the same ontology, data custodians are able to describe their data use limitations and data requestors are able to describe their research purpose. This means that using the DUOS service, DACs are able to compare data use limitations and research purposes using the same vocabulary of terms, making it easier for them to make data access decisions. There is also the ability to enable an algorithm to automate this comparison and replicate the decision that a DAC could make, which has seen >90% agreement through testing.

Some key features and advantages of DUOS include:

- Implementation and alignment with Data Use Ontology, a GA4GH standard
- Automated consent matching algorithm
- Source code is available
- Currently free to use

Some current limitations of the tool include high reliance and dependency on the Broad Institute for deployments, system improvements and data management which may not be feasible for highly collaborative research networks and organisations.

In conclusion, DAC management is an essential component of human genome data sharing to ensure data is protected from misuse, unauthorised access or modification. With methods ranging from highly manual to semi-automated, there is potential for further development in the future to better support data custodians with sharing their data.


# References

- Data Access Committees, BMC Medical Ethics journal (2020): [Link](https://bmcmedethics.biomedcentral.com/articles/10.1186/s12910-020-0453-z)
- Australian BioCommons Human Genomes Platform Project: DAC Automation Discovery Phase Report: [Link](https://zenodo.org/records/10781057)
- Australian BioCommons Human Genomes Platform Project: Data Access Committee Management Systems Candidate Solutions Evaluation Report: [Link](https://zenodo.org/records/10720100)
- Australian BioCommons Experiences using the REMS (Resource Entitlement Management System) software package: [Link](https://support.biocommons.org.au/support/solutions/articles/6000266884-experiences-using-the-rems-resource-entitlement-management-system-software-package)
- REMS Github: [Link](https://github.com/CSCfi/rems)
- REMS public demo: [Link](https://rems-demo.rahtiapp.fi/)
- DUOS for DACs webpage: [Link](https://broad-duos.zendesk.com/hc/en-us/articles/360060401131-DUOS-for-DACs)
- DUOS website: [Link](https://duos.broadinstitute.org/)