---
title: Gene Expression Omnibus
type: repositories
contributors: [Marion Shadbolt]
description: Open access database for functional genomics data.
affiliations: [NCBI, US]
---

The Gene Expression Omnibus ({% tool "geo" %}) is an open access data repository for functional genomics data. Submissions need to conform to Minimum INformation About a Microarray Experiment ([MIAME](https://doi.org/10.25504/FAIRsharing.32b10v)) and Minimum INformation about a SEQuencing Experiment ([MINSEQE](https://doi.org/10.25504/FAIRsharing.a55z32)) standards. It is run by the NCBI in the US and is analogous to ArrayExpress. Raw data gets submitted to the NCBI SRA behind the scenes and additional matrices and metadata can be uploaded. In general, metadata is less curated and is of a lower standard. It is possible to create submissions with summary expression data only if raw data needs to be controlled access. GEO has an [API](https://www.ncbi.nlm.nih.gov/geo/info/geo_paccess.html) for querying as well as a Bioconductor for interacting with the database through R {% cite davis_geoquery_2022 davis_geoquery_2007 %}.

## References

{% bibliography --cited %}