---
title: Editing tips
page_id: editing_tios
type: contribute
toc: true
contributors: [Marion Shadbolt]
---

## Editing the config file

A lot of the aspects of the website are changed by editing the `_config.yml` file. The [ELIXIR Toolkit Theme](https://elixir-belgium.github.io/elixir-toolkit-theme/configuring_theme) website has more detailed documentation and details the options available.

## Editing styling

The files that determine the overall styling of the pages are found in the `_sass` folder. Here you can define custom styles, colours, sizes etc.

## Copying other styles

Looking at other websites using this theme is a great way to learn how to implement certain features and styles, [see the list](https://elixir-belgium.github.io/elixir-toolkit-theme/#this-theme-is-known-to-be-used-in) on the ELIXIR toolkit theme website for a list of websites using the theme.

## If build fails...

If the build step of the deployment fails, go to the logs to see if there is an error that explains the issue. Commonly things might have failed due to invalid yaml/css syntax.

1. To view the logs, go to the [Actions](https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/actions) tab on the repo, and click the workflow run that failed.
1. Click on the step that failed and read through the logs to find the source of the error
1. Try to fix the source of the error

If the build fails, the previous version of the website will remain until an updated, successful build is run.

## Getting Help

Any issues with the theme itself can be raised with the ELIXIR Toolkit theme team by [raising an issue](https://elixir-belgium.github.io/elixir-toolkit-theme/configuring_theme) on their GitHub repo. You can also search through previous issues to see if anyone else has had similar issues and found a solution.



