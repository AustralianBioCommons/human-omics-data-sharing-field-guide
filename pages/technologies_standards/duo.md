---
title: Data Use Ontology (DUO)
page_id: duo
type: technologies_standards
toc: true
description: GA4GH standard ontology for describing consent, access and use restrictions on datasets
contributors: [Marion Shadbolt, Conrad Leonard]
affiliations: [GA4GH]
---

![DUO logo](https://github.com/EBISPOT/DUO/raw/master/doc/figs/DUO_logo_white_background.png)

# DUO Codes: A Primer for Genomic Researchers

## Overview

The Data Use Ontology (DUO) provides standardized terms to describe the conditions under which human genomic data can be used. DUO helps align research activities with the consent provided by participants and simplifies the communication of data usage restrictions across institutions and borders. By utilizing DUO codes, researchers can clearly understand the permissions and constraints associated with data, ensuring that data use complies with ethical and legal standards. DUO is approved as a [GA4GH technical standard](https://www.ga4gh.org/news_item/data-use-ontology-approved-as-a-ga4gh-technical-standard/).

## What Are DUO Codes?

DUO is a controlled vocabulary designed to represent data use limitations (DUL) in genomic research. It is essential for ensuring compliance with the conditions under which data were consented to by participants. DUO terms are used by data repositories and research consortia to categorize datasets based on their allowed use, whether for general research, specific diseases, or non-commercial purposes.

DUO is often used in conjunction with other ontologies, such as MONDO, to specify disease-specific restrictions in more detail. For example, a dataset might be restricted to studies on a particular disease.

## Example DUO Code Categories

1. **General Research Use (GRU) DUO:0000042**: Data may be used for any type of research.
   
2. **Disease-Specific Research (DS) DUO:0000007**: Data usage is limited to studies focused on a specific disease or a set of related diseases.

3. **Non-Commercial Use (NCU) DUO:0000046**: Data may only be used by non-commercial entities, such as academic institutions or public health agencies.

4. **No restriction (NRES) DUO:0000004**: There is no restriction on use

---

## Example: DUO and MONDO in Action

Consider a dataset in the European Genome-phenome Archive (EGA) that is restricted to research on juvenile idiopathic arthritis. In this case, the data would be tagged with two codes:

- **DUO:0000007 (Disease-Specific Research Use)**: Restricts use of the data to research on a particular disease.
- **MONDO:0011429**: Specifies the disease as juvenile idiopathic arthritis.

Thus, if a researcher requests access to this dataset, they would need to demonstrate that their research focuses specifically on juvenile idiopathic arthritis. Data usage outside this scope, such as studying another disease, would not be allowed.

---

## Why DUO Matters

DUO codes are vital for ensuring that genomic data is used ethically and in line with participant consent. They provide clarity for researchers and institutions, simplify the data access request process, and ensure that datasets are used appropriately across different research contexts. DUO also enhances data governance by making data-sharing policies transparent and easier to enforce.

---

### References

1. **DUO Specification (GA4GH)**: [Data Use Ontology](https://github.com/EBISPOT/DUO)  
   Official specification, including the full list of DUO codes.
2. **GA4GH DUO Documentation**: [GA4GH DUO](https://www.ga4gh.org/genomic-data-toolkit/data-use-ontology/)  
   Comprehensive documentation on DUO and its applications.
3. **DUO Use in EGA**: [EGA Data Access](https://ega-archive.org/access/data-access-committee/data-use-ontology/)  
