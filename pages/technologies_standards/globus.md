---
title: Globus
page_id: globus
type: technologies_standards
toc: true
description: A tool for moving large amounts of data across distance at speed.
contributors:  [Joshua Harris]
affiliations:  []
---


Globus, developed and maintained by the University of Chicago, is a transformative research data management platform designed to address the challenges of moving, sharing, and discovering large-scale scientific data across distributed systems. By abstracting the complexities of data transfer protocols, storage systems, and security frameworks, Globus empowers researchers to focus on their scientific objectives rather than infrastructure logistics. This article explores Globus’ core functionalities, use cases, limitations, applications in human genomics, and operational workflows, supplemented by a case study demonstrating its real-world impact.

---

## Understanding Globus: Purpose and Architecture

### Defining Globus

Globus is a cloud-based service that provides secure, reliable, and scalable solutions for research data management. It operates as a not-for-profit platform, offering both free and subscription-based tiers to academic institutions, national laboratories, and commercial entities ([1](https://www.globus.org/what-we-do), [6](https://www.osc.edu/resources/getting_started/howto/howto_use_globus_overview)). The system’s architecture integrates federated identity management (via Globus Auth), high-performance data transfer (via GridFTP and HTTPS), and programmable interfaces (REST APIs, Python SDK) to create a unified ecosystem for data handling ([1](https://www.globus.org/what-we-do), [6](https://www.osc.edu/resources/getting_started/howto/howto_use_globus_overview)).

### Core Functionalities

1. **Data Transfer**: Globus enables seamless movement of data ranging from kilobytes to petabytes between endpoints, including supercomputers, cloud storage, and personal devices ([1](https://www.globus.org/what-we-do), [6](https://www.osc.edu/resources/getting_started/howto/howto_use_globus_overview)).
2. **Secure Sharing**: Researchers can share data with collaborators using email addresses or institutional identities, with fine-grained access controls for protected datasets ([6](https://www.osc.edu/resources/getting_started/howto/howto_use_globus_overview), [8](https://ncifrederick.cancer.gov/about/theposter/content/using-globus-transfer-and-share-big-data)).
3. **Automation**: Tools like Globus Flows allow users to orchestrate multi-step data workflows, such as periodic transfers between storage systems or integration with high-performance computing (HPC) resources ([1](https://www.globus.org/what-we-do), [7](https://pmc.ncbi.nlm.nih.gov/articles/PMC4203657/)).
4. **Discovery**: The platform supports metadata cataloguing and search APIs, enabling the creation of domain-specific data portals ([1](https://www.globus.org/what-we-do), [2](https://www.globus.org/user-stories)).

---

## Use Cases Across Scientific Domains

### Genomics and Biomedical Research

Globus has become indispensable in genomics, where next-generation sequencing (NGS) generates terabytes of raw data per experiment. For example, the University of Michigan’s Advanced Genomics Core processes 6 TB of sequencing data per run, using Globus to automate transfers between sequencers, HPC clusters, and long-term archives ([4](https://www.globus.org/user-stories/genomic-researchers-umichigan), [12](https://pubmed.ncbi.nlm.nih.gov/26925205/)). The system’s ability to handle protected health information (PHI) under HIPAA compliance makes it suitable for clinical genomics collaborations ([8](https://ncifrederick.cancer.gov/about/theposter/content/using-globus-transfer-and-share-big-data), [13](https://www.globus.org/sites/default/files/case-study-dobyns-pediatric-brain-research-lab.pdf)).

### Multi-Institutional Collaborations

Projects like the Natural Hazards Engineering Research Infrastructure (NHERI) rely on Globus to distribute earthquake simulation datasets across 16 institutions. The CyberShake project transferred over 700 TB of seismic hazard models between Oak Ridge National Laboratory and the San Diego Supercomputer Center using Globus’ fault-tolerant transfer protocols ([2](https://www.globus.org/user-stories), [7](https://pmc.ncbi.nlm.nih.gov/articles/PMC4203657/)).

### Cloud and Hybrid Infrastructure Integration

Organisations such as Rice University leverage Globus connectors to bridge on-premises HPC resources with cloud storage (e.g., Google Drive, AWS S3). This hybrid approach enables cost-effective archiving while maintaining low-latency access to active datasets ([2](https://www.globus.org/user-stories), [10](https://globus.stanford.edu/cloud/drive.html)).

### Data Publication and DOI Assignment

Oak Ridge National Laboratory’s Digital Object Identifier (DOI) service uses Globus shared endpoints to streamline data publication. Researchers assemble datasets across multiple storage systems, which Globus then packages with metadata for DOI minting via DataCite ([2](https://www.globus.org/user-stories), [13](https://www.globus.org/sites/default/files/case-study-dobyns-pediatric-brain-research-lab.pdf)).

---

## Technical Limitations and Considerations

### Data Size and Throughput Constraints

While Globus excels at bulk transfers, its Compute service imposes strict limits:

- **10 MB maximum payload** per task submission ([3](https://globus-compute.readthedocs.io/en/stable/limits.html))
- **750 GB daily upload quota** when using Google Drive connectors ([10](https://globus.stanford.edu/cloud/drive.html))
- **400,000 item limit** per Google Shared Drive ([10](https://globus.stanford.edu/cloud/drive.html))

These constraints necessitate alternative strategies for exascale workflows, such as combining Globus transfers with parallel filesystem mounts for in-situ processing ([3](https://globus-compute.readthedocs.io/en/stable/limits.html), [7](https://pmc.ncbi.nlm.nih.gov/articles/PMC4203657/)).

### Permission Management Challenges

Globus currently lacks native support for propagating custom permissions when transferring data to Google Drive. All uploaded files inherit parent folder permissions, complicating multi-user collaborations ([10](https://globus.stanford.edu/cloud/drive.html)).

### Task Lifetime Limitations

Tasks abandoned for over two weeks are automatically purged, requiring users to implement checkpointing for long-running analyses ([3](https://globus-compute.readthedocs.io/en/stable/limits.html)).

---

## Globus in Human Genomics: A Paradigm Shift

### End-to-End Workflow Automation

The Globus Genomics platform integrates with the Galaxy workflow engine to automate NGS analysis pipelines. Researchers at the University of Washington reduced exome processing time from 24 hours to 2.5 hours by combining Globus transfers with AWS spot instances ([7](https://pmc.ncbi.nlm.nih.gov/articles/PMC4203657/), [12](https://pubmed.ncbi.nlm.nih.gov/26925205/)). Key features include:

- Automated retrieval of raw FASTQ files from sequencing cores ([4](https://www.globus.org/user-stories/genomic-researchers-umichigan), [14](https://www.globus.org/sites/default/files/UCSC_iBi_case_study.pdf))
- Elastic provisioning of cloud resources for alignment (BWA) and variant calling (GATK) ([7](https://pmc.ncbi.nlm.nih.gov/articles/PMC4203657/), [12](https://pubmed.ncbi.nlm.nih.gov/26925205/))
- Secure delivery of VCF results to collaborators via encrypted guest collections ([8](https://ncifrederick.cancer.gov/about/theposter/content/using-globus-transfer-and-share-big-data), [13](https://www.globus.org/sites/default/files/case-study-dobyns-pediatric-brain-research-lab.pdf))

### Case Study: University of Michigan Advanced Genomics Core

#### Challenge

With sequencing output doubling every 20 months, the Core faced unsustainable data growth—6 TB per instrument run, plus 6.5 TB of processed data ([4](https://www.globus.org/user-stories/genomic-researchers-umichigan)). Traditional methods (FTP, physical drives) caused delays and risked PHI exposure.

#### Solution Implementation

1. **Push-Pull Architecture**:
    - Sequencers write directly to Globus-mounted network storage
    - Post-processed data pushed to researcher endpoints via automated transfers ([4](https://www.globus.org/user-stories/genomic-researchers-umichigan))
    - Email notifications trigger collaborator-initiated “pull” transfers ([4](https://www.globus.org/user-stories/genomic-researchers-umichigan))
2. **Tiered Archiving**:
    - Active datasets stored on high-performance Lustre filesystems
    - Cold data migrated to tape archives after 30-day retention period ([4](https://www.globus.org/user-stories/genomic-researchers-umichigan))
3. **Compliance Framework**:
    - Globus Auth integrates with institutional Active Directory for PHI access control
    - All transfers encrypted with AES-256, audit logs retained for HIPAA reporting ([8](https://ncifrederick.cancer.gov/about/theposter/content/using-globus-transfer-and-share-big-data), [13](https://www.globus.org/sites/default/files/case-study-dobyns-pediatric-brain-research-lab.pdf))

#### Outcomes

- 90% reduction in data delivery time (weeks → hours) ([4](https://www.globus.org/user-stories/genomic-researchers-umichigan))
- Zero unplanned PHI breaches over three years ([13](https://www.globus.org/sites/default/files/case-study-dobyns-pediatric-brain-research-lab.pdf))
- Enabled cross-border collaborations with Plant & Food Research New Zealand, transferring 3 TB genomic data in three hours ([11](https://www.aarnet.edu.au/data-without-borders-the-role-of-globus-in-international-genome-research))

---

## Operational Guide: Using Globus for Data Management

### Step-by-Step Workflow

1. **Endpoint Configuration**
    - Install Globus Connect Personal on local machines or use institutional endpoints (e.g., OSC’s /fs/scratch) ([6](https://www.osc.edu/resources/getting_started/howto/howto_use_globus_overview))
    - For cloud storage, authenticate via OAuth2 to services like Google Drive ([10](https://globus.stanford.edu/cloud/drive.html))
2. **Initiating Transfers**
    - Log in via institutional credentials (e.g., Ohio Supercomputer Center) ([6](https://www.osc.edu/resources/getting_started/howto/howto_use_globus_overview))
    - In the two-panel interface, select source (e.g., sequencer output directory) and destination (e.g., HPC cluster) ([6](https://www.osc.edu/resources/getting_started/howto/howto_use_globus_overview))
    - Enable checksum verification for integrity validation ([6](https://www.osc.edu/resources/getting_started/howto/howto_use_globus_overview))
3. **Sharing Data**
    - Right-click folder → “Share” → enter collaborator emails
    - Set permissions (read/write/administrator) ([6](https://www.osc.edu/resources/getting_started/howto/howto_use_globus_overview))
    - For PHI, restrict sharing to vetted identities via Globus Groups ([8](https://ncifrederick.cancer.gov/about/theposter/content/using-globus-transfer-and-share-big-data))
4. **Automating Pipelines**
    - Define recurring transfers using cron-like schedules
    - Integrate with HPC schedulers (Slurm, PBS) via REST API triggers ([7](https://pmc.ncbi.nlm.nih.gov/articles/PMC4203657/), [12](https://pubmed.ncbi.nlm.nih.gov/26925205/))

---

## Future Directions and Community Impact

Globus continues evolving through partnerships with initiatives like the Open Storage Network (OSN), which leverages its Auth and transfer services to create a 1.5 PB federated storage fabric ([2](https://www.globus.org/user-stories)). Emerging features include enhanced metadata search via GraphQL and integration with FAIR data principles for improved reproducibility.

For genomics specifically, ongoing developments focus on:

- **Containerised Workflows**: Packaging alignment/variant calling tools as Docker images executable via Globus Flows ([7](https://pmc.ncbi.nlm.nih.gov/articles/PMC4203657/), [12](https://pubmed.ncbi.nlm.nih.gov/26925205/))
- **AI/ML Integration**: Direct data streaming from Globus endpoints to TensorFlow/PyTorch clusters ([2](https://www.globus.org/user-stories), [9](https://cloud.google.com/customers/globus))
- **Global Metadata Catalogue**: Cross-institutional indexing of genomic variants with GA4GH standards ([13](https://www.globus.org/sites/default/files/case-study-dobyns-pediatric-brain-research-lab.pdf))

---

## Conclusion

Globus has redefined research data management by providing a unified platform that transcends institutional and disciplinary boundaries. Its impact on human genomics exemplifies how robust cyberinfrastructure can accelerate discovery—from enabling multi-continental collaborations to ensuring compliance with stringent data regulations. While limitations in task scalability and permission granularity persist, ongoing development and community-driven enhancements position Globus as an enduring cornerstone of modern scientific workflows. As data volumes continue their exponential growth, platforms like Globus will remain critical for realising the full potential of collaborative, data-intensive science.


 [1]: https://www.globus.org/what-we-do

 [2]: https://www.globus.org/user-stories

 [3]: https://globus-compute.readthedocs.io/en/stable/limits.html

 [4]: https://www.globus.org/user-stories/genomic-researchers-umichigan

 [5]: https://www.storyblok.com/cs/globus

 [6]: https://www.osc.edu/resources/getting_started/howto/howto_use_globus_overview

 [7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4203657/

 [8]: https://ncifrederick.cancer.gov/about/theposter/content/using-globus-transfer-and-share-big-data

 [9]: https://cloud.google.com/customers/globus

 [10]: https://globus.stanford.edu/cloud/drive.html

 [11]: https://www.aarnet.edu.au/data-without-borders-the-role-of-globus-in-international-genome-research

 [12]: https://pubmed.ncbi.nlm.nih.gov/26925205/

 [13]: https://www.globus.org/sites/default/files/case-study-dobyns-pediatric-brain-research-lab.pdf

 [14]: https://www.globus.org/sites/default/files/UCSC_iBi_case_study.pdf

 [15]: https://docs.nersc.gov/services/globus/

 [16]: https://www.globus.org
 [17]: https://docs.globus.org/api/search/limits/

 [18]: https://www.smartcommunications.com/wp-content/uploads/2015/12/Globus-and-Smart-Communications-Case-Study-V2.0.pdf

 [19]: https://service.tamu.edu/TDClient/36/Portal/KB/ArticleDet?ID=498

 [20]: https://rcc.uq.edu.au/article/2022/05/globus-web-app-makes-research-data-sharing-breeze

 [21]: https://docs.globus.org/api/flows/limits/

 [22]: https://www.psomagen.com/blog/the-promise-and-security-risks-of-using-cloud-based-informatics-solutions-for-human-genomic-data-analysis

 [23]: https://www.globusmedical.com/category/case-studies/

 [24]: https://www.researchgate.net/publication/257919843_High-performance_data_management_for_genome_sequencing_centers_using_Globus_Online_A_case_study

 [25]: https://www.australiangenomics.org.au/genomic-data-sharing-resources-showcased/

 [26]: https://www.researchgate.net/publication/268076509_A_case_study_for_cloud_based_high_throughput_analysis_of_NGS_data_using_the_Globus_Genomics_system

 [27]: http://ieeexplore.ieee.org/document/6404443

 [28]: https://dl.acm.org/doi/10.1145/3086567.3086570

 [29]: https://www.globusworld.org/files/2013/07-Sulakhe-Globus-Genomics.pdf
