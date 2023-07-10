---
title: How to add a new page or edit an existing page
toc: true
contributors: [Marion Shadbolt]
---

## Creating a new page

The overall process to create a page on the website is as follows

1. Create a markdown file within the relevant section's folder
1. Add the page to the relevant sidebar

### 1. Create a markdown file

Each major section of the website has a folder within the `pages` folder. All pages relating to that section have a corresponding markdown file within the folder. 

#### Using the GitHub website interface

1. Navigate to the relevant subfolder, e.g. [`pages/legal_ethical`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/tree/main/pages/legal_ethical)
1. In the top right, click on the 'Add File' dropdown, and click '+ Create new file' 
1. At the top, above the file contents, enter a short, relevant, underscore-delimited name 
1. Within the file contents, copy and paste a [yaml header](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/3191522db7db360af2286776c91a76378529f4b8/pages/repositories/hca.md?plain=1#L1C1-L6C4) from an existing page and edit as needed
1. Enter the page content using [markdown syntax](https://elixir-belgium.github.io/elixir-toolkit-theme/markdown_cheat_sheet)
1. When happy with your draft, hit the green 'Commit changes...' button in the top right and enter a short message to describe what you have changed. We are happy to choose the default option of 'Commit directly to the main branch' at the moment. If you do want a specific review of your change, you can also choose to 'Create a new branch for this commit and start a pull request', and add a specific reviewer before your change will be incorporated into the website
1. Once your commit has been incorporated into the main branch, it will trigger the website to rebuild. The progress of the rebuild can be monitored in the [Actions](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/actions) tab. It should only take a few minutes. Once you see a green tick, it means it has completed and your new page should be live on the website and viewable by going to `https://australianbiocommons.github.io/human-omics-data-sharing-field-guide/<name_of_your_file_without_.md>`. Before your new page will appear in the sidebar you will need to follow the instructions below...

### 2. Add the page to the sidebar

All pages that are part of the main sections of the website, need to be added to the **main** sidebar before they will show up in the left-hand side navigation. All pages within the **About** section, need to be added to the **about** sidebar. 

#### Using the GitHub website interface

1. Open the relevant sidebar file within [`_data/sidebars`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/tree/main/_data/sidebars), e.g. [`main.yml`](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/main/_data/sidebars/main.yml)
2. Click on the <i class="fa-solid fa-pencil"></i>pencil icon in the top right to begin editing the file
3. Find the relevant title of the section where you would like your page to be added
4. Copy the pattern already in the file to add your page. Noting that the order in the sidebar will be as it is ordered in the file. Note that the hyphen and indentation should be consistent with the existing entries.

So the added text would look something like the block below:
```yaml
    subitems:
      - title: New Page    # The title of your page as it will show up in the side navigation
        url: my_new_page   # The exact name of your file without the .md extension
```

5. Once you have added the page or pages to the sidebar, commit the file to main to trigger the rebuild. 
6. When the site has successfully rebuilt, check the sidebar has been updated but navigating to the page and refreshing

## Editing an existing page

1. Navigate to the page you want to edit on the website
1. Click the <i class="fa-solid fa-pencil"></i>pencil icon at the top of the page to the right of the page title
1. This will take you to the relevant markdown page in the GitHub repo. Again, click the <i class="fa-solid fa-pencil"></i>pencil icon at the top right of the page to begin editing the text
1. Once you have finished editing, hit the green 'Commit changes...' button in the top right and enter a short message to describe what you have changed. We are happy to choose the default option of 'Commit directly to the main branch' at the moment. If you do want a specific review of your change, you can also choose to 'Create a new branch for this commit and start a pull request', and add a specific reviewer before your change will be incorporated into the website
1. Once your commit has been incorporated into the main branch, it will trigger the website to rebuild. The progress of the rebuild can be monitored in the [Actions](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/actions) tab. It should only take a few minutes. Once you see a green tick, it means it has completed and your edits should be live on the website and viewable by visiting the page and hitting refresh

## Editing locally

For users comfortable with interacting with GitHub via the commandline, a similar process as above can be followed as above by first cloning the repo, making changes as required, committing and pushing to the remote repository. 

It is also possible (in theory) to run the website locally, see instructions on the ELIXIR toolkit theme [README](https://github.com/ELIXIR-Belgium/elixir-toolkit-theme#locally-using-jekyll).

