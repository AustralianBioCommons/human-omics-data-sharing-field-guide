---
title: Data repositories
contributors: [Marion Shadbolt]
---

Researchers usually need to submit generated human genomics data to a central repository in order to obtain an accession that will allow publication [(Springer Nature n.d.; PLOS ONE 2019; CellPress 2021; Cannon et al. 2021)](https://www.zotero.org/google-docs/?74yQBN)  and to meet funding requirements. Where to submit depends both on the data type and permissions related to data use.

Several tools exist to help a researcher decide where to submit their data:

* EBI submission helper tool: [https://www.ebi.ac.uk/submission/](https://www.ebi.ac.uk/submission/) 
* NCBI submission helper tool: [https://submit.ncbi.nlm.nih.gov/](https://submit.ncbi.nlm.nih.gov/) 
* DDBJ submission guide [https://www.ddbj.nig.ac.jp/documents/data-categories-e.html](https://www.ddbj.nig.ac.jp/documents/data-categories-e.html) 
* NIH list of Repositories for Sharing Scientific Data [https://sharing.nih.gov/data-management-and-sharing-policy/sharing-scientific-data/repositories-for-sharing-scientific-data](https://sharing.nih.gov/data-management-and-sharing-policy/sharing-scientific-data/repositories-for-sharing-scientific-data) 
* FAIRsharing - [https://fairsharing.org/](https://fairsharing.org/)


## Open Access ‘Omics Archives

The International Nucleotide Sequence Database Collaboration ([INSDC](https://www.insdc.org/)) is the major global provider of infrastructure to archive and provide open access to genetic sequencing data [(Arita, Karsch-Mizrachi, and Cochrane 2020)](https://www.zotero.org/google-docs/?gl5leO). 

Ownership of data remains with the original data providers, but the INSDC requires free and unrestricted access to all data records without use restrictions, licensing requirements or fees for use [(Arita, Karsch-Mizrachi, and Cochrane 2020)](https://www.zotero.org/google-docs/?k55goP).

It is composed of three nodes:

* The European Nucleotide Archive (ENA)
* The DNA Data Bank of Japan (DDBJ)
* GenBank

Data submitted to each node must adhere to the INSDC data and metadata standard. This standard is implemented in a [set of XML schemas](https://github.com/enasequence/schema/tree/master/src/main/resources/uk/ac/ebi/ena/sra/schema). The [shared data model](https://ena-docs.readthedocs.io/en/latest/submit/general-guide/metadata.html) enables each archive to mirror all data submitted to any INSDC node. Archival accessions provided by each archive follow a consistent pattern with node specific lettering used based on where the data was originally submitted, ‘E’ for ENA, ‘D’ for DDBJ and ‘S’ for GenBank (see [ENA Accession numbers documentation](https://ena-docs.readthedocs.io/en/latest/submit/general-guide/accessions.html) for more information).

While not part of the INSDC, the China National Center for Bioinformation (CNCB) and its National Genomics Data Center (NGDC) provide archives that follow the same themes and data standards as those part of the INSDC [(CNCB-NGDC Members and Partners 2022; Wang et al. 2017)](https://www.zotero.org/google-docs/?ODfGZr). They also mirror the metadata of data within INSDC archives, enabling global search across all four major genetic sequencing archives.

Table 1. Databases of the three INSDC nodes (adapted from [(Arita, Karsch-Mizrachi, and Cochrane 2020)](https://www.zotero.org/google-docs/?vtIySk) and the NGDC CNCB. INSDC resources coloured in blue


<table>
  <tr>
   <td><strong>Institute</strong>
   </td>
   <td><strong>Annotated sequences</strong>
   </td>
   <td><strong>NGS Reads</strong>
   </td>
   <td><strong>Project Metadata</strong>
   </td>
   <td><strong>Sample Information</strong>
   </td>
   <td><strong>Functional Genomics</strong>
   </td>
   <td><strong>Processed functional genomics</strong>
   </td>
   <td><strong>Human Genomes (controlled)</strong>
   </td>
   <td><strong>Metabolomics</strong>
   </td>
   <td><strong>Proteomics</strong>
   </td>
  </tr>
  <tr>
   <td>DDBJ
   </td>
   <td style="background-color:#5ac3b1">DDBJ
   </td>
   <td style="background-color:#5ac3b1">SRA
   </td>
   <td style="background-color:#5ac3b1">BioProject
   </td>
   <td style="background-color:#5ac3b1" >BioSample
   </td>
   <td>GEA
   </td>
   <td>
   </td>
   <td>JGA
   </td>
   <td>Metabobank
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>EMBL-EBI
   </td>
   <td colspan="2" style="background-color:#5ac3b1;text-align:center" >ENA
   </td>
   <td>BioStudies
   </td>
   <td style="background-color:#5ac3b1">BioSamples
   </td>
   <td>ArrayExpress
   </td>
   <td>Expression Atlas
   </td>
   <td>EGA
   </td>
   <td>Metabolights
   </td>
   <td>PRIDE
   </td>
  </tr>
  <tr>
   <td>NCBI
   </td>
   <td style="background-color:#5ac3b1">GenBank
   </td>
   <td style="background-color:#5ac3b1">SRA
   </td>
   <td style="background-color:#5ac3b1">BioProject
   </td>
   <td style="background-color:#5ac3b1">BioSample
   </td>
   <td>GEO
   </td>
   <td>
   </td>
   <td>dbGaP
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>CNCB-NGDC
   </td>
   <td>GWH
   </td>
   <td>GSA
   </td>
   <td>BioProject
   </td>
   <td>BioSample
   </td>
   <td>
   </td>
   <td>GEN
   </td>
   <td>GSA-Human
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
</table>



## Controlled Access data repositories

When dealing with human data, it is often necessary to archive data in a controlled access repository in order to comply with consent, ethics and legal regulations. Controlled access means that anyone who wants to use the data, must apply for access to the data and agree to use the data in accordance with a data use policy. It varies whether that repository has its own Data Access Committee (DAC) that decides whether a data access request (DAR) complies with the policy and access is granted, or whether the data remains under the control of a dataset specific DAC.

Within Australia, the need to keep data onshore and the challenges involved in archiving in major international repositories means the majority of Australian human genomics research data remains siloed and un-FAIR in unsearchable institutional repositories. However, of the major controlled access archives, the European Genome-Phenome Archive (EGA) is the most used archive by Australian researchers, as it is the only one available to researchers without the need for specific funding arrangements or explicit approval.

## Data repositories explained

Choose a data repository below to learn more about it:

{% include section-navigation-tiles.html type="data_repositories" affiliations=true search=true %}

For full table see here: [https://marion-biocommons.shinyapps.io/field_guide_repo_table/](https://marion-biocommons.shinyapps.io/field_guide_repo_table/)
<iframe height="400" width="100%" frameborder="no" src="https://marion-biocommons.shinyapps.io/field_guide_repo_table/"> </iframe>
