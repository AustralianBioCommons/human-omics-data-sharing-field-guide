---
title: Federated Identity & Access Management
page_id: fediam
type: technologies_standards
toc: true
description: Description of Federated Identity and Access Management and various options for implementing it.
contributors: [Kylie Davies, Marion Shadbolt, Nick Rossow, Sarah Nisbet, Irene Hung, Joshua Harris]
affiliations: [Australian Access Federation]
---

This is an introductory guide to federated identity and access management. This guide focuses on the benefits and risks associated with various identity and access management models. Plain language is deliberately used within this guide and the focus is mainly on the experience of organisations and users, rather than detailed technology concepts.

## Identity and Access Management (also known as Trust and Identity)
When you login with a username and password, or a one time password, or even a preconfigured link and you are then granted access to protected information, such as at your workplace or in an app or website, you are using the systems of Identity and Access Management:

### Definition

Identity and Access Management (also known as Trust and Identity) is the collection of policies, technologies and tools that ensure people can access an organisation’s computing services easily and securely. 

Identity and access management solutions are designed to:
- allow people to login to systems, in such a way that the system and any information it holds is protected from unauthorised access; and 
- allow the people using the system (users) to login easily and access the information they authorised to access, while being confident their privacy is protected and the information they view, input or retrieve is secure.

## Federated Identity and Access Management
Federated Identity and Access Management (IAM) differs from traditional models of trust and identity, in that it relies on a federated system, where the user’s identity is provided by the most authoritative source, and the system is automated to allow the user to use one login ID and password (one set of credentials) to access multiple organisations by agreement. Before we discuss the benefits of Federated IAM, let’s learn more about the difference between traditional IAM models and the Federated model. For the purposes of understanding, let’s imagine a pathologist based at a university research organisation who wants to store images with a pathology image storage company called Bits Imaging.

### Challenges within a Traditional Identity and Access Model
In a traditional IAM model, if I want to access Bits Imaging and start storing my pathology images, I visit the Bits Imaging website and sign up. I enter my name, address, company/practice name, email address and create a password for bitsimaging.com.au. All this data will be stored at Bits Imaging in the IAM system’s user directory. Each time I login, the Bits Imaging login page will pass my credentials to be compared with those stored for me in the user directory, to make sure my username matches a current user record and my password is correct for that user record. If it is, Bingo! I am into the system and start uploading my images. This is illustrated below in Bits Imaging Example 1.

![bitsimagingExample1](/images/diagrams/bitsimagingExample1.png)

This is how all websites and applications used to work. And for a long time we all thought that was enough and pretty amazing.

But, there are several risks in this traditional model. Here are a few:

- **Who is this user…really?** How does Bits know I am who I say I am? I created my own user ID and provided my own email address. I could be planning to flood Bits’ cloud storage with junk and I could have made up user details that don’t identify me. There is no independent verification of user details.
- **The honeypot!** At Bits’ headquarters, over time, the user directory grows to a large valuable dataset, containing all the users’ personal details and payment details. This presents a very tempting honeypot for bad actors and hackers. Bits has to work harder and harder to firewall off these users’ details. If there is a data breach, their company reputation will be damaged and the users may lose their privacy, or have payment details stolen. And because users tend to repeat passwords, a breach does not just put the users’ Bits’ details at risk but also their logins on other websites too. Hackers typically approach targets using a laddered approach, gaining access to one system and using information from there to breach another of the user’s accounts elsewhere, and so on.
- **So many different logins!** For me, the user, I can’t remember my login details and have to reset my password over and over. This is so annoying. Bits Imaging is just one of the many tools I use in my work and I waste valuable time keeping track of multiple login/password combinations (credentials). Or I might write the password into my little book of passwords, which is risky for me and for Bits Imaging if I lose that book or it falls into the wrong hands.

### The Federated Identity and Access Model
The Federated Identity and Access Management model is dependent on the user identity being verified by an organisation who can act as that user’s most authoritative identity source (Identity Provider). This enables other organisations, known as Service Providers, based on agreements with the Identity Provider, to invite the user to use those original login credentials, to access the Service Provider’s services, web assets and data. (How much access the user gets is always managed by the Service Provider).

Let’s revisit Bits Imaging and this time let’s say I work at the University of Melbourne (UniMelb) on a pathology project. Here’s how Federated Identity is set up:

