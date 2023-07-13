---
title: Omics Discovery Index
type: repositories
contributors: [Marion Shadbolt]
description: Index to query across multiple omics databases.
affiliations: [EMBL-EBI, ELIXIR Europe, GB]
---

{% tool "omicsdi" %} enables users to search across multiple repositories rather than performing searches at each one {% cite perez-riverol_discovering_2017 %}. One example use case is searching for human data across the main 3 human data repositories, EGA, dbGaP, JGA which is not otherwise possible. It may also be useful for searching across ArrayExpress and GEO, the two main repositories that house functional genomics data. The index currently contains ~2.7 million datasets from 24 repositories. The databases currently indexed can be [found on their website](https://www.omicsdi.org/database).

## References

{% bibliography --cited %}