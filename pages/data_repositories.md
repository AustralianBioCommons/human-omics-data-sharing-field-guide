---
title: Data repositories
contributors: [Marion Shadbolt]
---

<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.1/css/jquery.dataTables.css">
  
<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.13.1/js/jquery.dataTables.js"></script>


Researchers usually need to submit generated human genomics data to a central repository in order to obtain an accession that will allow publication {% cite plos_one_data_2019 cannon_repository_2021 cellpress_authors_2021 springer_nature_mandated_2022  %} and to meet funding requirements. Where to submit depends both on the data type and permissions related to data use.

Several tools exist to help a researcher decide where to submit their data:

* EBI submission helper tool: [https://www.ebi.ac.uk/submission/](https://www.ebi.ac.uk/submission/) 
* NCBI submission helper tool: [https://submit.ncbi.nlm.nih.gov/](https://submit.ncbi.nlm.nih.gov/) 
* DDBJ submission guide [https://www.ddbj.nig.ac.jp/documents/data-categories-e.html](https://www.ddbj.nig.ac.jp/documents/data-categories-e.html) 
* NIH list of Repositories for Sharing Scientific Data [https://sharing.nih.gov/data-management-and-sharing-policy/sharing-scientific-data/repositories-for-sharing-scientific-data](https://sharing.nih.gov/data-management-and-sharing-policy/sharing-scientific-data/repositories-for-sharing-scientific-data) 
* FAIRsharing - [https://fairsharing.org/](https://fairsharing.org/)


## Open Access ‘Omics Archives

The International Nucleotide Sequence Database Collaboration ([INSDC](https://www.insdc.org/)) is the major global provider of infrastructure to archive and provide open access to genetic sequencing data {% cite arita_international_2020 %}. 

Ownership of data remains with the original data providers, but the INSDC requires free and unrestricted access to all data records without use restrictions, licensing requirements or fees for use {% cite arita_international_2020 %}.

It is composed of three nodes:

* The European Nucleotide Archive (ENA)
* The DNA Data Bank of Japan (DDBJ)
* GenBank

Data submitted to each node must adhere to the INSDC data and metadata standard. This standard is implemented in a [set of XML schemas](https://github.com/enasequence/schema/tree/master/src/main/resources/uk/ac/ebi/ena/sra/schema). The [shared data model](https://ena-docs.readthedocs.io/en/latest/submit/general-guide/metadata.html) enables each archive to mirror all data submitted to any INSDC node. Archival accessions provided by each archive follow a consistent pattern with node specific lettering used based on where the data was originally submitted, ‘E’ for ENA, ‘D’ for DDBJ and ‘S’ for GenBank (see [ENA Accession numbers documentation](https://ena-docs.readthedocs.io/en/latest/submit/general-guide/accessions.html) for more information).

While not part of the INSDC, the China National Center for Bioinformation (CNCB) and its National Genomics Data Center (NGDC) provide archives that follow the same themes and data standards as those part of the INSDC {% cite cncb-ngdc_genome_2019 %}. They also mirror the metadata of data within INSDC archives, enabling global search across all four major genetic sequencing archives.

Table 1. Databases of the three INSDC nodes (adapted from {% cite arita_international_2020 %} and the NGDC CNCB. INSDC resources coloured in blue


<table id="table_id">
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

### Data repositories summary table

<table id="table_id2">
 <thead>
  <tr>
   <th style="text-align:left;"> resource name </th>
   <th style="text-align:left;"> Institute </th>
   <th style="text-align:left;"> data type </th>
   <th style="text-align:left;"> Linked archives </th>
   <th style="text-align:left;"> access type </th>
   <th style="text-align:left;"> submission method </th>
   <th style="text-align:left;"> metadata standard </th>
   <th style="text-align:left;"> data formats </th>
   <th style="text-align:left;"> publication </th>
   <th style="text-align:left;"> training </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ebi.ac.uk/ena/browser/&quot; target=&quot;_blank&quot;&gt;European Nucleotide Archive
(ENA)&lt;/a&gt; </td>
   <td style="text-align:left;"> EMBL-EBI </td>
   <td style="text-align:left;"> raw genomic reads
Genome assemblies </td>
   <td style="text-align:left;"> BioSamples </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> interactive
webin CLI
programmatic API </td>
   <td style="text-align:left;"> INSDC metadata model, minimal experimental &amp; sequencing information </td>
   <td style="text-align:left;"> CRAM
BAM
FASTQ </td>
   <td style="text-align:left;"> &lt;a href=&quot;https://doi.org/10.1093/nar/gkab1051&quot; target=&quot;_blank&quot;&gt;&lt;i class=&quot;fa-solid fa-book&quot;&gt;&lt;/i&gt; Cummins et al. 2022&lt;/a&gt; </td>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ebi.ac.uk/training/online/courses/ena-quick-tour/&quot; target=&quot;_blank&quot;&gt;&lt;i class=&quot;fa-solid fa-chalkboard-user&quot;&gt;&lt;/i&gt;&lt;/a&gt; </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://ega-archive.org/&quot; target=&quot;_blank&quot;&gt;European Genome-Phenome Archive
(EGA)&lt;/a&gt; </td>
   <td style="text-align:left;"> EMBL-EBI </td>
   <td style="text-align:left;"> sensitive human data
raw genomic reads
variant information </td>
   <td style="text-align:left;"> BioSamples </td>
   <td style="text-align:left;"> managed </td>
   <td style="text-align:left;"> interactive
programmatic API </td>
   <td style="text-align:left;"> INSDC metadata model plus DAC &amp; policy, minimal experimental &amp; sequencing information </td>
   <td style="text-align:left;"> CRAM
BAM
FASTQ
VCF </td>
   <td style="text-align:left;"> &lt;a href=&quot;http://dx.doi.org/10.1093/nar/gkab1059&quot; target=&quot;_blank&quot;&gt;&lt;i class=&quot;fa-solid fa-book&quot;&gt;&lt;/i&gt; Freeberg et al. 2022&lt;/a&gt; </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ebi.ac.uk/arrayexpress/&quot; target=&quot;_blank&quot;&gt;ArrayExpress&lt;/a&gt; </td>
   <td style="text-align:left;"> EMBL-EBI </td>
   <td style="text-align:left;"> raw transcriptomic reads (mRNA/miRNA)
Microarray
SNP genotyping
ChIP
Comparative genomic hybridisation
count matrix
(more examples) </td>
   <td style="text-align:left;"> ENA
BioStudies
BioSamples </td>
   <td style="text-align:left;"> open
can link to EGA accessions </td>
   <td style="text-align:left;"> interactive </td>
   <td style="text-align:left;"> demographic, phenotypic &amp; experimental information
human curation to check correctness </td>
   <td style="text-align:left;"> FASTQ
BAM
MTX </td>
   <td style="text-align:left;"> Parkinson et al. 2007 </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ncbi.nlm.nih.gov/sra&quot; target=&quot;_blank&quot;&gt;Short Read Archive
(SRA)&lt;/a&gt; </td>
   <td style="text-align:left;"> NCBI </td>
   <td style="text-align:left;"> raw genomic reads </td>
   <td style="text-align:left;"> BioProject
BioSample </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> minimal experimental &amp; sequencing information </td>
   <td style="text-align:left;"> CRAM
BAM
FASTQ </td>
   <td style="text-align:left;"> Katz et al. 2022 </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ncbi.nlm.nih.gov/geo/&quot; target=&quot;_blank&quot;&gt;Gene Expression Omnibus
(GEO)&lt;/a&gt; </td>
   <td style="text-align:left;"> NCBI </td>
   <td style="text-align:left;"> RNA profiling
small RNA profiling
ChIP-Seq
HiC-Seq
methyl-seq
raw transcriptomic
count matrix </td>
   <td style="text-align:left;"> SRA 
BioProject BioSample </td>
   <td style="text-align:left;"> Open but can choose to include summary level data e.g. matrix </td>
   <td style="text-align:left;"> interactive (spreadsheet)
programmatic (XML) </td>
   <td style="text-align:left;"> MIAME, MINISEQ-E, SOFT </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> Clough and Barrett 2016 </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ncbi.nlm.nih.gov/gap/&quot; target=&quot;_blank&quot;&gt;database of Genotypes and Phenotypes (dbGaP)&lt;/a&gt; </td>
   <td style="text-align:left;"> NCBI </td>
   <td style="text-align:left;"> raw genomic
raw transcriptomic
variant information </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> Managed by central DAC </td>
   <td style="text-align:left;"> Needs to be NIH funded or go through approvals process </td>
   <td style="text-align:left;"> INSDC metadata model? </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> Tryka et al. 2014 </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ddbj.nig.ac.jp/dra/index-e.html&quot; target=&quot;_blank&quot;&gt;DDBJ Sequence Read Archive
(DRA)&lt;/a&gt; </td>
   <td style="text-align:left;"> DDBJ </td>
   <td style="text-align:left;"> raw genomic </td>
   <td style="text-align:left;"> BioProject
BioSample </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> INSDC metadata model </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> Okido et al. 2022 </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ddbj.nig.ac.jp/gea/index-e.html&quot; target=&quot;_blank&quot;&gt;Genomic Expression Archive (GEA)&lt;/a&gt; </td>
   <td style="text-align:left;"> DDBJ </td>
   <td style="text-align:left;"> mRNA profiling - RNA-seq
small RNA profiling - miRNA-seq
ChIP-Seq
HiC-seq
methyl-seq, bisulfite-seq
SNP microarray genotyping
count matrix </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> ? </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> Okido et al. 2022 </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://humandbs.biosciencedbc.jp/en/data-use/all-researches&quot; target=&quot;_blank&quot;&gt;Japanese Genome-Phenome Archive (JGA)&lt;/a&gt; </td>
   <td style="text-align:left;"> DDBJ </td>
   <td style="text-align:left;"> sensitive human data
raw genomic reads
variant information </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> Managed by central DAC </td>
   <td style="text-align:left;"> Needs to be approved by JST-NBDC, then submission portal </td>
   <td style="text-align:left;"> Extended INSDC metadata model
JGA schemas </td>
   <td style="text-align:left;"> BAM
FASTQ
SFF
VCF
TXT </td>
   <td style="text-align:left;"> Okido et al. 2022 </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://ngdc.cncb.ac.cn/gsa/&quot; target=&quot;_blank&quot;&gt;Genome Sequence Archive (GSA)&lt;/a&gt; </td>
   <td style="text-align:left;"> CNCB, NGDC </td>
   <td style="text-align:left;"> raw sequence </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> Mirrors INSDC even though not a part of it
Data standards </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> CNCB-NGDC Members and Partners 2022 </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://bigd.big.ac.cn/gsa-human&quot; target=&quot;_blank&quot;&gt;GSA-Human&lt;/a&gt; </td>
   <td style="text-align:left;"> CNCB, NGDC </td>
   <td style="text-align:left;"> raw sequence </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> managed </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> ? </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> CNCB-NGDC Members and Partners 2022 </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ebi.ac.uk/biosamples/&quot; target=&quot;_blank&quot;&gt;BioSamples (EBI)&lt;/a&gt; </td>
   <td style="text-align:left;"> EBI </td>
   <td style="text-align:left;"> Sample metadata </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> open
(but can be set private) </td>
   <td style="text-align:left;"> API </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> Courtot et al. 2019 </td>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ebi.ac.uk/training/online/courses/biosamples-quick-tour/&quot; target=&quot;_blank&quot;&gt;&lt;i class=&quot;fa-solid fa-chalkboard-user&quot;&gt;&lt;/i&gt;&lt;/a&gt; </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ebi.ac.uk/biostudies/&quot; target=&quot;_blank&quot;&gt;BioStudies (EBI)&lt;/a&gt; </td>
   <td style="text-align:left;"> EBI </td>
   <td style="text-align:left;"> Study/project metadata </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> Web interface or API </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> Sarkans et al. 2018 </td>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ebi.ac.uk/training/events/biostudies-database-aggregating-all-outputs-life-sciences-study/&quot; target=&quot;_blank&quot;&gt;&lt;i class=&quot;fa-solid fa-chalkboard-user&quot;&gt;&lt;/i&gt;&lt;/a&gt; </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ncbi.nlm.nih.gov/biosample/&quot; target=&quot;_blank&quot;&gt;BioSamples (NCBI)&lt;/a&gt; </td>
   <td style="text-align:left;"> NCBI </td>
   <td style="text-align:left;"> Sample metadata </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> Don’t generally encourage stand alone submission </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ncbi.nlm.nih.gov/bioproject/&quot; target=&quot;_blank&quot;&gt;BioProject (NCBI)&lt;/a&gt; </td>
   <td style="text-align:left;"> NCBI </td>
   <td style="text-align:left;"> Study/project metadata </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> Don’t generally encourage stand alone submission </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://ngdc.cncb.ac.cn/bioproject/&quot; target=&quot;_blank&quot;&gt;BioProject (CNCB)&lt;/a&gt; </td>
   <td style="text-align:left;"> CNCB </td>
   <td style="text-align:left;"> Study/project metadata </td>
   <td style="text-align:left;"> GSA
BioSample </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> web interface </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> CNCB-NGDC Members and Partners 2022 </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://ngdc.cncb.ac.cn/biosample/&quot; target=&quot;_blank&quot;&gt;BioSample (CNCB)&lt;/a&gt; </td>
   <td style="text-align:left;"> CNCB </td>
   <td style="text-align:left;"> Sample metadata </td>
   <td style="text-align:left;"> GSA
BioProject </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> web interface </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> CNCB-NGDC Members and Partners 2022 </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ddbj.nig.ac.jp/biosample/index-e.html&quot; target=&quot;_blank&quot;&gt;BioSamples (DDBJ)&lt;/a&gt; </td>
   <td style="text-align:left;"> DDBJ </td>
   <td style="text-align:left;"> Sample metadata </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> Don’t generally encourage stand alone submission </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ddbj.nig.ac.jp/bioproject/index-e.html&quot; target=&quot;_blank&quot;&gt;BioProject (DDBJ)&lt;/a&gt; </td>
   <td style="text-align:left;"> DDBJ </td>
   <td style="text-align:left;"> Study/project metadata </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> Don’t generally encourage stand alone submission </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ddbj.nig.ac.jp/metabobank/index-e.html&quot; target=&quot;_blank&quot;&gt;Metabobank&lt;/a&gt; </td>
   <td style="text-align:left;"> DDBJ </td>
   <td style="text-align:left;"> metabolomics </td>
   <td style="text-align:left;"> BioSample
BioProject </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> MAGE-TAB </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> Okido et al. 2022 </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ebi.ac.uk/metabolights/&quot; target=&quot;_blank&quot;&gt;MetaboLights&lt;/a&gt; </td>
   <td style="text-align:left;"> EBI </td>
   <td style="text-align:left;"> metabolomics </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> web interface </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> Haug et al. 2020 </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ebi.ac.uk/pride/&quot; target=&quot;_blank&quot;&gt;PRIDE&lt;/a&gt; </td>
   <td style="text-align:left;"> EBI </td>
   <td style="text-align:left;"> Proteomics </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> Perez-Riverol et al. 2022 </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://jpostdb.org/&quot; target=&quot;_blank&quot;&gt;JPOST&lt;/a&gt; </td>
   <td style="text-align:left;"> DDBJ </td>
   <td style="text-align:left;"> Proteomics </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ebi.ac.uk/bioimage-archive/&quot; target=&quot;_blank&quot;&gt;BioImage Archive&lt;/a&gt; </td>
   <td style="text-align:left;"> EBI </td>
   <td style="text-align:left;"> Biological images </td>
   <td style="text-align:left;"> BioStudies </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> Hartley et al. 2022 </td>
   <td style="text-align:left;">  </td>
  </tr>
  <tr>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ebi.ac.uk/empiar/&quot; target=&quot;_blank&quot;&gt;EMPIAR&lt;/a&gt; </td>
   <td style="text-align:left;"> EBI </td>
   <td style="text-align:left;"> Electron microscopy images </td>
   <td style="text-align:left;"> BioStudies </td>
   <td style="text-align:left;"> open </td>
   <td style="text-align:left;"> web interface
python automated script </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> &lt;a href=&quot;https://doi.org/10.1101/2022.10.04.510785&quot; target=&quot;_blank&quot;&gt;&lt;i class=&quot;fa-solid fa-book&quot;&gt;&lt;/i&gt; NA&lt;/a&gt; </td>
   <td style="text-align:left;"> &lt;a href=&quot;https://www.ebi.ac.uk/training/online/courses/empiar-quick-tour/&quot; target=&quot;_blank&quot;&gt;&lt;i class=&quot;fa-solid fa-chalkboard-user&quot;&gt;&lt;/i&gt;&lt;/a&gt; </td>
  </tr>
</tbody>
</table>

<script>
    $(document).ready( function () {
        $('#table_id2').DataTable();
    } );
</script>

For full-size interactive table see here: [https://marion-biocommons.shinyapps.io/field_guide_repo_table/](https://marion-biocommons.shinyapps.io/field_guide_repo_table/)
<iframe height="800" width="100%" frameborder="no" src="https://marion-biocommons.shinyapps.io/field_guide_repo_table/"> </iframe>

## References

{% bibliography --cited %}