1. The University and Bits Imaging reach an agreement where Bits will trust the University as an authoritative Identity Provider for access to Bits Imaging systems. (This step happens at the start, in the background, between organisations, and the user is not involved.)
1. When I enrol or become employed at UniMelb, I show the Human Resources department my birth certificate and driver’s licence and so they are ASSURED of my identity. UniMelb creates a set of user credentials for me in the system and I can login to UniMelb systems using my username, password and a One Time code (multi-factor authentication). Very secure.
1. When I want to sign up for Bits Imaging, on their website they have an option “Sign In with your University of Melbourne details”. I click that and the Bits website passes me back to the UniMelb website where I enter my credentials (illustrated below in “Bits Imaging Example 2”). This is KEY - Bits Imaging NEVER knows what my UniMelb login credentials are. They are not passed from UniMelb to Bits Imaging. Instead an encrypted authorisation code is passed.
![bitsimagingExample2](/images/diagrams/bitsimagingExample2.png)
1. I login to Bits Imaging and receive a basic account. I may receive further allocation if I am based in a certain faculty or work on a certain project. Bits Imaging determines this.

Here are the benefits:

- **Identity Assurance!** Bits Imaging knows because of its agreement with UniMelb, that UniMelb sighted my original identity documents and met me face to face. I definitely am who I say I am. We call this a high level of identity assurance and it is provided by UniMelb to its Federated Identity partners based on the trust agreement.
- **No Honeypot!** Bits Imaging does not store my details. Instead it leverages UniMelb’s identity system and multi factor authentication. It trusts UniMelb to assure my identity is correct. There is no longer a honeypot of user data stored at Bits Imaging. Instead they can depend on UniMelb’s more cyber secure set up to protect Bits from unlawful access and data breaches.
- **One password!** I only have to remember my UniMelb credentials, not a new password for Bits. And I feel secure because I can trust that UniMelb takes good care of my personally identifiable information (PII).

There are fewer risks to this model but some risks persist:
- **Trust!** How does UniMelb know that Bits Imaging maintains their systems and won’t create a cyber risk when UniMelb staff and students use the Bits Imaging site?
- **Effort and Cost!** In order to establish trust, UniMelb needs to establish and maintain robust trust agreements with Bits Imaging and every other service they allow their users to access using UniMelb credentials. These agreements and the technology setups need to be audited by someone with specialist Identity and Access Management knowledge. This is a lot of ongoing work for a high-cost skillset.

To share these costs and ensure high standards are maintained, national identity federations were formed in the early 2000s.

