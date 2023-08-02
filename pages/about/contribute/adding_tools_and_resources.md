---
title: How to add to and edit tools and resources
page_id: adding_to_tools_resources
type: contribute
toc: true
contributors: [Marion Shadbolt]
---

The [tools and resources](tools_resources) table is automatically created from the yaml file: [`_data/tool_and_resource_list.yml`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/main/_data/tool_and_resource_list.yml). This file should not be edited directly. To add to or edit the information in the table, please add to or edit the information in the `Field Guide Tools and Resources` google sheet which is located within the BioCommons `Human Data` Google folder under `Activities/Human Omics Data Sharing Field Guide`. Each time the website is built, the script [`var/tools_table_converstion.py`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/main/var/tools_table_conversion.py) runs as part of the [GitHub Actions](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/bf2bd38ee26441ecc1c5ec1de537a45216e35d9c/.github/workflows/github-pages.yml#L25) that deploy the site, and converts the google sheet to the yaml file.

## Editing the Google Sheet

**Columns:**

- **name**: This is the display name that will show up when a tool is tagged and in the table
- **url**: the full url of the resource (required)
- **description**: A brief description of what the tool or resource is
- **id**: kebab-case (lower case with hyphens) version of the tool name that is used for tagging
- **fairsharing**: The [FairSharing](https://fairsharing.org/) identifier for the resource, if one exists
- **biotools**: The [bio.tools](https://bio.tools/) identifier for the tool if one exists
- **tess**: The [Training eSupport Systen (TeSS)](https://tess.elixir-europe.org/) identifier for the tool if one exists
- **europmc**: The [Europe PMC](https://europepmc.org/About) identifier (PMID) for the most relevant publication for the tool or resource

{% include callout.html type="important" content="Note that the ability to tag tools and the information in the tables on the website will not be updated until the site is rebuilt after editing the google sheet." %}

## Tagging a tool or resource

On any page where you want to refer to a resource

Add the tool in the text by mentioning it using following syntax:
```
{% raw %}
{% tool "tool_id" %}
{% endraw %}
```
Example:

The following code snippet:

```
{% raw %}
{% tool "beacon" %} is a GA4GH standard which enables standardised querying across multiple sources.
{% endraw %}
```

Will give: 
    
{% tool "beacon" %} is a GA4GH standard which enables standardised querying across multiple sources.

{% include callout.html type="important" content="Don't forget to add the `\"` double quotes around the tool_id and make sure to use the exact tool_id as described in the yaml file." %}

When a tool is tagged on a page, a table containing all tools and resources mentioned on the page is added to the bottom of that page (see below).
