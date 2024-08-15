---
title: FHIR
page_id: fhir
type: technologies_standards
toc: true
description: FHIR (Fast Healthcare Interoperability Resources) is a standard for exchanging healthcare information electronically. 
contributors: [Marion Shadbolt]
affiliations: [FHIR]
---

Stuff about FHIR

## Fast Healthcare Interoperability Resources (FHIR)

FHIR is a standard for characterising all information about a patient within a healthcare setting. As it provides specifications and rules for the way the information is captured, it allows interoperability between all systems using the same framework. This is particularly important in a healthcare setting where there may be multiple systems capturing data that need to be able to interoperate to provide the full picture of a patient’s clinical and demographic history.

FHIR can be implemented in JSON, XML, or Turtle, or SQL schema.

## Resources

A FHIR data model is built from components called ‘resources’. Each resource spells out properties and rules around the information that is captured in that resource and how they are linked to other resources. Resources are the same across different systems using the same version of FHIR, but different systems may choose to implement different combinations of resources. Properties within resources are generally not required, so it is possible that systems using the same resources may not store exactly the same information.

The resources that are embedded in the core of FHIR are designed to be used by 80% of use cases. This ensures the standard does not become bloated with resources that are very specific to a small group of users. If users need to capture additional information then it is possible to do so via the use of extensions.

## Definitions

| term | meaning |
|---|---|
| extension | [Extensions](http://hl7.org/fhir/extensibility.html) can be added to any resource. They must be properly defined so that when they are exchanged, any system/user can understand what they mean. |
| Implementation Guide (IG) | A set of resources, profiles and extensions that help implementers establish an instance of FHIR within a particular domain. |
| profile | Profiles place constraints on the core FHIR resources to more precisely define what should be captured within an Implementation guide to better suit its use case. |
| resource | A modular set of defined, structured data items that join together to form a complete FHIR implementation. |
| Terminologies | [Terminologies](https://terminology.hl7.org/documentation.html#content) consist of Code Systems, Value Sets, Concept Maps, and Naming Systems. <br><br>- Code Systems are managed collections of concepts. <br>- Value Sets are managed collections of concepts drawn from one or more Code Systems. <br>- Naming Systems are collections of objects with known identifiers. <br>- Concept Maps are objects containing relationship information between concepts across code systems. |

## Extensions

## Implementation guides

Implementation guide registry: [https://fhir.org/guides/registry/](https://fhir.org/guides/registry/)

Australian Base implementation guide: [http://hl7.org.au/fhir/4.0.0/index.html](http://hl7.org.au/fhir/4.0.0/index.html)

## Profiles

## Terminologies

FHIR package registry: [http://registry.fhir.org/](http://registry.fhir.org/)

[(Duda et al. 2022; Vorisek et al. 2022)](https://www.zotero.org/google-docs/?hRYB0H)

## FHIR and genomics

The use of FHIR in the realm of Genomics is mainly in the domain of clinical genomics, though there are some investigations into its applicability in research settings (HERNANDEZ et al. 2022). The core of FHIR does not natively support genomics specific structured data. However, there have been several Implementation Guides that suit a more Genomics based use case:

- Australian Genomics’ Clinical Picture Repository Implementation Guide: [https://aehrc.github.io/genclipr-fhir-ig/index.html](https://aehrc.github.io/genclipr-fhir-ig/index.html)
- Genomics Reporting Implementation Guide: [http://hl7.org/fhir/uv/genomics-reporting/STU2/](http://hl7.org/fhir/uv/genomics-reporting/STU2/) (ALTEROVITZ et al. 2020)
- Phenopackets Implementation Guide: [http://phenopackets.org/core-ig/](http://phenopackets.org/core-ig/)

Given the complexity of genomics data, there has also been work to develop ‘genomic operations’ to allow for wrapping of genomic data repositories to integrate with electronic health records captured in FHIR (DOLIN et al. 2022).

There is ongoing work to improve the capture of genomic information in FHIR through the HL7 Clinical Genomics Workgroup (https://confluence.hl7.org/display/CGW) and GenomeX (https://confluence.hl7.org/display/COD/Genomics).