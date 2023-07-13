---
title: Beacon
type: technologies_standards
toc: true
description: Beacon is an API framework and metadata model to enable discoverability of genomic variants and related cohort and individual level metadata.
contributors: [Marion Shadbolt]
affiliations: [Beacon, GA4GH, Centre for Genomic Regulation]
---

The main aim of {% tool "beacon" %} is to enable data discoverability of datasets with criteria of interest, including clinical, demographic, experimental and variant level data {% cite rambla_beacon_2022 %}. It provides a common [data model and a framework specification](https://github.com/ga4gh-beacon/beacon-v2) for how the metadata can be queried via API {% cite rambla_beacon_2022 %}. Many Beacons can be aggregated into a single network, allowing single queries to be sent to multiple individual Beacon instances {% cite rambla_beacon_2022 %}. It was approved as a GA4GH standard in April, 2022 {% cite ga4gh_new_2022 %}.

The {% tool "beacon" %} model is based on [seven object types](https://docs.genomebeacons.org/models/#introduction) with default schemas. Schemas have minimal required fields and can be expanded with additional fields to suit the needs of a particular implementation. The model structure is highly nested and ontologised. There are recommended ontologies for particular fields but nothing is enforced as it is expected that communities will choose ontologies based on what best suits their use case. This offers flexibility but may present challenges when aggregating multiple Beacons with different ontology curations.

## Implementations

Since Beacon is a specification framework, anyone is free to develop their own implementation which meets the specification. Implementations can be registered on the [EGA registry server](https://ga4gh-approval-service-registry-demo.ega-archive.org/) which assesses how well an implementation matches the spec. A few implementations are described in more detail below as well as on the [Beacon documentation](https://docs.genomebeacons.org/other-implementations/). 

### Reference Implementation

The reference implementation was developed by the CRG and is built on an internal Mongo DB with APIs defined in Python {% cite rueda_beacon_2022 %}. It is intended as a starting point for those who want to try out Beacon and gives them a head start on the resourcing required to light a Beacon. 

There are [tutorials](https://b2ri-documentation.readthedocs.io/en/latest/) available in order to understand how to 'beaconize' your data, ingest it into the database and set up the API {% cite rueda_beacon_2022 %}.

The two main GitHub repos are:

[<i class="fa-brands fa-github"></i> Beacon v2 Reference Implementation (Data ingestion tools)](https://github.com/EGA-archive/beacon2-ri-tools)

[<i class="fa-brands fa-github"></i> Beacon v2 Reference Implementation (API)](https://github.com/EGA-archive/beacon2-ri-api)

### Serverless Beacon (sBeacon)

A serverless implementation of the Beacon specification has been developled by the Transformational Bioinformatics team at [CSIRO AERC](https://aehrc.csiro.au/research/cloud-native-genomics/). This 'on-demand' implementation can offer a fast and cost-effective way of running a Beacon as the cost is proportional to how much it is used, rather than a constant running cost. Originally published to the [version 1 specification](https://github.com/aehrc/terraform-aws-serverless-beacon), developers are now updating the implementation to support [Beacon v2](https://github.com/aehrc/terraform-aws-serverless-beacon/tree/dev).

An investigation of the in-progress v2 sBeacon implementation by the team at the University of Melbourne Centre for Cancer Research can be explored here: 

[<i class="fa-brands fa-github"></i> *sbeacon-exploration*](https://github.com/umccr/sbeacon-exploration)

### Java Beacon (jBeacon)

A Java implementation of the Beacon v2 Specification has been developed by the Barcelona Supercomputing Centre (BSC) {% cite repchevsky_open_2022 %}.

An investigation of the jBeacon implementation by the team at the University of Melbourne Centre for Cancer Research can be explored here: 

[<i class="fa-brands fa-github"></i> *jbeacon-exploration*](https://github.com/umccr/beacon-doc)

## Beacon networks

### ELIXIR Beacon network

The [ELIXIR Beacon network](https://beacon-network.elixir-europe.org/) brings together 11 beacons from across Europe. Most Beacons are at version 1. It is possible to register a Beacon into this system following the [instructions](https://beacon-network.elixir-europe.org/join).

### GA4GH Beacon network

The [GA4GH Beacon network](https://beacon-network.org/#/) aggregates data from over 40 institutes. It contains variants mapped to GRCh37 and no contextual metadata as it is aggregating version 1 beacon data. It is maintained and hosted by DNAstack. It isn't clear whether this is actively maintained and will be adapted to the version specification.

## References
{% bibliography --cited %}
