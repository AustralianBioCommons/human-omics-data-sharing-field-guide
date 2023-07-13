---
title: ArrayExpress
page_id: arrayexpress
type: repositories
contributors: [Marion Shadbolt]
description: Open access database for functional genomics data including transcriptomics and micro-arrays.
affiliations: [EMBL-EBI, GB]
---

{% tool "arrayexpress" %} is a repository for functional genomic data, usually transcriptomic raw reads but was originally created for microarray data (thus the name) run by the EBI {% cite athar_arrayexpress_2019 %}. Submission is through the annotare web interface. Behind the scenes, metadata gets submitted to Biosamples and raw sequence files get submitted to the ENA but with upgraded metadata. Expression matrices can also be submitted to ArrayExpress. Each dataset is curated to ensure it meets the ArrayExpress MAGE-TAB metadata standard for the particular type of experiment and data being submitted. As raw data is stored in the ENA and made available openly, it is not suitable for data that requires controlled access. It is possible to create submissions in ArrayExpress that contain openly available metadata along with a summary expression matrix and link to raw data in the EGA to allow for more discoverability of controlled access functional genomic datasets via ArrayExpress.

Many ArrayExpress experiments have ‘ExpressionSet’ objects that can be downloaded and loaded directly into R. They can also be accessed through the ‘ArrayExpress’ Bioconductor package {% cite kauffmann_arrayexpress_2022 %}. Data and metadata in ArrayExpress can be queried programmatically through the [BioStudies API endpoints](https://www.ebi.ac.uk/biostudies/arrayexpress/help#programmatic).

Data is either submitted directly by contributors or curated from other sources such as the HCA and GEO.

## References

{% bibliography --cited %}