---
title: Phenopackets
page_id: phenopackets
type: technologies_standards
toc: true
description: Phenopackets are a way of exchanging structured clinical, demographic and phenotypic metadata in a standardised way.
contributors: [Marion Shadbolt, Conrad Leonard]
affiliations: [GA4GH]
---

```yaml
# The following block describes Decreased fetal movement.

- type:
    id: "HP:0001558"
    label: "Decreased fetal movement"
  onset:
    ontologyClass:
      id: "HP:0011461"
      label: "Fetal onset"
  evidence:
  - evidenceCode:
      id: "ECO:0000033"
      label: "author statement supported by traceable reference"
    reference:
      id: "PMID:30808312"
      description: "COL6A1 mutation leading to Bethlem myopathy with recurrent hematuria:\
        \ a case report."
```

**Documentation** https://phenopacket-schema.readthedocs.io/en/latest/

**GitHub** https://github.com/phenopackets/phenopacket-schema

## Description

Phenopackets are a standard data format designed for sharing structured information about
phenotypic abnormalities and their associations with genetic or other data. Developed by the
Global Alliance for Genomics and Health (GA4GH), phenopackets capture detailed information
about a patient's phenotype, medical history, and, optionally, genetic data such as variants
or omics findings. This standard enables interoperability across research and clinical
settings, allowing consistent representation and exchange of data in studies of rare
diseases, cancer, and other areas where phenotype-genotype correlations are critical.

Phenopackets are designed to work closely with the HPO ontology for phenotype, and the
VRS standard for genomic variant representation. Phenopackets have a native binary format
defined using Protocol Buffers (protobuf), and may be encoded in JSON or YAML making them
machine-readable while maintaining human interpretability. Phenopackets are registered as an
[ISO standard](https://www.iso.org/standard/79991.html)

## What they are not

Phenopackets are not a comprehensive electronic health record (EHR) or a system for managing
clinical workflows. Instead, they focus on phenotypic and genomic data and are intended to
complement, not replace, existing clinical or research systems. The format is specific,
structured, and optimized for cross-platform data sharing and integration into bioinformatics
pipelines or research projects. The phenopacket schema is not designed as a primary data
storage schema (*cf.* OMOP)

Phenopackets and FHIR differ significantly in their scope. Phenopackets focus on capturing
detailed phenotypic and genomic data, particularly for research and precision medicine use
cases like rare diseases and cancer. They are designed to facilitate data sharing between
researchers and clinicians by providing a standardized, lightweight format for describing
phenotypes, diagnoses, genetic findings, and medical histories.

In contrast, FHIR (Fast Healthcare Interoperability Resources) has a much broader scope,
covering all aspects of healthcare data exchange. FHIR is designed for clinical and
administrative use cases, including patient records, medication management, scheduling,
billing, and much more. It provides a comprehensive framework for healthcare interoperability
and supports a wide variety of data types and workflows.

## Technical Implementation

The technical implementation of phenopackets is simple and focused. They use JSON or Protocol
Buffers for encoding, which makes them lightweight, easy to parse, and well-suited for research
pipelines. The schema is specific, concise, and tailored to phenotypic and genomic data,
enabling rapid adoption for its niche use cases. Phenopackets rely heavily on controlled
vocabularies, such as the Human Phenotype Ontology (HPO), to ensure consistency in describing
phenotypic abnormalities.

(FHIR, in contrast, is a comprehensive and modular standard based on RESTful APIs and supports
data representation in JSON, XML, or RDF. Its resources are highly extensible and interoperable,
allowing for detailed customization to fit the needs of diverse healthcare systems. However,
FHIR’s complexity can make implementation challenging, especially for organizations with
limited technical resources.)

### Examples

https://phenopacket-schema.readthedocs.io/en/stable/examples.html

* [Rare Disease](https://phenopacket-schema.readthedocs.io/en/stable/rd-example.html)
* [Cancer](https://phenopacket-schema.readthedocs.io/en/stable/cancer-example.html)
* [COVID-19 case report](https://phenopacket-schema.readthedocs.io/en/stable/covid19-example.html)



### Mappings to other models 

* [Phenopackets -> OMOP](https://github.com/phenopackets/omop-exporter)
* [OMOP -> Phenopackets](https://github.com/kaylas2138/omop2pheno)
* [(various) -> Phenopackets](https://github.com/CNAG-Biomedical-Informatics/convert-pheno)

### Further reading

[The GA4GH Phenopacket Schema — a presentation by Monica C. Munoz-Torres](https://docs.google.com/presentation/d/14xk2NpCtlOSbiPVp7RQrfWYMJTRB-tsuSZoyEejmENU/edit#slide=id.g134dd7d6c0a_0_1072)


## References

{% bibliography --cited %}
