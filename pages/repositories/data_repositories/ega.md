---
title: EGA
contributors: [Marion Shadbolt]
affiliations: [ELIXIR Europe]
---

The European Genome-Phenome Archive (EGA) is a controlled access data repository for sensitive human data. The repository is managed by EMBL-EBI (UK) and the Centre for Genomic Regulation (CRG) (Spain). Submission is open to anyone and data access is controlled per dataset by a user submitted data access policy and user defined data access committee. A single data access committee and policy may be used for a single dataset or may be reused for multiple datasets.


# EGA Submission process

The EGA submission process can be challenging to those unfamiliar to it, so the following sections provide an overview as well as some tips and tricks that may help you along the way. The first step is to gain an EGA submission account, which can be done by completing the [submission account form](https://ega-archive.org/submission-form.php).


## EGA Metadata

The metadata files that must be submitted to EGA follow the same INSDC schemas, with the addition of policy, dataset and dac objects. These allow for the administration aspects related to controlled access of data and allow for finer grained access to datasets within a study. All information submitted in these XML files is considered public access and can be queried via the EGA API once the study is available in the platform. The required attributes that must be included about each sample are:



* Donor ID - anonymised individual identifier
* Biological sex (referred to as gender)
* Phenotype - preferably ontologised using [EFO](https://www.ebi.ac.uk/ols/ontologies/efo)

Submitters can add as many other attributes as they like, but this information will be openly accessible when the study is submitted. It is also possible to first submit attributes to the BioSamples database first and use the obtained accessions in your EGA submission to link to BioSamples. These would also only be for public metadata. 

Due to limited required attributes, it is often necessary to make more comprehensive clinical, phenotypic and demographic metadata available alongside the data files. If this metadata is subject to controlled access, the information can be attached to the submission as Analysis (phenotype) files. These do not follow any kind of strict standard or format, however the use of the [GA4GH phenopacket](https://phenopacket-schema.readthedocs.io/en/latest/) is an emerging standard for characterising this type of information. README files can also be incorporated to provide an explanation of the phenotype or other analysis files.

Submitting to the EGA can be done via its submission interface or through submitting XMLs or JSONs via their REST API. The submission interface is useful for a user-friendly experience when submitting metadata for objects where there are relatively few objects of that type. We recommend using it for objects such as:



* Study
* DAC
* Policy
* Experiment 

For objects with a high cardinality, such as Samples, Runs and Analyses, using the CSV templates that are available through the submission portal or creating XML documents and submitting via API is more efficient.

However, it is possible to create a fully automated submission process that contains all metadata required by creating XML documents.

NOTE: When preparing a submission, it is important to validate and check all the details because editing after submission is not possible without going through the helpdesk. Submission to the test instance of the EGA is recommended before making your final submission.

NOTE: The alias field that is set for each object is not strictly required, if not specified one will be provided. BUT the alias is what you used to link between the different objects so it is useful to set to names that you can recognise to facilitate the linking that is required in your submission. Aliases must be unique across all items within a submission account.

NOTE: All data files that are referred to by ‘run’ or ‘analysis’ objects must be placed in the submission box and indexed by the system before it will allow submission of those object XMLs.

NOTE: For objects that are linked by their accessions i.e. policy, dataset, the objects they refer to must be submitted and assigned accessions by the EGA before they can be linked.

Table: Detailed information about ega objects and tips on creating XMLs for each object. Adapted from [(Band 2019; EGA n.d.)](https://www.zotero.org/google-docs/?5otJgj)


<table>
  <tr>
   <td><strong>Metadata object</strong>
   </td>
   <td><strong>definition</strong>
   </td>
   <td><strong>Important fields</strong>
   </td>
   <td><strong>schema</strong>
   </td>
   <td><strong>EGA Example</strong>
   </td>
  </tr>
  <tr>
   <td>submission
   </td>
   <td>An XML that points to all the other xml files that will be included as part of a submission
   </td>
   <td>At least one ACTION in the ACTIONS list
   </td>
   <td><a href="https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.submission.xsd">sra.submission.xsd</a>
   </td>
   <td><a href="https://ega-archive.org/files/Submission.xml">Submission.xml</a>
   </td>
  </tr>
  <tr>
   <td>study
   </td>
   <td>Describes information about the study, such as the title and abstract, and is linked to 1 or more datasets
   </td>
   <td>STUDY_TITLE
<p>
STUDY_TYPE
<p>
alias - useful to refer to in later objects
   </td>
   <td><a href="https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.study.xsd">sra.study.xsd</a>
   </td>
   <td><a href="https://ega-archive.org/files/Study.xml">Study.xml</a>
   </td>
  </tr>
  <tr>
   <td>sample
   </td>
   <td>Describes the set of samples to be submitted
   </td>
   <td>TAXON_ID
<p>
SAMPLE_ATTRIBUTES
<ul>

<li>SAMPLE_ATTRIBUTE 
<ul>
 
<li>TAG: subject_id
 
<li>VALUE: a unique identifier
</li> 
</ul>

<li>SAMPLE_ATTRIBUTE 
<ul>
 
<li>TAG: gender
 
<li>VALUE: male/female/unknown
</li> 
</ul>

<li>SAMPLE_ATTRIBUTE

<li>TAG: phenotype

<li>VALUE: EFO Term

<li>UNITS: Experimental Ontology Factor accession

<li>SAMPLE_ATTRIBUTE

<li>TAG: Any other attribute that is useful to provide and can be released open access

<li>VALUE: the value for the tag

<p>
alias - useful to refer to in later objects
</li>
</ul>
   </td>
   <td><a href="https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.sample.xsd">sra.sample.xsd</a>
   </td>
   <td><a href="https://ega-archive.org/files/Sample.xml">Sample.xml</a>
   </td>
  </tr>
  <tr>
   <td>experiment
   </td>
   <td>Describes the sequencing experiment such as platform, model, library prep information. Typically it would collect all information that would need to be analysed together, e.g. all sequencing runs from a single library from a single sample
   </td>
   <td>LIBRARY_STRATEGY
<p>
LIBRARY_SOURCE
<p>
LIBRARY_SELECTION
<p>
LIBRARY_LAYOUT
<p>
LIBRARY_CONSTRUCTION_PROTOCOL
<p>
alias - useful to refer to in later objects
<p>
<strong>Links To Other Objects</strong>:
<p>
STUDY_REF - study alias of the study it belongs to
<p>
SAMPLE_DESCRIPTOR - sample alias of sample object the experiment was performed on
   </td>
   <td><a href="https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.experiment.xsd">sra.experiment.xsd</a>
   </td>
   <td><a href="https://ega-archive.org/files/Experiment_illumina_paired.xml">Experiment_illumina_paired.xml</a>
   </td>
  </tr>
  <tr>
   <td>run
   </td>
   <td>Each run contains a single data file, files that belong together get grouped under an experiment
   </td>
   <td>FILES
<ul>

<li>FILE

<li>filename

<li>filetype

<li>checksum_method

<li>checksum

<li>unencrypted_checksum

<p>
<strong>Links To Other Objects</strong>:
<p>
EXPERIMENT_REF
</li>
</ul>
   </td>
   <td><a href="https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.run.xsd">sra.run.xsd</a>
   </td>
   <td><a href="https://ega-archive.org/files/Run.xml">Run.xml</a>
   </td>
  </tr>
  <tr>
   <td>analysis - BAM/CRAM
   </td>
   <td>Metadata that describes a bam or cram file. Ideally should capture information about the reference assembly used. Can also link related files such as a readme, index and/or phenotype file.
   </td>
   <td>ANALYSIS_TYPE
<ul>

<li>REFERENCE_ALIGNMENT 
<ul>
 
<li>ASSEMBLY  
<ul>
  
<li>refname (INSDC assembly name)
</li>  
</ul>
</li>  
</ul>

<li>SEQUENCE  
<ul>
 
<li>accession

<p>
FILES
<ul>

<li>FILE

<li>filename

<li>filetype

<li>checksum_method

<li>checksum

<li>unencrypted_checksum

<p>
<strong>Links to Other Objects:</strong>
<p>
STUDY_REF: study alias
<p>
SAMPLE_REF: sample alias, Can specify multiple times if contains analysis of multiple samples
<p>
If raw files also being submitted:
<p>
EXPERIMENT_REF: experiment alias
<p>
RUN_REF: run alias
</li>
</ul>
</li>
</ul>
</li>
</ul>
   </td>
   <td><a href="https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.analysis.xsd">sra.analysis.xsd</a>
   </td>
   <td><a href="https://ega-archive.org/files/Analysis_BAM.xml">Analysis_BAM.xml</a>
   </td>
  </tr>
  <tr>
   <td>analysis - VCF
   </td>
   <td>One vcf file per analysis object and should be linked to submitted samples. 
   </td>
   <td>ANALYSIS_TYPE
<ul>

<li>SEQUENCE_VARIATION 
<ul>
 
<li>ASSEMBLY  
<ul>
  
<li>refname (INSDC assembly name)
</li>  
</ul>
</li>  
</ul>

<li>EXPERIMENT_TYPE

<p>
FILES
<ul>

<li>FILE

<li>filename

<li>filetype

<li>checksum_method

<li>checksum

<li>unencrypted_checksum

<p>
<strong>Links to Other Objects:</strong>
<p>
STUDY_REF: study alias
<p>
SAMPLE_REF: sample alias, Can specify multiple times if contains analysis of multiple samples
</li>
</ul>
</li>
</ul>
   </td>
   <td><a href="https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.analysis.xsd">sra.analysis.xsd</a>
   </td>
   <td><a href="https://ega-archive.org/files/Analysis_VCF.xml">Analysis_VCF.xml</a>
   </td>
  </tr>
  <tr>
   <td>analysis - phenotype
   </td>
   <td>One phenotype per analysis object and should be linked to submitted samples. E.g. phenopacket file
   </td>
   <td>ANALYSIS_TYPE
<ul>

<li>SAMPLE_PHENOTYPE

<p>
FILES
<ul>

<li>FILE

<li>filename

<li>filetype

<li>checksum_method

<li>checksum

<li>unencrypted_checksum

<p>
<strong>Links to Other Objects:</strong>
<p>
STUDY_REF: study alias
<p>
SAMPLE_REF: sample alias, Can specify multiple times if contains analysis of multiple samples
</li>
</ul>
</li>
</ul>
   </td>
   <td><a href="https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.analysis.xsd">sra.analysis.xsd</a>
   </td>
   <td><a href="https://ega-archive.org/files/Analysis_phenotypes_0.xml">Analysis_phenotypes_0.xml</a>
   </td>
  </tr>
  <tr>
   <td>dac
   </td>
   <td>Contains the contact information of all members of the data access committee that makes decisions on who can access the data. Can be used for many different policies and datasets
   </td>
   <td>TITLE
<p>
CONTACT : at least one
   </td>
   <td><a href="https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/EGA.dac.xsd">EGA.dac.xsd</a>
   </td>
   <td><a href="https://ega-archive.org/files/DAC.xml">DAC.xml</a>
   </td>
  </tr>
  <tr>
   <td>policy
   </td>
   <td>Describes the data access agreement and links to the data access committee (DAC) that administers it.
   </td>
   <td>TITLE
<p>
POLICY_TEXT
<p>
POLICY_LINKS
<ul>

<li>POLICY_LINK 
<ul>
 
<li>URL_LINK: to link to external web pages if applicable

<p>
<strong>Links to Other Objects:</strong>
<p>
DAC_REF
<ul>

<li>accession
</li>
</ul>
</li>
</ul>
</li>
</ul>
   </td>
   <td><a href="https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/EGA.policy.xsd">EGA.policy.xsd</a>
   </td>
   <td><a href="https://ega-archive.org/files/Policy_0.xml">Policy_0.xml</a>
   </td>
  </tr>
  <tr>
   <td>dataset
   </td>
   <td>Describes a set of files that are logically grouped together and represent a unit to which would be provided access. Must link to the policy that defines how it can be used and the runs and/or analyses that describe the data set files. Examples provided by the EGA include: cases and controls, or different phenotypes.
   </td>
   <td>DATASET_TYPE
<p>
<strong>Links to Other Objects:</strong>
<p>
RUN_REF 
<ul>

<li>accession : repeated for all runs in the dataset

<p>
ANALYSIS_REF
<ul>

<li>accession : repeated for all runs in the dataset

<p>
POLICY_REF
<ul>

<li>accession EGAP

<li>refcenter
</li>
</ul>
</li>
</ul>
</li>
</ul>
   </td>
   <td><a href="https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/EGA.dataset.xsd">EGA.dataset.xsd</a>
   </td>
   <td><a href="https://ega-archive.org/files/Dataset_0.xml">Dataset_0.xml</a>
   </td>
  </tr>
</table>




<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![EGA Metadata Model schematic](images/infrastructures/EGA-Metadata-Model.png "EGA Metadata Model schematic")

Figure 1. Graphical representation of EGA Metadata Model to represent a sequencing experiment with some recommended fields specified based on [EGA example xmls](https://ega-archive.org/submission/sequence/programmatic_submissions/prepare_xml). For comprehensive detail of available fields, see the [XML schemas](https://github.com/enasequence/schema/tree/master/src/main/resources/uk/ac/ebi/ena/sra/schema).


### Resources:

Set of example XMLs created by EGA: [https://ega-archive.org/submission/sequence/programmatic_submissions/prepare_xml](https://ega-archive.org/submission/sequence/programmatic_submissions/prepare_xml) 

A somewhat tongue-in-cheek but potentially useful 4 part run through of one user’s experience with how to submit to EGA, mostly programmatically:

[https://gavinband.github.io/bioinformatics/data/2019/05/01/Me_versus_the_European_Genome_Phenome_Archive.html](https://gavinband.github.io/bioinformatics/data/2019/05/01/Me_versus_the_European_Genome_Phenome_Archive.html) 

Example of automated data flow to EGA from QIMRB. This transforms their internally stored metadata into the XMLs required for an EGA submission: [https://github.com/delocalizer/ega_metadata](https://github.com/delocalizer/ega_metadata) 


## EGA Data Files

All files that will be referenced from the Run or Analysis objects must be encrypted before they are transferred to the EGA servers. Encryption is done by using the [EGAcryptor](https://ega-archive.org/submission/tools/egacryptor) software and you need the [public key](https://ega-archive.org/files/submission_2020_public.gpg.asc) provided by EGA. The files must be checksummed both before and after encryption, and the checksums as well as the method used must be incorporated into the metadata files. File can be transferred using Aspera (faster) or FTP. They don’t generally allow for more than 10TB of data to be uploaded to a submission box at a time, but this can be negotiated with the helpdesk if a higher limit is needed.

Note: Ensure that any potentially identifiable information is take out of any data files, such as information in BAM headers

Note: Once files are uploaded, it takes time for them to be indexed and recognised as present within the submission box. Submission of file-related metadata won’t be possible until the EGA system recognises the files are in the submission box.

Note: File names should be kept in a simple flat structure when uploading and ideally shouldn’t change names as changes in names may take up to 24 hours to change.

Note: There may be limits on the bandwidth of data that can be uploaded to a submission box but this is unknown. Be prepared for timeouts, dropouts and don’t over burden with lots of parallelisation. 

Note: The transfer process can be very slow from Australia->Europe

Note: It is expected that you will complete your submission, including metadata from the entire experiment, within 60 days of uploading files to a submission box, and files will be deleted after 90 days. So don’t upload files unless you are ready to complete your submission. 


### Resources:

EGA file upload documentation: [https://ega-archive.org/submission/tools/ftp-aspera](https://ega-archive.org/submission/tools/ftp-aspera) 

Automated encryption and submission of data files from an Amazon S3 bucket to EGA submission box using Aspera, created by UMCCR: [https://github.com/umccr/ega-submit](https://github.com/umccr/ega-submit) 

Walk through process: [https://github.com/QingliGuo/EGA_Data_submission](https://github.com/QingliGuo/EGA_Data_submission) 

Specific software for ICGC members but may be useful/adaptable for other submitters: [https://github.com/icgc-dcc/egasub](https://github.com/icgc-dcc/egasub) (not actively maintained)


## EGA Access Process

Once a dataset of interest is found, a user must apply directly to the data access committee that controls the dataset. There may be different requirements around what information is required to be submitted to apply for access. Any dataset use must comply with the data access policy that is attached to the dataset.

Data access committees will follow their own processes to assess the application, and if approved, contact the EGA to inform them of their decision. Access is then given to a particular EGA account to download the data from their system. The EGA provides a command line program to facilitate downloading of files from the EGA - [EGA Download Client](https://github.com/EGA-archive/ega-download-client).

Download files of interest, can be a subset, particular files/runs/samples? Demonstrate how to use XMLs to subset data and download files/samples of interest.

[https://ega-archive.org/download/downloader-quickguide-APIv3](https://ega-archive.org/download/downloader-quickguide-APIv3) 

[https://github.com/EGA-archive/ega-download-client](https://github.com/EGA-archive/ega-download-client)

Unencrypt files using provided key

[https://ega-archive.org/access/data-access](https://ega-archive.org/access/data-access) 


### Resources:

EGA data access guide: [https://ega-archive.org/access/data-access](https://ega-archive.org/access/data-access) 


# Federated EGA

There are currently federated EGA nodes being set up in other countries in Europe such as Finland, Sweden, Germany and Spain. The main driver for this has been to allow for data to remain within the country it is generated.

As part of the [Human Genomes Platform Project](https://www.biocommons.org.au/hgpp), leading Australian institutes are looking into the feasibility of setting up a federated node in Australia.
