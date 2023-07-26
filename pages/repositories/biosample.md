---
title: BioSample
page_id: biosample
type: repositories
contributors: [Marion Shadbolt]
description: Object used to describe samples when submitting to INSDC and CNCB repositories
---

All major archives have some version of a ‘sample’ object that stores sample related metadata. The {% tool "NCBI" %} (SRA), {% tool "DDBJ" %} and {% tool "cncb-ngdc" %}  databases are limited to storing metadata that gets submitted when submitting a study to their related genome archives.

As well as storing metadata from samples that are submitted as part of an ENA submission, the EBI’s {% tool "biosamples" %} database can be used for any form of sample metadata archiving and can be linked to other EBI archives at a later point. It is flexible to store any kind of key value pair and values can be linked to ontologies. Multiple BioSamples can be linked together, for example, a virus sample could be linked to a sample from its host through a ‘Derived from’ relationship. Samples may also be linked under a project by specifying a ‘project’ key.

Samples can be linked to {% tool "ega" %} projects if sample metadata provided is openly accessible (e.g. [https://www.ebi.ac.uk/biosamples/samples/SAMEA4940335](https://www.ebi.ac.uk/biosamples/samples/SAMEA4940335) ).

Metadata can be submitted and queried via their [REST API](https://www.ebi.ac.uk/biosamples/docs/references/api/overview). There is a [python wrapper](https://github.com/Kerruba/python_biosamples-v4_lib) though it is not actively maintained.

Can be used to provide a stable identifier to project samples as they are being processed and then linked to the final archival submission e.g. HipSci project example {% cite streeter_human-induced_2017 %}, FAANG project example [https://www.ebi.ac.uk/biosamples/samples?filter=attr%3Aproject%3AFAANG](https://www.ebi.ac.uk/biosamples/samples?filter=attr%3Aproject%3AFAANG) [https://data.faang.org/specimen](https://data.faang.org/specimen)  [https://www.faang.org/](https://www.faang.org/)


## References

{% bibliography --cited %}