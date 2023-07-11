---
title: How to edit the home page
type: contribute
toc: true
contributors: [Marion Shadbolt]
---

The homepage is populated from the `index.html` file. It is written mainly in `html` but also incorporates some elements that it populates from other configuration files. When there is code that is enclosed in curly brackets e.g.

{% raw %}
```
{% ... %}
or
{{ ... }}
```
{% endraw %}

it is reading information from elsewhere or running some javascript.

## Header

### The logo

The logo displayed in the top left corner gets automatically populated from `assets/img/main_logo.svg`. To change the logo it is easiest to replace this logo with your preferred image, retaining the same filename.

### Top Navigation bar

The navigation options in the top navigation bar are configured by editing the `_data/topnav.yml` file. Here you can link to particular pages or sidebar views of the page. Currently, we link to the home page or to the `about` sidebar view. 

The GitHub link in the top right is configurable by editing the `_config.yml` file. To disable it, you would need to add a line to the file specifying `github: false`, like so

```yaml
theme_variables:
  topnav:
    github: false
```

Further configuration options are specified in the [ELIXIR toolkit theme documentation](https://elixir-belgium.github.io/elixir-toolkit-theme/configuring_theme).

## Development banner

To edit the banner at the top of the page, the [following section](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/4939e03ef83527fc618c11eb8f062c91988a91b3/index.html#L13C3-L20C15) of code needs to be edited:

```html
    <section class="container mb-5">
        <div class="card border border-primary text-primary text-center">
            <div class="card-body">
                <h7 class="card-title fs-3">This website is under active development</h7>
                <p class="card-text">Don't hesitate to <a href="https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/issues">open an issue</a> or to contact us via <a href="mailto:marion@biocommons.org.au">email</a> to give some early feedback.</p>
            </div>
        </div>
    </section>
```

Text and links can be updated or the whole section can be deleted once we know longer want to display this.

## Text below banner

The text below the banner is within this section and can be updated by editing the html within this [`div`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/4939e03ef83527fc618c11eb8f062c91988a91b3/index.html#L24)

## Search bar

The search bar section has the id [`search-section`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/4939e03ef83527fc618c11eb8f062c91988a91b3/index.html#L28). Editing this section you can change the [placeholder](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/4939e03ef83527fc618c11eb8f062c91988a91b3/index.html#L37C37-L37C48) text that appears in the search bar as well as the [icon](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/4939e03ef83527fc618c11eb8f062c91988a91b3/index.html#L35C82-L35C126).

## Topic Tiles

The tiles that display below the search bar are configured in [this section](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/4939e03ef83527fc618c11eb8f062c91988a91b3/index.html#L45C1-L68C19).

The tiles that are shown are based on the sections within the main sidebar, it will create one tile for each [`subitem`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/4939e03ef83527fc618c11eb8f062c91988a91b3/_data/sidebars/main.yml#L3) based on each listed `title`. The icon image that is displayed is defined by the `image-url` field for each subitem. These are currently saved within `assets/img/section-icons`. 

{% include callout.html type="note" content="If the icons are changed for the section tiles, please update the references in the [footer section](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/4939e03ef83527fc618c11eb8f062c91988a91b3/_data/footer.yml#L2C1-L2C1) and [acknowledgements](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/main/pages/about/acknowledgements.md) page (if attribution is required)." %}

The grid layout of the tiles is determined by the [`class`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/4939e03ef83527fc618c11eb8f062c91988a91b3/index.html#L49) attributes of the `div` that contains the tiles. This determines how many columns will show on small or large screens. It is currently set at 2 but can be increased or decreased as required.

## Contribution section

The icon that appears on the left for this section is determined by the [`img`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/4939e03ef83527fc618c11eb8f062c91988a91b3/index.html#L73) div. It can be updating by changing the link within the `src` attribute to an alternate relative path of an image within the repo.

The text can be edited in the [`div`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/4939e03ef83527fc618c11eb8f062c91988a91b3/index.html#L76C24-L79C29) below by adjusting the heading and paragraph.

The button is linking to the 'contribute' page and can be updated by modifying the `href` argument [on this line](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/4939e03ef83527fc618c11eb8f062c91988a91b3/index.html#L82C78-L82C112).

## News section

The items that show up in the news section are populated from the [`_data/news.yml`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/main/_data/news.yml) file. Each entry entered on this file will automatically show up in the news section of the homepage as well as on the [news page](https://australianbiocommons.github.io/human-omics-data-sharing-field-guide/news) under the 'about' sidebar.

## Stats section

The 'Human 'Omics Data Sharing Field Guide in numbers' section is automatically populated from the information on the website. It is generated by this [code container](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/4939e03ef83527fc618c11eb8f062c91988a91b3/index.html#L96C8-L144C19) . The displayed text can be edited by editing the various paragraph sections as required.

## The footer

The footer information is populated from the [`_data/footer.yml`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/main/_data/footer.yml) file, including the copyright, logo and links. 
