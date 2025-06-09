# Intro to collections ​

Academy

Want to learn more about working with data in WeWeb? Check out our Build a proof of concept course which teaches you how to connect data sources and display collection data effectively in your web applications.


# Intro to collections ​

In WeWeb, a collection is a set of data fetched from a 3rd-party API or backend. You can then use this data to display it in your app.


## Pre-requisites ​

WARNING

Before you can create a new collection of data in WeWeb, you first need to have installed at least one data source plugin, e.g. Xano, Supabase, REST API, etc.

Once you have added a data source plugin, you will be able to create a collection to fetch data from that source.


## Understanding APIs ​

The principle of collections is that you can make an API call to an external data source, momentarily store that data in WeWeb, and then have an easy way to utilize it in your project.

DATA SECURITY

Although the wording 'momentarily store that data in WeWeb' was used above, as long as you are using the collection mode Dynamic, the data is never actually stored in anyway by WeWeb. It was just worded this way for simplicity.

`Dynamic`
When you fetch a collection, none of the data passes through the WeWeb servers in anyway. It goes straight from the external data source to the user's browser.

This is noteworthy, as this ensures you can use WeWeb and meet common data security compliance requirements, like GDPR.

Understanding the basics of how to work with APIs will be extremely useful in order to understand the basics of working with collections, as collections are just a way to easily fetch data from APIs.

We have a dedicated page on understanding APIs, but the basic things you need to know are that an API consists of:

- the type of request you are making (do you want to get data, or edit data, or delete data etc)
- where you are making the request to (the URL of the external data source)
- any additional information you want to send (such as the fields you want to filter by)


## Create a collection ​

To create a collection, go to the Data tab in the left sidebar, then click on + New to start setting up the collection.

`Data`
`+ New`
The setup process is different for every data source plugin, but it revolves around the following steps:

- give your collection a name
- select the data source plugin you want to use
- select the collection mode
- configure how you want to fetch the data
- fetch the data
- apply any frontend sort, filter or pagination

Let's look at an example:

SOURCE TYPES

In the example above, we used the REST API plugin as the source of our collection.

However, any of the available data source plugins can be used as the source of a collection.

View the full list of available data source plugins →


## How to use a collection ​

Collections are typically used to display data in a list or a grid. The most common way to do this in WeWeb is via the Repeat Items property.

`Repeat Items`
To learn more about how to utilize collections and dynamically display lists of data, view the guide on how to bind the repeating of items.


### Understanding what's inside a collection ​

Collections look like this inside the data explorer:



What are all these fields to be used for?:

- first, the most important field will likely be the data field, as this is the actual list of items that you can use to display the items.
- secondly, the other metadata fields are to be used for other core pieces of the user experience, such as: using the isFetched and isFetching values to show loaders while the collection is loadingusing the total value to display the total number of items in the UI
- using the isFetched and isFetching values to show loaders while the collection is loading
- using the total value to display the total number of items in the UI

`data`
- using the isFetched and isFetching values to show loaders while the collection is loading
- using the total value to display the total number of items in the UI

`isFetched`
`isFetching`
`total`
Let's discuss each field:

- data[index] shows the data for the item at the index index in the collection. It's useful to bind to a specific item in the collection. To change the item, you can use the index dropdown next to the data property.

`data[index]`
`index`
`data`
UNDERSTANDING INDEXES

In web development, the 'index' just refers to the numbering of items in a list, and they always start at 0, not 1. For example, the first item in the list would have an index of 0, the second item would have an index of 1, etc.

- Length is the number of items there are in the collection.

`Length`
TIP

To know if a collection is empty, use the Length property. If it's equal to 0, the collection is empty!

`Length`
`0`
- isFetching is a boolean that tells you if the collection is currently fetching data. It's useful to display a loading state while the data is being fetched.
- isFetched is a boolean that tells you if the collection has already been fetched.

`isFetching`
`isFetched`
TIP

To display a loading state while your collection is being fetched, you can use a loading GIF or SVG, and bind its display property to the collection's isFetching property.

