---
title: Contribute
toc: true
contributors: [Marion Shadbolt]
---

## Ways to contribute:

### GitHub Issues

If you find an error, bug or mistake, please [make a github issue](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/issues/new) detailing the problem and we will do our best fix it as soon as we can. This can also be done by clicking the `!` symbol next to the title of any page.

### GitHub Pull Request

If you would like to contribute a section or some text or fix an error yourself, please fork and create a pull request and we will review and incorporate as soon as we can. 

This can be done by clicking the pencil symbol next to the title of any page, you will be taken to the page on github where you can again click the pencil symbol, make your changes then create a pull request for review.

For more complex changes or addition of new pages, you may find it easier to fork the repo then clone to your local machine and make changes locally before pushing back to GitHub and creating a pull request.

### Email

If you are not too familiar with GitHub, please feel free to [send us an email](mailto:marion@biocommons.org.au) and we will get back to you as soon as we can.

Thanks for your contribution!

## Guide to adding references

The references for the field guide are managed using a Zotero group library - [HumanGenomicsFieldGuide](https://www.zotero.org/groups/4744118/humangenomicsfieldguide/library). This library is openly accessible for read-only access but only members of the group can edit references. 

Each time the website is built, [a script](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/main/var/extract_zotero.py) to extract all references from Zotero and save as a bibtex file (`_bibliography/references.bib`) in the repo is run via [GitHub actions](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/main/.github/workflows/github-pages.yml). 

### Adding references to bibliography

{% include callout.html type="note" content="Ensure you have [Zotero](https://www.zotero.org/) installed with the appropriate browser addon and the ability to add references to the Zotero group library, if you need to be added as a member, please [contact the HGI team](mailto:marion@biocommons.org.au)." %}

1. Open the Zotero desktop app
1. Go to the webpage of the publication you want to add to the group library
1. Use the Zotero browser add-on and ensure the reference is added to the correct group library i.e. `HumanGenomicsFieldGuide`

Next time the Human 'Omics field guide is updated, the new reference will be automatically added to the `_bibliography/references.bib` file.

### Adding citations to a page

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

### Adding reference list to a page

If you would like to have a list of the references that have been cited on a page at the bottom, simply use the following code:

{% raw %}
```
{% bibliography --cited %}
```
{% endraw %}

Using our example reference, this would look like this:
{% bibliography --cited %}

If you want to list all references  that are in the entire `references.bib` file, remove the `--cited` tag. This is what is displayed on the [References](https://australianbiocommons.github.io/human-omics-data-sharing-field-guide/references) page.

### Modifying citation and reference style and appearances

The style and format of the references is controlled by the [_layouts/bib.html](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/main/_layouts/bib.html) file.

More information about how to edit this can be found in the [Jekyll Scholar Documentation](https://github.com/inukshuk/jekyll-scholar#configuration).


## Guide to adding affiliations

Affiliations to institutes, projects or countries can be added to pages. 

To add an affiliation to the list of affiliations that can be referred to, it needs to be added to the [`_data/affiliations.yml`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/main/_data/affiliations.yml).

An example of how to do this can be seen below:

```yaml
- name: ELIXIR Europe                                 # name of the affiliation, used to reference it
  image_url: /images/infrastructures/ELIXIR-logo.svg  # path to the logo for this affiliation
  pid:                                                # identifier (optional)
  expose: true                                        # whether the affiliation can be referenced 
  type: infrastructure                                # type of affiliation
  url: https://elixir-europe.org/                     # link of affiliation
```

Country affiliations are automatically included, to understand the abbreviation used for a particular country see the [`_data/countries.yml`](https://github.com/ELIXIR-Belgium/elixir-toolkit-theme/blob/main/_data/countries.yml). 

To reference an organisation or country affiliation from a page, it needs to be added to the yaml front matter of that page as follows:

```yaml
---
title: EGA
contributors: [Marion Shadbolt]
description: Controlled access database for human data.
affiliations: [ELIXIR Europe, GA4GH, EMBL-EBI, Centre for Genomic Regulation, GB, ES]
---
```

These affiliations then show up on the navigation tiles and allow filtering on organisation and country. As well as linking directly to the provided affiliation link.

Example result from the [Data repositories exaplained](https://australianbiocommons.github.io/human-omics-data-sharing-field-guide/data_repositories#data-repositories-explained) section:

{% include image.html file="/screenshots/EGA-nav-tile.png" caption="Screenshot of EGA navigation tile with affiliations" alt="EEGA navigation tile with affiliations" max-width="10" %}


## Guide to adding contributors

The Elixir Toolkit theme allows you to show who has contributed to the site as a whole, as well as those who have contributed to individual pages.

All contributors to this site are listed on the [Contributors](https://australianbiocommons.github.io/human-omics-data-sharing-field-guide/contributors) page.

The listed contributors are populated from the [`_data/CONTRIBUTORS.yml`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/main/_data/CONTRIBUTORS.yml)

For each contributor, an indented block of text is used and links are automatically generated, including automatically pulling the user's GitHub profile photo if a GitHub username is listed.

If you make a contribution to this resource, please feel free to add yourself to the list!

The block of text should look like this:

```yaml
Firstname Lastname:
    git: github_username
    email: users@email.com
    orcid: 0000-1234-5678-9012
    role: users_role
    affiliation: declared affiliation (not linked)
```

Once a user is listed in this way in this file, a tile will be generated on the Contributors page. This is done by using the following code:

{% raw %}
```markdown
{% include contributor-tiles-all.html %}
```
{% endraw %}

To add a contributor on an individual page, the name of the contributor (`Firstname Lastname` as above), must be added to the yaml front matter of the page:

This would look something like:

```yaml
---
title: Australian Legal Landscape
contributors: [Bernie Pope, Marion Shadbolt]
toc: true
---
```

Contributor chips are then automatically listed at the bottom of the page.

## Guide to adding to resources table


