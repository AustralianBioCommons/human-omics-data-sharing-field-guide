---
title: Beacon
toc: true
description: Beacon is an API framework and metadata model to enable discoverability of genomic variants and related cohort and individual level metadata.
contributors: [Marion Shadbolt]
affiliations: [Beacon, GA4GH]
---

## Beacon v2

The main aim of Beacon v2 is to enable data discoverability of datasets with criteria of interest, including clinical, demographic, experimental and variant level data {% cite rambla_beacon_2022 %}. It provides a common [data model and a framework](https://github.com/ga4gh-beacon/beacon-v2) specification for how the metadata can be queried via API {% cite rambla_beacon_2022 %}. Many Beacons can be aggregated into a single network, allowing single queries to be sent to multiple individual Beacon instances {% cite rambla_beacon_2022 %}. It was approved as a GA4GH standard in April, 2022 .

{% include image.html file="https://github.com/ga4gh-beacon/beacon-v2/blob/main/docs/img/Schema.png" caption="Diagram of Beacon v2 schemas." alt="Beacon v2 schemas" max-width="10" %}


![Beacon model](https://github.com/ga4gh-beacon/beacon-v2/blob/main/docs/img/Schema.png)

## Implementations

### Reference Implementation

### Serverless Beacon

### Java Beacon

## Beacon networks

### ELIXIR Beacon network

The [ELIXIR Beacon network](https://beacon-network.elixir-europe.org/) brings together 11 beacons from across Europe. Most Beacons are at version 1. It is possible to register a Beacon into this system following the [instructions](https://beacon-network.elixir-europe.org/join).

### GA4GH Beacon network

The [GA4GH Beacon network](https://beacon-network.org/#/) aggregates data from over 40 institutes. It contains variants mapped to GRCh37 and no contextual metadata as it is aggregating version 1 beacon data. It is maintained and hosted by DNAstack. It isn't clear whether this is actively maintained and will be adapted to the version specification.



Beacon v1 was a simple protocol to discover the presence/absence of variants across cohorts. It 

rambla_beacon_2022



stuff about sbeacon

beacon network

reference implementation 
etc

rueda_beacon_2022