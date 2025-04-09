---
title: Ontologies
page_id: ontologies.md
type: technologies_standards
toc: true
description: A summary of ontologies and resources to help with searching and ontology curation
contributors: [Joshua Harris, Marion Shadbolt]
affiliations: []
---

Ontologies are essential tools in medical research, providing structured frameworks to represent, organise, and share complex biomedical knowledge. This guide explores what ontologies are, their advantages and limitations, how they are used in medical research, and introduces two critical infrastructure tools: the EMBL-EBI Ontology Lookup Service (OLS) and CSIRO's Ontoserver. It concludes with a summary of prominent ontologies used in the field.

---

## What Are Ontologies?

Ontologies are formal representations of knowledge within a specific domain, such as medicine. They define concepts (e.g., diseases, symptoms, treatments) and the relationships between them in a structured manner that is both human-readable and machine-processable. Unlike simple vocabularies or taxonomies, ontologies enable reasoning and inference by embedding logical rules and axioms. For example, an ontology can infer that "viral meningitis" is a subtype of "infectious meningitis" or that "penicillin" is a treatment for "bacterial infections."

In medical research, ontologies are indispensable for standardising terminology across systems, facilitating semantic interoperability, and enabling advanced data analysis. They play a critical role in integrating heterogeneous datasets from electronic health records (EHRs), genomic databases, and clinical studies.

---

## Why Use Ontologies in Medical Research?

### Advantages

- **Semantic Interoperability**: Ontologies standardise terminology across different systems, enabling seamless integration of data from diverse sources.
- **Enhanced Reasoning**: Logical rules embedded in ontologies allow automated inference, supporting tasks like disease prediction or treatment recommendations.
- **Data Standardisation**: By providing consistent definitions for medical concepts, ontologies reduce ambiguity and improve data quality.
- **Support for Advanced Analytics**: Ontologies facilitate sophisticated queries and data mining in large datasets, uncovering patterns that may not be immediately apparent.
- **Clinical Decision Support**: Many clinical decision support systems rely on ontologies to provide evidence-based recommendations by linking symptoms to diagnoses or treatments.


### Limitations

Despite their strengths, ontologies face several challenges:

- **Development Complexity**: Creating comprehensive ontologies requires expertise in both medicine and ontology engineering.
- **Scalability Issues**: Large ontologies like SNOMED CT can become unwieldy to maintain as they grow.
- **Integration Challenges**: Aligning multiple ontologies often reveals conflicting definitions or hierarchies.
- **Contextual Limitations**: Ontologies may struggle to represent nuanced or context-dependent aspects of medical knowledge.

---

## Infrastructure Tools for Ontology Management

### EMBL-EBI Ontology Lookup Service (OLS)

The Ontology Lookup Service (OLS), developed by EMBL-EBI's Samples, Phenotypes and Ontologies Team (SPOT), is a centralised repository for biomedical ontologies. It provides access to hundreds of ontologies through a user-friendly interface and programmatic API. OLS supports searching, browsing, visualising ontology structures, and querying metadata.

One of OLS’s key features is its ability to track ontology evolution through versioning systems. It uses an ontology crawler to detect changes in external ontologies and updates its database accordingly. This ensures researchers always have access to the latest versions of terminologies. Additionally, OLS integrates with related tools like OxO (for cross-ontology mappings) and Zooma (for mapping data to ontology terms).

OLS has become a cornerstone for biomedical researchers needing quick access to standardised terminologies. For example, it is widely used in genomic studies to annotate datasets with terms from Human Phenotype Ontology (HPO) or Gene Ontology (GO). Its SPARQL endpoint allows complex queries across multiple ontological frameworks.

---

### CSIRO's Ontoserver

Ontoserver is a world-leading clinical terminology server developed by the Australian eHealth Research Centre at CSIRO. It implements Fast Health Interoperability Resources (FHIR) standards to simplify the use of clinical terminologies like SNOMED CT and Human Phenotype Ontology (HPO).

