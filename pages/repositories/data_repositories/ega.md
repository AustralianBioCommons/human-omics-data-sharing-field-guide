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

Submission notes:

* When preparing a submission, it is important to validate and check all the details because editing after submission is not possible without going through the helpdesk. Submission to the test instance of the EGA is recommended before making your final submission.

* The **alias** field that is set for each object is not strictly required, if not specified one will be provided. BUT the alias is what you used to link between the different objects so it is useful to set to names that you can recognise to facilitate the linking that is required in your submission. Aliases must be unique across all items within a submission account.

* All data files that are referred to by ‘run’ or ‘analysis’ objects must be placed in the submission box and indexed by the system before it will allow submission of those object XMLs.

* For objects that are linked by their accessions i.e. policy, dataset, the objects they refer to must be submitted and assigned accessions by the EGA before they can be linked.

Table: Detailed information about ega objects and tips on creating XMLs for each object. Adapted from [(Band 2019; EGA n.d.)](https://www.zotero.org/google-docs/?5otJgj)


| Metadata object      | definition                                                                                                                                                                                                                                                                                                                     | Important fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | schema                                                                                                                                 | EGA Example                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| submission           | An XML that points to all the other xml files that will be included as part of a submission                                                                                                                                                                                                                                    | At least one ACTION in the ACTIONS list                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [sra.submission.xsd](https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.submission.xsd) | [Submission.xml](https://ega-archive.org/files/Submission.xml)                                   |
| study                | Describes information about the study, such as the title and abstract, and is linked to 1 or more datasets                                                                                                                                                                                                                     | STUDY\_TITLE

STUDY\_TYPE

alias - useful to refer to in later objects                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [sra.study.xsd](https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.study.xsd)           | [Study.xml](https://ega-archive.org/files/Study.xml)                                             |
| sample               | Describes the set of samples to be submitted                                                                                                                                                                                                                                                                                   | TAXON\_ID

SAMPLE\_ATTRIBUTES

*   SAMPLE\_ATTRIBUTE
    

*   TAG: subject\_id
    
*   VALUE: a unique identifier
    

*   SAMPLE\_ATTRIBUTE
    

*   TAG: gender
    
*   VALUE: male/female/unknown
    

*   SAMPLE\_ATTRIBUTE
    

*   TAG: phenotype
    
*   VALUE: EFO Term
    
*   UNITS: Experimental Ontology Factor accession
    

*   SAMPLE\_ATTRIBUTE
    

*   TAG: Any other attribute that is useful to provide and can be released open access
    
*   VALUE: the value for the tag
    

alias - useful to refer to in later objects | [sra.sample.xsd](https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.sample.xsd)         | [Sample.xml](https://ega-archive.org/files/Sample.xml)                                           |
| experiment           | Describes the sequencing experiment such as platform, model, library prep information. Typically it would collect all information that would need to be analysed together, e.g. all sequencing runs from a single library from a single sample                                                                                 | LIBRARY\_STRATEGY

LIBRARY\_SOURCE

LIBRARY\_SELECTION

LIBRARY\_LAYOUT

LIBRARY\_CONSTRUCTION\_PROTOCOL

alias - useful to refer to in later objects

Links To Other Objects:

STUDY\_REF - study alias of the study it belongs to

SAMPLE\_DESCRIPTOR - sample alias of sample object the experiment was performed on                                                                                                                                                                                                                                         | [sra.experiment.xsd](https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.experiment.xsd) | [Experiment\_illumina\_paired.xml](https://ega-archive.org/files/Experiment_illumina_paired.xml) |
| run                  | Each run contains a single data file, files that belong together get grouped under an experiment                                                                                                                                                                                                                               | FILES

*   FILE
    

*   filename
    
*   filetype
    
*   checksum\_method
    
*   checksum
    
*   unencrypted\_checksum
    

Links To Other Objects:

EXPERIMENT\_REF                                                                                                                                                                                                                                                                                                                                                                                  | [sra.run.xsd](https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.run.xsd)               | [Run.xml](https://ega-archive.org/files/Run.xml)                                                 |
| analysis - BAM/CRAM  | Metadata that describes a bam or cram file. Ideally should capture information about the reference assembly used. Can also link related files such as a readme, index and/or phenotype file.                                                                                                                                   | ANALYSIS\_TYPE

*   REFERENCE\_ALIGNMENT
    

*   ASSEMBLY
    

*   refname (INSDC assembly name)
    

*   SEQUENCE 
    

*   accession
    

FILES

*   FILE
    

*   filename
    
*   filetype
    
*   checksum\_method
    
*   checksum
    
*   unencrypted\_checksum
    

Links to Other Objects:

STUDY\_REF: study alias

SAMPLE\_REF: sample alias, Can specify multiple times if contains analysis of multiple samples

If raw files also being submitted:

EXPERIMENT\_REF: experiment alias

RUN\_REF: run alias                            | [sra.analysis.xsd](https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.analysis.xsd)     | [Analysis\_BAM.xml](https://ega-archive.org/files/Analysis_BAM.xml)                              |
| analysis - VCF       | One vcf file per analysis object and should be linked to submitted samples.                                                                                                                                                                                                                                                    | ANALYSIS\_TYPE

*   SEQUENCE\_VARIATION
    

*   ASSEMBLY
    

*   refname (INSDC assembly name)
    

*   EXPERIMENT\_TYPE
    

FILES

*   FILE
    

*   filename
    
*   filetype
    
*   checksum\_method
    
*   checksum
    
*   unencrypted\_checksum
    

Links to Other Objects:

STUDY\_REF: study alias

SAMPLE\_REF: sample alias, Can specify multiple times if contains analysis of multiple samples                                                                                                                                      | [sra.analysis.xsd](https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.analysis.xsd)     | [Analysis\_VCF.xml](https://ega-archive.org/files/Analysis_VCF.xml)                              |
| analysis - phenotype | One phenotype per analysis object and should be linked to submitted samples. E.g. phenopacket file                                                                                                                                                                                                                             | ANALYSIS\_TYPE

*   SAMPLE\_PHENOTYPE
    

FILES

*   FILE
    

*   filename
    
*   filetype
    
*   checksum\_method
    
*   checksum
    
*   unencrypted\_checksum
    

Links to Other Objects:

STUDY\_REF: study alias

SAMPLE\_REF: sample alias, Can specify multiple times if contains analysis of multiple samples                                                                                                                                                                                                                              | [sra.analysis.xsd](https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/SRA.analysis.xsd)     | [Analysis\_phenotypes\_0.xml](https://ega-archive.org/files/Analysis_phenotypes_0.xml)

<br>     |
| dac                  | Contains the contact information of all members of the data access committee that makes decisions on who can access the data. Can be used for many different policies and datasets                                                                                                                                             | TITLE

CONTACT : at least one                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | [EGA.dac.xsd](https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/EGA.dac.xsd)               | [DAC.xml](https://ega-archive.org/files/DAC.xml)                                                 |
| policy               | Describes the data access agreement and links to the data access committee (DAC) that administers it.                                                                                                                                                                                                                          | TITLE

POLICY\_TEXT

POLICY\_LINKS

*   POLICY\_LINK
    

*   URL\_LINK: to link to external web pages if applicable
    

Links to Other Objects:

DAC\_REF

*   accession                                                                                                                                                                                                                                                                                                                                                                                    | [EGA.policy.xsd](https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/EGA.policy.xsd)         | [Policy\_0.xml](https://ega-archive.org/files/Policy_0.xml)                                      |
| dataset              | Describes a set of files that are logically grouped together and represent a unit to which would be provided access. Must link to the policy that defines how it can be used and the runs and/or analyses that describe the data set files. Examples provided by the EGA include: cases and controls, or different phenotypes. | DATASET\_TYPE

Links to Other Objects:

RUN\_REF 

*   accession : repeated for all runs in the dataset
    

ANALYSIS\_REF

*   accession : repeated for all runs in the dataset
    

POLICY\_REF

*   accession EGAP
    
*   refcenter                                                                                                                                                                                                                                                                                                                      | [EGA.dataset.xsd](https://github.com/enasequence/schema/blob/master/src/main/resources/uk/ac/ebi/ena/sra/schema/EGA.dataset.xsd)       | [Dataset\_0.xml](https://ega-archive.org/files/Dataset_0.xml)                                    |


![EGA Metadata Model schematic](/images/infrastructures/EGA-Metadata-Model.png)

Figure 1. Graphical representation of EGA Metadata Model to represent a sequencing experiment with some recommended fields specified based on [EGA example xmls](https://ega-archive.org/submission/sequence/programmatic_submissions/prepare_xml). For comprehensive detail of available fields, see the [XML schemas](https://github.com/enasequence/schema/tree/master/src/main/resources/uk/ac/ebi/ena/sra/schema).


### Resources:

* Set of example XMLs created by EGA: [https://ega-archive.org/submission/sequence/programmatic_submissions/prepare_xml](https://ega-archive.org/submission/sequence/programmatic_submissions/prepare_xml) 

* A somewhat tongue-in-cheek but potentially useful 4 part run through of one user’s experience with how to submit to EGA, mostly programmatically:

[https://gavinband.github.io/bioinformatics/data/2019/05/01/Me_versus_the_European_Genome_Phenome_Archive.html](https://gavinband.github.io/bioinformatics/data/2019/05/01/Me_versus_the_European_Genome_Phenome_Archive.html) 

* Example of automated data flow to EGA from QIMRB. This transforms their internally stored metadata into the XMLs required for an EGA submission: [https://github.com/delocalizer/ega_metadata](https://github.com/delocalizer/ega_metadata) 


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