## National Federations
In many countries around the world including Australia, national research and education networks (NREN) have set up national identity federations. These federations act as multi-partner identity brokers. [Australian Access Federation (AAF)](https://aaf.edu.au/) is Australia’s identity federation, established in 2009. AAF acts as the Identity and Access Management hub for:
- all Australian universities
- CSIRO and other government research agencies as well as leading research support organisations
- organisations providing online products or services for teaching, learning and research.

Using single sign-on with the user’s home organisation credentials, AAF enables access for over one million people. Here is a link to the list of AAF’s current subscribers [https://aaf.edu.au/subscribers/](https://aaf.edu.au/subscribers/)

AAF provides a list of organisations a user can select from to login to the service. So in our Bits Imaging example, my login button would say “Sign in with AAF” instead of “Sign in with UniMelb”. When I click that button I am presented with a list of AAF Identity Providers. I select “University of Melbourne” then enter my credentials. AAF passes my credentials to UniMelb. When a valid match is found, UniMelb passes a secure authorisation code via AAF to Bits Imaging. This is illustrated in the image below.

![nationalfediammodel](/images/diagrams/nationalfediammodel.png)

Here are the benefits of using a national federation like AAF:

- **AAF takes care of all the trust agreements!** Using AAF means that UniMelb does not have to set up and maintain/enforce separate trust agreements with Bits Imaging and every other Service Provider. This is advantageous because technologies and standards are forever improving as new threats arise. Maintenance of agreements to reflect these changes takes time and effort. AAF acts as the hub, with organisations interacting with each other via AAF. All AAF subscribers must agree to the single set of federation rules and recommit each year.
- **Specialist knowledge!** AAF makes Trust and Identity their core business: regularly updating their software, implementing new standards, monitoring the systems they provide and continuously improving  AAF’s cyber security.
- **Better security for service providers!** Service Providers like Bits Imaging can leverage the identity assurance provided by the user’s identity provider to be sure they are who they say they are. This enhances security.
- **More users for service providers!** Service Providers like Bits Imaging can leverage multiple connections (identity broking) available through AAF to attract more users from many universities and other government organisations. 
- **More services available for staff and students!** Organisations leverage AAF’s agreements with Service Providers to offer access to their staff and students to over 150 services. Examples of services available through AAF include CERN (home of the Large Hadron Collider), the Murchison Widefield Array, MyeQuals and Science Direct. AAF’s website lists [all available services](https://aaf.edu.au/subscribers/services/).
- **One set of rules for everyone!** AAF maintains a set of regularly reviewed Identity Provider and Service Provider rules (the “[Federation Rules](https://aaf.edu.au/wp-content/uploads/AAF_Federation_Rules_v2_20240101.pdf)”) and all subscribers, both Identity Providers like universities, and Service Providers like our Bits example, agree to them and confirm how they are adhering to the rules via an annual self assessment.
- **Lowers the burden on IT staff!** UniMelb does not need to worry about Bits Imaging or any other AAF subscriber. As long as UniMelb maintains its internal Identity and Access Management system to an acceptable standard as per the AAF Rules, AAF takes care of (most of) the rest. AAF now also offers cloud based solutions (RapidIdP) to deploy and maintain IAM software for Identity Providers for a fee.
- **NCRIS partner!** AAF is entrusted by NCRIS through the Trust and Identity project to partner with national research infrastructure and develop a globally aligned Trust and Identity Framework for the Australian research environment. The output will be a system-wide approach to Identity and Access Management, as illustrated in the image by AAF below. This means that subscribers of AAF will benefit from the NCRIS investment and the improvements that stem from the project work. More information about AAF’s Trust and Identity Project is available at [https://trust.aaf.edu.au](https://trust.aaf.edu.au)

![fediamFutureState](/images/diagrams/fediamFutureState.png)

The future state of access to Australian research infrastructure, via single sign-on with AAF (AAF Trust and Identity Project, [https://trust.aaf.edu.au/trust-and-identity-framework/](https://trust.aaf.edu.au/trust-and-identity-framework/) accessed 29/05/2024.)

### Considerations:
- **Fees** - National federations like AAF charge a subscription fee to organisations (not individual users). So in our example, UniMelb and Bits Imaging need to be prepared to pay a fee to AAF for the service. This subscription fee needs to be considered in comparison to the savings through a reduced resource workload for university IT and contract administration staff.
- **Coverage** - While AAF subscriber organisations include almost 100% of universities in Australia and other flagship organisations, when government entities and other research organisations are counted, subscriber coverage is currently under 50%. AAF is developing a roadmap to broaden coverage in order to better serve NCRIS facilities and the Australian research community.

## Conclusion
Federated Identity and Access Management (IAM) differs from traditional models of trust and identity, in that it relies on a federated system, where the user’s identity is provided by the most authoritative source, and the system is automated to allow the user to use one login ID and password (one set of credentials) to access multiple organisations through technology and a trust agreement. This delivers convenience and assurance for the user and enhanced cyber security for organisations. Trust agreements (policies) can be organised one to one between organisations, or through a central hub like a national or community federation or other type of identity broker. The benefits of utilising federations or brokers are substantial, but coverage of user communities needs to be achievable and costs should be considered. This was a basic introduction to the concept of federated identity and access management. Information is widely available about supporting technologies such as OAuth2.0, OIDC, cyber security and Multi Factor Authentication. Some links to further reading are provided below.

## Additional Info:
- [What is OAuth2.0?](https://auth0.com/intro-to-iam/what-is-oauth-2)
- [What is OIDC (OpenID Connect)?](https://auth0.com/docs/authenticate/protocols/openid-connect-protocol)
- [Okta Maturity Model](https://www.okta.com/au/resources/whitepaper-workforce-maturity-framework/?utm_source=google&utm_campaign=apac_anz_mult_all_wf-all_dg-ao_a-wf_search_google_text_kw_IAM_utm2&utm_medium=cpc&utm_id=aNK4z000000UECBGA4&gad_source=1&gclid=CjwKCAjw-O6zBhASEiwAOHeGxV9MEvwMq7elJCmqxHDGNFuiUVZExZsQPU3aI1Hdmmhn2pC5DXx2_BoCOyIQAvD_BwE)
- [AARC Blueprint Architecture](https://aarc-community.org/architecture/)
- [About the Australian Access Federation](https://aaf.edu.au/about/)
- [What is MFA (Multi-Factor Authentication)?](https://aws.amazon.com/what-is/mfa/#:~:text=Multi%2Dfactor%20authentication%20(MFA),question%2C%20or%20scan%20a%20fingerprint.)
- [REFEDS (the Research and Education FEDerations group)](https://refeds.org/)
- [Identity Federations and eduGAIN](https://wiki.geant.org/display/eduGAIN/Identity+Federations+and+eduGAIN)

## Hashtags
#federatedidentity #identityandaccessmanagement #trustandidentity #IAM #credentials #cyber #NREN #federation #researchaccess #researchnetworks #identityassurance

## References
- [Trust and Identity Future State Diagram, AAF website](https://trust.aaf.edu.au/trust-and-identity-framework/) (accessed 29/05/2024)
- [Benefits of Identity and Access Management Systems](https://www.fortinet.com/resources/cyberglossary/identity-and-access-management#:~:text=An%20IAM%20solution%20enables%20businesses,desk%20requests%20by%20automating%20them.)

{% bibliography --cited %}