`display`
`isFetching`
- limit is typically the maximum number of items per page. If there is no limit, you can expect this to be null or NaN, otherwise, you can expect it to be the maximum number of items per page you have set.
- total is the total number of items in the collection. This is different to the Length field, as the total field is the total number of items inside the entire collection. If you are using pagination, these fields will be different, as the Length will tell you the number of items on the current page, whereas the total will tell you the total number of items in the entire collection.
- offset is the index at which the list starts. For example, if the offset was 0, then you would know the returned data begins from the first item in the list. However, if the offset was 1, then you would know the first item has been skipped and not included,

`limit`
`total`
`Length`
`total`
`Length`
`total`
`offset`
`offset`
`offset`

## Optimize collection load ​

By default, a collection is:

- fetched automatically when a user navigates to a page that uses that collection, and
- is preserved (not fetched again), when a user navigates to other pages in the app.

To optimize the performance and UX of your web app, you can change that default behavior in the Fetch data step of the collection setup:

`Fetch data`


Fetch this collection automatically tells WeWeb if it should fetch the collection whenever a page loads that contains a binding that uses the collection. This binding can be anywhere on the page. Even if just a single workflow or element contains a binding that uses the collection, it will be automatically fetched. If you want to disable this and control the fetching manually, you can simply toggle this off and utilize the Fetch collection workflow action when necessary.

`Fetch this collection automatically`
`Fetch collection`
Preserve on navigation tells WeWeb if it should keep the collection in memory when the user navigates to a new page. If you want to fetch the collection again, you can trigger the Fetch collection workflow action.

`Preserve on navigation`
`Fetch collection`
There may be use cases where you want to change these default settings.


### Why disable automatic fetch? ​

If you have a collection that you don't need immediately on page load, you should consider disabling the automatic fetch to improve performances. For example, you might want to fetch a collection when the user opens a modal on a page and not on page load.

If you disable the automatic fetch on a collection, you'll need to remember to trigger a workflow that fetches the collection every where you need it in the app.


### Why disable preserve on navigation? ​

A common use case where you don't want to preserve on navigation: a collection that fetches a single item selected on a previous page (if you preserve on navigation, there might be a blink where the info from the previously selected item appears while the API call takes place to fetch the info of the new selected item)

This is especially problematic if the collection data concerns a specific user with potentially private information. You want to make sure that data is not preserved on navigation in case 2 users connect to your app using the same browser.


## Collection modes ​

TIP

To build dynamic web applications, we highly recommend creating Dynamic collections.

`Dynamic`
However, at times, when you need to pre-render content or bypass API rate limits from a data source, you may want to consider working with a Static or Cached collection instead.