Ontoserver excels at translating clinical descriptions into standardised codes through fast incremental searches and context-specific result ranking algorithms. It supports multiple versions of terminologies and offers sub-millisecond response times for code searches. Its syndication capabilities allow automatic updates from central servers, ensuring users always have access to the latest terminology resources.

A key application of Ontoserver is its integration into genotype-phenotype databases for rare diseases. By leveraging HPO alongside SNOMED CT, it facilitates data sharing between institutions while improving clinical understanding through standardisation. For example, Australian health organisations use Ontoserver to enhance EHR interoperability by embedding coded medical data directly into patient records.

---

## Commonly Used Medical Ontologies

| **Ontology** | **Description** | **Applications** |
| :-- | :-- | :-- |
| **SNOMED CT** | Comprehensive clinical terminology with 350,000+ concepts | EHR integration; clinical decision support |
| **Human Phenotype Ontology (HPO)** | Standardised representation of phenotypic abnormalities | Rare disease diagnosis; genotype-phenotype databases |
| **ICD-10/ICD-O** | WHO classification system for diseases and oncology | Statistical reporting; epidemiological studies |
| **Data Use Ontology (DUO)** | Encodes consent-based restrictions for data sharing | Automates access control for genomic datasets |
| **LOINC** | Standardises laboratory observations | Interoperability between diagnostic systems |
| **Gene Ontology (GO)** | Represents gene functions | Functional genomics; protein interaction studies |
| **UMLS Metathesaurus** | Integrates 100+ terminological systems | Cross-system terminology mapping; natural language processing |

---

## How Are Ontologies Used in Medical Research?

Medical researchers use ontologies in various ways:

1. **Clinical Decision Support Systems**: SNOMED CT provides the backbone for many decision support tools by linking symptoms to diagnoses or treatments.
2. **Genomic Data Annotation**: HPO terms are widely used to annotate phenotypic data in genomic studies, improving rare disease diagnosis accuracy.
3. **EHR Integration**: Tools like Ontoserver embed standardised terminologies directly into patient records for better interoperability across healthcare systems.
4. **Data Sharing Frameworks**: DUO facilitates ethical sharing of genomic datasets by automating consent-based restrictions.

---

## Summary Table

| Feature/Tool | Description | Key Benefits | Example Use Case |
| :-- | :-- | :-- | :-- |
| **Ontology Lookup Service (OLS)** | Central repository for biomedical ontologies | Access latest ontology versions; supports complex queries | Annotating genomic datasets with HPO |
| **Ontoserver** | FHIR-based clinical terminology server | Fast searches; automatic updates; multi-version support | Embedding SNOMED CT codes into EHRs |

---

## Conclusion

Ontologies are vital tools for organising biomedical knowledge and enabling effective health data sharing across institutions. With infrastructure like EMBL-EBI’s OLS and CSIRO’s Ontoserver supporting ontology management and integration, researchers can leverage standardised terminologies to improve interoperability, enhance analytics capabilities, and streamline workflows in medical research.

By adopting these tools alongside widely used ontological frameworks such as SNOMED CT or HPO, researchers can overcome challenges associated with fragmented health data systems while advancing precision medicine initiatives globally.


## References

