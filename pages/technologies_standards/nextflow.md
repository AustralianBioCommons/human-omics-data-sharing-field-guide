---
title: Nextflow
page_id: nextflow
type: technologies_standards
toc: true
description: Workflow execution framework
contributors: [Irene Hung, Bernie Pope]
affiliations: []
---

## What is Nextflow?

Nextflow is an open-source workflow management system that enables the development and execution of computational pipelines for data analysis. Many other similar computational workflow systems exist, often employed in the field of bioinformatics, where complex and interconnected computations are performed over large datasets in a distributed fashion. At the time of writing, Nextflow has risen in popularity, but other prominent examples include Common Workflow Language (CWL), Workflow Description Language (WDL), Snakemake, and Galaxy. The need for this type of tool is becoming increasingly prevalent with the rise of big data and the growing demand for capability to perform analysis on these datasets in a reproducible manner (see [here](https://www.nextflow.io/docs/latest/overview.html) for more information). Nextflow workflows are written using a domain specific language implemented in the Groovy programming language. Effectively these are stylised programs that are specialised for the task of describing computational pipelines of interconnected tools. Nextflow was originally developed by the Centre for Genomic Regulation in Spain with the first public release in 2013. Later, in 2018 a commercial spin-off company called Seqera Labs was formed to provide support and consulting for Nextflow related systems. A community of nextflow users and developers has assembled to collect a curated set of open‑source analysis workflows built using Nextflow called [nf-core](https://nf-co.re/).

### Key features

- **Flexibility**: Operates across different computing environments e.g. local machines, high-performance computing clusters, and cloud platforms (like AWS, Google Cloud, and Azure).

- **Scalability**: Easily scales from local to large computing setups by enabling modular and parallel execution of processes. It also enables dynamic scaling of resources based on workload and environment, and can take advantage of clusters of computers in HPC systems or in the cloud.

- **Reproducibility**: Promotes reproducible research by tracking data and processes, and encouraging community contributions, allowing researchers to reuse and adapt existing workflows easily.

- **Integration**: Supports various programming languages and tools commonly used in bioinformatics and data science e.g. container technologies, cloud services and job schedulers. Nextflow also provides APIs for integration with other tools and systems, enabling custom extensions and enhancements to workflows.

## References
- [Nextflow Overview](https://www.nextflow.io/docs/latest/overview.html)
- [Seqera Labs - Nextflow](https://seqera.io/nextflow/)
- [Nextflow GitHub Repository](https://github.com/nextflow-io/nextflow)