- Static: the collection will be fetched once, on our servers, while the app is built. Everytime this collection is used in your app, the data will be pre-rendered (better for SEO, can slow down the publish process).
- Dynamic: the collection will be fetched on the client side, when the app is loaded. This is the best option if you want to fetch data that changes often (like a list of products).
- Cached: the collection will be fetched on the client side, but from our servers. This is the best option if you want to fetch data that changes often, but you want to avoid hitting any API rate limit (but you'll need to refresh the data yourself when it changes).

`Static`
`Dynamic`
`Cached`

## Frontend vs Backend filters ​

When setting up a collection, you have two options for filtering your data: frontend filters or backend filters.


### What's the difference? ​

- Backend filters apply filters on the server side before the data is sent to your app. The external data source only sends the filtered data that matches your criteria.
- Frontend filters apply filters after all the data has been received by your browser. The complete dataset is first downloaded to the user's browser, and then filtered locally.

Backend filters apply filters on the server side before the data is sent to your app. The external data source only sends the filtered data that matches your criteria.

Frontend filters apply filters after all the data has been received by your browser. The complete dataset is first downloaded to the user's browser, and then filtered locally.

Here's what happens in each case:

SECURITY CONSIDERATION

When you use frontend filtering, all data is downloaded to the user's browser first, even if it's filtered out later. This means anyone could inspect the network requests and see the complete dataset.

If your data contains sensitive information, you should use backend filtering to ensure that sensitive data never leaves your server.


### When to use which type of filter? ​

- Use backend filters when:you have a large amount of datayour data contains sensitive informationyou need to implement security at the data levelyou have APIs that support filtering parameters
- you have a large amount of data
- your data contains sensitive information
- you need to implement security at the data level
- you have APIs that support filtering parameters
- Use frontend filters when:you have a small dataset (hundreds of items, not thousands)the data contains no private informationyou need quick, dynamic filtering without additional API callsyou're working with APIs that don't support filtering parameters
- you have a small dataset (hundreds of items, not thousands)
- the data contains no private information
- you need quick, dynamic filtering without additional API calls
- you're working with APIs that don't support filtering parameters

Use backend filters when:

- you have a large amount of data
- your data contains sensitive information
- you need to implement security at the data level
- you have APIs that support filtering parameters

Use frontend filters when:

- you have a small dataset (hundreds of items, not thousands)
- the data contains no private information
- you need quick, dynamic filtering without additional API calls
- you're working with APIs that don't support filtering parameters

Learn more about adding security to the web-apps you build with no-code tools.

WHAT YOUR DATA SOURCE ALLOWS

Depending on the data source plugin you are using as the source of collection, you may only have the ability to apply either frontend or backend filtering, or in some cases both.

For example, the Supabase plugin only allows for backend filtering natively.

Each data source plugin will have its own unique way to configure the fetching and filtering data.

View the full list of available data source plugins →


## Applying backend filters ​

Depending on the data source plugin you are using, there will be variance in the exact way to specify your filters. However, the one core thing that will not change and allows you to identify when you are apply a backend filter is that filter configuration is applied before the fetch step:

Here is an example of configuring a backend filter in your request:

AVAILABLE FILTERS

To know what query strings and values will be accepted by an API endpoint, you will need to refer to its respective documentation.

In the example above, we passed the query sting symbols and value btc because the documentation of the API we are using explicitly says it accepts symbols as a query:

`symbols`
`btc`
`symbols`
ADVANTAGES OF BACKEND FILTERING

Backend filtering provides several important benefits:

- improved security by keeping sensitive data on the server
- better performance with large datasets by reducing the amount of data transferred
- reduced memory usage in the browser
- better scalability as your dataset grows over time

This approach is ideal for production applications dealing with sensitive information or large amounts of data.


## Applying frontend filters ​

With frontend filtering, the filter configuration is applied after the data has been fetched. This is the key indicator that you're working with frontend filters:

Here's how to set up frontend filters in WeWeb:

ADVANTAGES OF FRONTEND FILTERING

Frontend filtering gives you more flexibility since you can:

- apply complex filter logic that may not be supported by the API
- change filters instantly without making additional API calls
- create dynamic, responsive filtering as users type or select options
- filter on any field in the data, not just what the API exposes

Remember, though, that all data is downloaded first. This can cause data security issues and performance issues if dealing with very large datasets


### Frontend filter options ​

- Pagination is the number of items that are displayed per page. It's useful if you have lot of data to display, and you want to split it into multiple pages. We have a Paginator element that allows you to easily handle this.
- Filter is a formula that filters the data. It's useful if you want to display only a subset of the data.

Pagination is the number of items that are displayed per page. It's useful if you have lot of data to display, and you want to split it into multiple pages. We have a Paginator element that allows you to easily handle this.

`Pagination`
Filter is a formula that filters the data. It's useful if you want to display only a subset of the data.

`Filter`
Let's look at an example: 

Here, we're filtering the data to only display companies where their name contains the letter t or, (where their domain contains www and their number_of_employees is greater than 100).

`name`
`t`
`domain`
`www`
`number_of_employees`
`100`
As you can see, you can create groups of filters using condition groups.

`condition groups`
For each of these groups or conditions, you can set them under certain conditions (using the Apply if...). For example, when a variable is true or false in your app.

`Apply if...`
`true`
`false`
You can also use the AND and OR operators to combine filters.

`AND`
`OR`
The toggles are Ignore if empty options that tell WeWeb not to apply the filter if the value is empty.

`Ignore if empty`
Sort is a formula that sorts the data. It's useful if you want to display the data in a specific order (like ascending or descending order for alphabetical or numerical values, etc).

`Sort`