- [Ontology Archive Data - Human Cell Atlas](https://ontology.archive.data.humancellatlas.org)
- [CEUR Workshop Proceedings - Paper 29](https://ceur-ws.org/Vol-1546/paper_29.pdf)
- [PMC Article - PMC2896109](https://pmc.ncbi.nlm.nih.gov/articles/PMC2896109/)
- [Australian Genomics - Standardising Clinical Phenotype](https://www.australiangenomics.org.au/standardising-clinical-phenotype-csiros-ontoserver-and-shrimp/)
- [Ontoserver Documentation - Overview 6.19.2](https://ontoserver.csiro.au/docs/6.19.2/overview.html)
- [Talking HealthTech - Ontoserver CSIRO](https://www.talkinghealthtech.com/glossary/ontoserver-csiro)
- [Ontoserver Documentation - Overview 6](https://ontoserver.csiro.au/docs/6/overview.html)
- [Ontoserver Solutions](https://ontoserver.csiro.au/site/our-solutions/ontoserver/)
- [Ontology Archive Data - About](https://ontology.archive.data.humancellatlas.org/docs/about)
- [EMBL-EBI Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols4)
- [PMC Article - PMC8591903](https://pmc.ncbi.nlm.nih.gov/articles/PMC8591903/)
- [EMBL-EBI OLS Ontologies](https://www.ebi.ac.uk/ols4/ontologies)
- [CINECA Project - Data Harmonization and Enrichment](https://www.cineca-project.eu/blog-all/data-harmonization-and-enrichment-using-embl-ebi-ontology-tools)
- [GitHub - EBISPOT OLS](https://github.com/EBISPOT/OLS)
- [GitHub - EBISPOT DUO](https://github.com/EBISPOT/DUO)
- [Ontology Archive Data - Installation Guide](https://ontology.archive.data.humancellatlas.org/docs/installation-guide)
- [Cookbook Dev - Technical and Architectural Selection Criteria of Ontology Lookup Services](https://egonw.github.io/cookbook-dev/content/recipes/infrastructure/vocabularies/technical-and-architectural-selection-criteria-of-ontology-lookup-services.html)
- [Ontoserver FAQs](https://ontoserver.csiro.au/site/faqs/)
- [Ontoserver About](https://ontoserver.csiro.au/site/about/)
- [Ontoserver Site](https://ontoserver.csiro.au/site/)
- [Ontoserver Solutions](https://ontoserver.csiro.au/site/our-solutions/)
- [Ontoserver Documentation - Changelog 6](https://ontoserver.csiro.au/docs/6/changelog.html)
- [YouTube - Ontoserver Overview](https://www.youtube.com/watch?v=r2LTZPlRd5Q)
- [CSIRO News - NCTS Digital Healthcare](https://www.csiro.au/en/news/all/articles/2024/november/ncts-digital-healthcare)
- [Ontoserver Technical Documentation - Atomio Config](https://ontoserver.csiro.au/site/technical-documentation/atomio/atomio-config/)
- [Ontoserver Documentation](https://ontoserver.csiro.au/docs/)
- [AEHRC - Transforming Healthcare with the National Clinical Terminology Service](https://aehrc.csiro.au/transforming-healthcare-with-the-national-clinical-terminology-service/)
- [Ontoserver Documentation - Changelog 6.19.2](https://ontoserver.csiro.au/docs/6.19.2/changelog.html)
- [Australian Genomics - Tools and Resources](https://www.australiangenomics.org.au/tools-and-resources/ontoserver/)
- [YouTube - Ontoserver Introduction](https://www.youtube.com/watch?v=p8XF7yJvW4E)
- [re3data - Repository r3d100010413](https://www.re3data.org/repository/r3d100010413)
- [ELIXIR Europe - RIR Selection](https://elixir-europe.org/intranet/forms/rir-selection/sid442)
- [FAIR Cookbook - Selecting and Using Ontology Lookup Services](https://fairplus.github.io/the-fair-cookbook/content/recipes/infrastructure/vocabularies/Selecting_and_using_ontology_lookup_services.html)
- [TeSS ELIXIR - Data Harmonization and Enrichment](https://tess.elixir-europe.org/materials/data-harmonization-and-enrichment-using-embl-ebi-ontology-tools)
- [Ontoserver Technical Documentation - Design Considerations](https://ontoserver.csiro.au/site/technical-documentation/ontoserver-technical-documentation/planning-a-deployment/design-considerations-infrastructure-implications/)
- [STB Blog - Ontoserver OpenShift](https://www.stb.id.au/blog/ontoserver-openshift)
- [Ontoserver Technical Documentation - Security Features](https://ontoserver.csiro.au/site/technical-documentation/ontoserver-technical-documentation/planning-a-deployment/security-features-and-considerations/)
