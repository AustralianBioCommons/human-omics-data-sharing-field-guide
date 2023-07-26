---
title: BioStudies
page_id: biostudies
type: repositories
contributors: [Marion Shadbolt]
description: Database for storing project level information and linking to other repositories.
affiliations: [EMBL-EBI, GB]
---

{% tool "biostudies" %} is a repository for storing project level information under a stable accession along with any data that does not fit into any of the other resources of the EBI {% cite sarkans_biostudies_2018 %}. It includes project abstract, authors (including ORCIDs) and publication. Studies can be linked to other EBI resources such as data in Biosamples and the ENA. BioStudies provides that backend database behind {% tool "arrayexpress" %}, {% tool "bioimage-archive" %}, and {% tool "empiar" "%}.

Studies are submitted through a [web-based submission tool](https://www.ebi.ac.uk/biostudies/submit). Studies may also be queried through their [REST API](https://www.ebi.ac.uk/biostudies/help#rest-api-docs).

{% bibliography --cited %}