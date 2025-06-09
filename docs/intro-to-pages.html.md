# Intro to pages ​

Academy

Want to learn how to create and organize pages in WeWeb? Check out our Build a Proof of Concept course, which covers essential page creation techniques and how to design effective page structures.


# Intro to pages ​

A page is the distinct screen that appears when visitors go to a specific web address (URL) on your web app. Each page shows different information and features, like how a "Contact" page displays contact details while an "About" page shows company information.


## Create a page ​

Here's an interactive tutorial on how to create a page:

Let's go over all the steps:

- Open the page dropdown in the top navbar
- Click on Add page
- Name your page
- Decide if you want to copy content from an existing page
- If copying from another page, decide if you want some sections to be linked
- Click on Create to create the page

`Add page`
`Create`
TIP

Linked sections are referred to as Multi-page sections in WeWeb. They are useful to improve the user experience and page loading time of your web application.

`Multi-page sections`
Learn more about using multi-page sections in WeWeb.


## Page name ​

The name of the page. This is the name that you will see in the page panel:




## Page folder ​

The folder that the page is in. You can create folders to organize your pages:




## Draft mode ​

Pages with draft mode Enabled won't be included when you publish your WeWeb app.

`Enabled`
Pages that are in draft mode can be identified by a different color in the Pages panel:

`Pages`


WARNING

Changing a page's Draft mode setting only takes effect after you (re)publish the app.

`Draft mode`
For example, if the app was published when Page A had draft mode set to Disabled, changing the draft mode of Page A to Enabled in the WeWeb Editor won't remove the page from production until you publish the app again.

`Disabled`
`Enabled`

## Url paths ​



This is where you can change the path of the page. This is the path that your users will see in the URL bar when they visit the page.

You can also add variables to the path.

For example, if you add a variable called product_id to the path, you can access the value of the variable in the page by using the From path in current page section in the data explorer:

`product_id`
`From path in current page`


TIP

Adding variables is helpful to create detail pages for your collections. For example, if you have a collection called products, you can create a page called products/{product_id} and then use the product_id variable to display the details of the product.

`products`
`products/{product_id}`
`product_id`
Learn more about dynamic collection pages.


## Trigger workflows ​

This is where you can setup the workflows that will be triggered when the page is visited.

In the example below, before we fetch the collections present on the page, we trigger a workflow to update the current user's preferences:



You can trigger page workflows:

- on app load before fetching collections,
- on page load before fetching collections,
- on app load,
- on page load,
- on page scroll,
- on page resize,
- on collection fetch error,
- on page unload.

Use cases include, but are not limited to:

- reacting to a user scrolling up or down the page,
- updating a variable before a collection is fetched,
- checking for a Stripe purchase after a page is loaded,
- manipulating collection data before displaying it on the page,
- displaying a customized error message when a collection fetch fails, etc.


## Custom code ​

This is where you can add custom code to the page.

You can add custom code either:

- in the page header, so that the code is loaded right before the page is loaded (useful to add custom CSS or JS, but hurts SEO performances).
- in the page body, so that the code is loaded right after the page is loaded (useful for tracking scripts, doesn't hurt SEO performances).

in the page header, so that the code is loaded right before the page is loaded (useful to add custom CSS or JS, but hurts SEO performances).

in the page body, so that the code is loaded right after the page is loaded (useful for tracking scripts, doesn't hurt SEO performances).



TIP

When you add custom code at page level, the code is only added on that page.

If you want to install app-wide custom code, you can do it in the Custom code section in the Settings panel.

`Custom code`
`Settings`
Learn more about adding custom code at app level.

WARNING

When you add custom CSS to a page or project, you should not add any <head> or <body> tags. WeWeb handles those tags for you.

`<head>`
`<body>`

## Languages ​

In the Languages panel, you can:

`Languages`
- Add languages to your project
- Define the default language of your project
- Decide if you want to add the default language slug to the URL path of the current page
- Decide which languages should be enabled on the current page
- Toggle between active languages to preview the page content in different languages



Assuming you have multiple languages enabled on a page:

- all the text elements on the page will invite you to provide the content in those languages
- you can then toggle between languages, and
- the appropriate text will be displayed




## Duplicate ​

Here, you can duplicate the page. This is useful if you want to create a page that is similar to another one, but with different content.

The Duplicate page panel provides the same options as the Create new page panel with the Copy from option selected:

`Duplicate page`
`Create new page`
`Copy from`



## Create collection page from ​

Here, you can create a static collection page:



Static collection pages are helpful if you want to publish collection pages with pre-rendered content.

WARNING

To create a static collection page, you will need to bind the Page collection and Page default path to a static collection.

`Page collection`
`Page default`
Learn more about static collection pages and dynamic collection pages.


## Make {page} the homepage ​

Here, you can make the current page the homepage of your app. The homepage is the page that will be displayed when you access the root URL of your app.


## Remove page ​

Here, you can delete the page. This is useful if you want to remove a page from your app:



