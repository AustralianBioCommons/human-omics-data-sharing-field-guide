---
title: FHIR
page_id: fhir
type: technologies_standards
toc: true
description: FHIR (Fast Healthcare Interoperability Resources) is a standard for exchanging healthcare information electronically. 
contributors: [Marion Shadbolt]
affiliations: [FHIR]
---

Stuff about FHIR

## Fast Healthcare Interoperability Resources (FHIR)

FHIR is a standard for characterising all information about a patient within a healthcare setting. As it provides specifications and rules for the way the information is captured, it allows interoperability between all systems using the same framework. This is particularly important in a healthcare setting where there may be multiple systems capturing data that need to be able to interoperate to provide the full picture of a patient’s clinical and demographic history.

FHIR can be implemented in JSON, XML, or Turtle, or SQL schema.

## Resources

A FHIR data model is built from components called ‘resources’. Each resource spells out properties and rules around the information that is captured in that resource and how they are linked to other resources. Resources are the same across different systems using the same version of FHIR, but different systems may choose to implement different combinations of resources. Properties within resources are generally not required, so it is possible that systems using the same resources may not store exactly the same information.

The resources that are embedded in the core of FHIR are designed to be used by 80% of use cases. This ensures the standard does not become bloated with resources that are very specific to a small group of users. If users need to capture additional information then it is possible to do so via the use of extensions.

## Definitions

