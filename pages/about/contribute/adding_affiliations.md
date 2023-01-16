---
title: How to add affiliations
toc: true
contributors: [Marion Shadbolt]
---

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

