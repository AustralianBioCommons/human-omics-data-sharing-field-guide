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




## Guide to adding to resources table