| term | meaning |
|---|---|
| extension | [Extensions](http://hl7.org/fhir/extensibility.html) can be added to any resource. They must be properly defined so that when they are exchanged, any system/user can understand what they mean. |
| Implementation Guide (IG) | A set of resources, profiles and extensions that help implementers establish an instance of FHIR within a particular domain. |
| profile | Profiles place constraints on the core FHIR resources to more precisely define what should be captured within an Implementation guide to better suit its use case. |
| resource | A modular set of defined, structured data items that join together to form a complete FHIR implementation. |
| Terminologies | [Terminologies](https://terminology.hl7.org/documentation.html#content) consist of Code Systems, Value Sets, Concept Maps, and Naming Systems. <br><br>- Code Systems are managed collections of concepts. <br>- Value Sets are managed collections of concepts drawn from one or more Code Systems. <br>- Naming Systems are collections of objects with known identifiers. <br>- Concept Maps are objects containing relationship information between concepts across code systems. |

## Extensions

## Implementation guides

Implementation guide registry: [https://fhir.org/guides/registry/](https://fhir.org/guides/registry/)

Australian Base implementation guide: [http://hl7.org.au/fhir/4.0.0/index.html](http://hl7.org.au/fhir/4.0.0/index.html)

## Profiles

## Terminologies

FHIR package registry: [http://registry.fhir.org/](http://registry.fhir.org/)

[(Duda et al. 2022; Vorisek et al. 2022)](https://www.zotero.org/google-docs/?hRYB0H)

## FHIR and genomics

The use of FHIR in the realm of Genomics is mainly in the domain of clinical genomics, though there are some investigations into its applicability in research settings (HERNANDEZ et al. 2022). The core of FHIR does not natively support genomics specific structured data. However, there have been several Implementation Guides that suit a more Genomics based use case:

- Australian Genomics’ Clinical Picture Repository Implementation Guide: [https://aehrc.github.io/genclipr-fhir-ig/index.html](https://aehrc.github.io/genclipr-fhir-ig/index.html)
- Genomics Reporting Implementation Guide: [http://hl7.org/fhir/uv/genomics-reporting/STU2/](http://hl7.org/fhir/uv/genomics-reporting/STU2/) (ALTEROVITZ et al. 2020)
- Phenopackets Implementation Guide: [http://phenopackets.org/core-ig/](http://phenopackets.org/core-ig/)

Given the complexity of genomics data, there has also been work to develop ‘genomic operations’ to allow for wrapping of genomic data repositories to integrate with electronic health records captured in FHIR (DOLIN et al. 2022).

There is ongoing work to improve the capture of genomic information in FHIR through the HL7 Clinical Genomics Workgroup (https://confluence.hl7.org/display/CGW) and GenomeX (https://confluence.hl7.org/display/COD/Genomics).


---

# Understanding FHIR: A Guide for Non-Technical Researchers in Human Genomics

## Introduction to FHIR

FHIR, or Fast Healthcare Interoperability Resources, is a standard developed by Health Level Seven International (HL7) to enable the electronic exchange of healthcare information. It addresses the challenge of interoperability in healthcare, ensuring that different systems can communicate and share data seamlessly. This is particularly important as healthcare records become increasingly digitized, and there is a need for standardized data that is available, discoverable, and understandable across various platforms.

## Problems FHIR Addresses

### Interoperability Challenges

One of the primary issues FHIR addresses is the lack of interoperability in healthcare IT systems. Traditionally, healthcare systems have used various proprietary formats and standards, making it difficult to exchange data between different systems. This lack of interoperability can lead to fragmented patient records, inefficiencies, and increased costs. FHIR provides a standardized framework for data exchange that is both simple and efficient, allowing for the integration of data from different sources.

### Data Quality and Standardization

Healthcare organizations often have vast amounts of data stored in different formats and with varying levels of quality. FHIR helps ensure data quality and standardization by defining clear data standards and validation processes. This standardization is crucial for accurate and reliable data exchange, enabling healthcare providers to have a more complete view of a patient's medical history.

### Legacy System Integration

Many healthcare organizations rely on legacy systems that were not designed with interoperability in mind. FHIR facilitates the integration of these systems by providing middleware solutions or interoperability platforms that act as intermediaries, translating data formats and enabling seamless integration with FHIR-enabled applications.

### Security and Privacy

FHIR implementation requires careful consideration of security and privacy measures to protect patient health information. Organizations must adhere to industry best practices, such as using secure communication protocols, implementing authentication and authorization mechanisms, and encrypting data at rest and in transit. Compliance with privacy regulations like HIPAA is essential to ensure the privacy of patient data.

## Basic Concepts of FHIR

### Resources

The building blocks of FHIR are called **Resources**. These are discrete units of data that represent specific healthcare concepts, such as patients, medications, or observations. Each resource is self-contained and can be combined with others to represent complex healthcare data. For example, in human genomic research, resources like **GenomicStudy** and **MolecularSequence** can capture detailed genomic information.

### Datatypes and Profiles

FHIR uses **Datatypes** to define the kind of data that can be included in a resource. These range from simple types like strings and integers to complex types that hold structured data. **Profiles** are sets of rules that constrain or extend resources to meet specific use cases, allowing for customization while maintaining core standards.

## How FHIR Works

FHIR utilizes a RESTful API architecture, which is a set of rules for creating web services that allow different applications to communicate. This architecture is widely used in today's web services, making FHIR easy to implement and integrate with existing systems. Data is accessed and modified using standard web protocols like HTTP, and formats like JSON or XML.

## Use Cases for FHIR

### General Use Cases

- **Interoperability**: FHIR promotes interoperability by allowing healthcare systems to communicate and share data seamlessly, crucial for providing holistic patient care.
- **Patient Access**: It enables patients to access their medical records through APIs, complying with regulations like the CMS Interoperability and Patient Access Rule.
- **Clinical Decision Support**: FHIR supports decision-making processes by integrating real-time data into clinical workflows.

### Genomic Research Use Cases

- **Genomic Data Standardization**: FHIR provides a framework for representing and exchanging complex genomic data, ensuring consistent communication across platforms.
- **Integration with EHRs**: FHIR facilitates the integration of genomic data into Electronic Health Records (EHRs), supporting precision medicine by providing a comprehensive view of patient health data.
- **Research and Data Harmonization**: FHIR helps harmonize genomic data across research platforms, crucial for large-scale studies and collaborations.

## Implementation Guides

Implementation Guides (IGs) provide detailed instructions on implementing FHIR in specific contexts. In the Australian human genomic research field, guides like the **Clinical Picture FHIR Implementation Guide** and the **HL7 FHIR Implementation Guide: Genomics Reporting** help standardize genomic data representation and reporting. These guides ensure consistent data exchange, supporting research and clinical decision-making.

## Setting Up and Using FHIR

### Setting Up FHIR

To set up FHIR, you typically create a FHIR server, which acts as a repository for storing and managing healthcare data. This server can be hosted on a physical or virtual server, using technologies like Docker for easy deployment. Alternatively, you can integrate a FHIR interface with existing systems.

### Accessing and Modifying Data

Data is accessed using RESTful API calls, allowing you to retrieve, create, update, or delete resources. For example, you can use HTTP GET requests to access patient records. To modify FHIR to suit specific needs, you can use profiles and extensions to customize resources, ensuring they capture the necessary information for your research.

### Putting Data into FHIR

There are several ways to input data into FHIR:

- **Manual Entry**: Enter data directly using user interfaces or structured forms.
- **Automated Conversion**: Use data mapping tools or ETL pipelines to transform existing data into FHIR format and load it into the server.
- **FHIR APIs**: Use RESTful API calls to load data, including bulk operations for large datasets.
- **Specialized Tools**: Use tools like the Azure FHIR Converter to convert data from other formats into FHIR.

## A User Story: Setting Up and Using FHIR in Genomic Research

As a human genomics researcher, I was tasked with setting up a FHIR server to manage and analyze genomic data for our latest research project. Here's how I approached the task:

### Step 1: Setting Up the FHIR Server

I started by setting up a FHIR server using HAPI FHIR, an open-source implementation. I opted to use Docker to simplify the deployment process. Docker allowed me to package the server application and its dependencies into a container, which I could easily deploy on our lab's virtual server.

### Step 2: Applying an Implementation Guide

Next, I applied the **HL7 FHIR Implementation Guide: Genomics Reporting** to ensure that our genomic data was represented consistently. This guide provided detailed instructions on structuring genomic data, including variant reporting and pharmacogenomic data. By following the guide, I was able to create custom profiles and extensions to capture the specific genomic attributes needed for our research.

### Step 3: Setting Up a Data Capture Interface

To facilitate data entry, I set up a user-friendly data capture interface using SMART on FHIR. This interface allowed our research team to input genomic data directly into the FHIR server. The interface was designed with structured forms that mapped directly to FHIR resources, ensuring data consistency and accuracy.

### Step 4: Inputting Data into FHIR

We began inputting data into the FHIR server using a combination of manual entry and automated data conversion. For existing datasets, I used an ETL pipeline to transform the data into FHIR format and load it into the server. For new data, the research team used the data capture interface to enter information directly.

### Step 5: Accessing and Analyzing Data

With the data in place, I accessed it using FHIR's RESTful APIs. This allowed me to retrieve specific genomic study results and sequencing data as needed. I then transferred the data to our analytics platform, where I could perform detailed research analyses. The standardized FHIR format made it easy to integrate the data with our analytics tools, enabling us to conduct comprehensive genomic studies and derive meaningful insights.

## Conclusion

FHIR is a powerful standard that transforms how healthcare data is exchanged and integrated, particularly in the field of human genomic research. By providing a standardized framework for data representation and exchange, FHIR enhances interoperability, supports precision medicine, and facilitates research collaborations. Understanding how to set up and use FHIR, and leveraging implementation guides, can significantly improve data management and utilization in genomic research.

## Resources for Further Learning

To explore more about FHIR and its applications, here are some resources:

1. **HL7 FHIR Official Website**: Provides comprehensive documentation on FHIR standards and resources. [Visit HL7 FHIR](https://www.hl7.org/fhir/resourcelist.html).

2. **Kodjin Blog on Understanding FHIR**: Offers insights into FHIR components and resources. [Read more](https://kodjin.com/blog/understanding-fhir-components-fhir-resources/).

3. **CapMinds Guide to FHIR Resources & API**: A detailed guide on FHIR resources and API interactions. [Learn more](https://www.capminds.com/blog/a-complete-guide-to-fhir-resources-fhir-api/).

4. **Medplum FHIR Resources Documentation**: Explains various FHIR resources and their uses. [Explore here](https://www.medplum.com/docs/api/fhir/resources).

5. **FHIR Drills Bundle Tutorial**: Provides a tutorial on using FHIR Bundles for data grouping and transmission. [Check it out](https://fhir-drills.github.io/bundle.html).

These resources offer valuable information for anyone looking to deepen their understanding of FHIR and its role in healthcare data interoperability.