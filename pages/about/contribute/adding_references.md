---
title: How to add references
toc: true
contributors: [Marion Shadbolt]
---

The references for the field guide are managed using a Zotero group library - [HumanGenomicsFieldGuide](https://www.zotero.org/groups/4744118/humangenomicsfieldguide/library). This library is openly accessible for read-only access but only members of the group can edit references. 

Each time the website is built, [a script](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/main/var/extract_zotero.py) to extract all references from Zotero and save as a bibtex file (`_bibliography/references.bib`) in the repo is run via [GitHub actions](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/main/.github/workflows/github-pages.yml). 

## Adding references to bibliography

{% include callout.html type="note" content="Ensure you have [Zotero](https://www.zotero.org/) installed with the appropriate browser addon and the ability to add references to the Zotero group library, if you need to be added as a member, please [contact the HGI team](mailto:marion@biocommons.org.au)." %}

1. Open the Zotero desktop app
1. Go to the webpage of the publication you want to add to the group library
1. Use the Zotero browser add-on and ensure the reference is added to the correct group library i.e. `HumanGenomicsFieldGuide`

Next time the Human 'Omics field guide is updated, the new reference will be automatically added to the `_bibliography/references.bib` file.

## Adding citations to a page

Any citation in the `_bibliography/references.bib` file can be referenced using its identifier. This is done through the use of the [Jekyll Scholar](https://github.com/inukshuk/jekyll-scholar) extension.  

To find out the identifier of the article you want to reference:

1. Open the `references.bib` file in a text editor or in [a browser](https://raw.githubusercontent.com/AustralianBioCommons/human-omics-data-sharing-field-guide/main/_bibliography/references.bib).
1. Search for the article in the file by using keyword or author names
1. Once you have found the article, copy the article identifier, the first part of the entry, just after the `@article{`. It is usually a combination of the first author, a key word from the title, and the year of publication. e.g. `zappia_exploring_2018`
1. Open the markdown file of the page where you would like to add the citation
1. At the location where you want to add the reference, use the identifier to create the following code:

{% raw %}
```
{% cite $identifier %}
```
{% endraw %}

So using the example above, this would look like

{% raw %}
```
{% cite zappia_exploring_2018 %}
```
{% endraw %}

When the website is built, this will be rendered into a reference like this: {% cite zappia_exploring_2018 %}

## Adding reference list to a page

If you would like to have a list of the references that have been cited on a page at the bottom, simply use the following code:

{% raw %}
```
{% bibliography --cited %}
```
{% endraw %}

Using our example reference, this would look like this:
{% bibliography --cited %}

If you want to list all references  that are in the entire `references.bib` file, remove the `--cited` tag. This is what is displayed on the [References](https://australianbiocommons.github.io/human-omics-data-sharing-field-guide/references) page.

## Modifying citation and reference style and appearances


The overall style and format of citations and references is determined by the `scholar` block in the [`_config.yml`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/90cbd1f372ab2e50fc4ad3ea94fa185dfd798973/_config.yml#L85).

You can modify what is displayed in the reference when it is listed by editing the [_layouts/bib.html](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/main/_layouts/bib.html) file.

More information about how to edit the configurations can be found in the [Jekyll Scholar Documentation](https://github.com/inukshuk/jekyll-scholar#configuration).
