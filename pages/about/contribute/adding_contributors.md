---
title: How to add contributors
toc: true
contributors: [Marion Shadbolt]
---

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