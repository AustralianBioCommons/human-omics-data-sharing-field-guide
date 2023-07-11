[![theme badge](https://img.shields.io/badge/ELIXIR%20toolkit%20theme-jekyll-blue?color=0d6efd)](https://github.com/ELIXIR-Belgium/elixir-toolkit-theme)

# Australian BioCommons Human 'Omics Field Guide


A prototype website for the WIP Human 'Omics Field Guide.

Any suggestions or contributions are most welcome!

## Abstract

Human Genomics data sharing is an increasingly complex task. Researchers need to juggle legal, ethical and intellectual requirements, along with publishing and funding responsibilities. Although the majority of researchers want to do the right thing, navigating the maze of data, tool, workflow and protocol repositories; software, protocol, metadata and infrastructure standards is not an easy task. Let alone staying up to date with major genome projects and support agencies that can help them on their quest. The Human Genomics Data Sharing Field guide seeks to provide a comprehensive resource that gathers together essential information on a broad range of topics to help Australian researchers on their genomics data sharing journey. 

## Deployment

The website is deployed using GitHub actions defined in the workflow here: [github-pages.yml](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/main/.github/workflows/github-pages.yml)

The action is run each time a new commit is pushed to the GitHub repository.

The actions perform three things:
1. Extract references from the group Zotero library and save it to the `_bibliography` folder as `references.bib`
2. Builds the website using Ruby/Jekyll, converting all the markdown files to html
3. Deploys the website
