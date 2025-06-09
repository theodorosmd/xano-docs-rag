# Xano ​

Academy

Want to build robust and secure web applications with Xano? Check out our Scale your web app course which teaches you how to implement authentication and secure data access with Xano.


# Xano ​

Xano is a visual development backend platform that lets you build custom APIs, manage databases, and handle server-side logic without writing traditional code. Through its visual interface, you can create data storage systems, user authentication, and API endpoints - essentially everything needed to power modern web applications.


## Add Xano plugin ​

In order to get data from Xano, you first need to add Xano as a data source in WeWeb, in Plugins > Data sources:

`Plugins`
`Data sources`


TIP

Xano recently deprecated API keys. You now have to create an Access Token to connect a Xano account to a WeWeb project.

If you have existing WeWeb projects that use the deprecated method of authentication, you don't need to do anything.

However, you can choose to update them by going to the plugin configuration step and adding an Access Token:



This will ensure your project continues to work properly in the event that Xano stops supporting the deprecated API key completely in the future.

No other action is required on the WeWeb side of things. Updating the Xano data source plugin configuration will not affect the collections you previously added to WeWeb using that plugin.


### Plugin configuration ​

When you add the Xano data source plugin, you will be invited to:

- Add your personal access token
- Select the Xano instance you want to connect
- Add the custom domain of your instance (if you have one)
- Select the workspace you want to connect



WARNING

The Metadata API Key field expects the value of the Xano personal access token.

Make sure to paste the access token itself, NOT the key ID of the access token:



Note: you will only be able to view the access token once, when you first create it. Make sure to copy/paste it there and then or you might have to create a new access token down the line.

TIP

The custom domain field is optional. It is useful if you need to:

- replace the base URL of Xano with the custom domain you setup in Xano, or
- replace an old base URL with a new base URL (e.g. if you went from a free plan to a paid plan in Xano)


### Generate access token in Xano ​

To generate or find your access token in Xano, you have 2 options.

Option 1 - go to Account > Metadata API:

`Account`
`Metadata API`


Option 2 - go to the Metadata API section in the Settings of your instance:

`Metadata API`
`Settings`


WARNING

By default, when you create an access token in Xano, all the options will be enabled:



Depending on your use case, you may want to customize those settings.

Bear in mind, however, that these settings will affect what you can and cannot do in WeWeb.

For example, if you remove the reading rights to the Database and API Groups, WeWeb will have no way of fetching the data from your tables.


## Data sources (optional) ​

Depending on your Xano plan, you may have the option to support multiple data sources.

For example, you could have a live data source and a test data source:

`live`
`test`


TIP

As you can see above, Xano will display a banner at the top of your workspace to remind you what data source you're looking at at any given moment.

In WeWeb, you could decide to work with different data sources depending on whether you're working:

- inside the WeWeb editor,
- on the app published in the WeWeb staging environment, or
- on the published app in production.

In the example below, we chose to work with the data from the test data source inside the WeWeb editor, and on the app in staging:

`test`


As a result, when working in the WeWeb editor or viewing the app published in staging, the data that is displayed will be the data from the test data source in Xano. We will not be able to see or work with the data in the live data source.

`test`
`live`
WARNING

As per Xano's user documentation, "it's important to note that a test data source will have exactly the same data schema and structure as your live environment. You cannot change, edit, or delete the schema or database tables in your test data source environment. The test environment allows you to use different data or records so that you can perform tests in your API without affecting your live data."


## Branching (optional) ​

Depending on your Xano plan, you may have the option to support multiple branches.

In Xano, a branch is "a copy of a workspace's business logic (APIs, Functions, Addons, and Tasks)."

WARNING

Branches in Xano do not apply to the database. To enable test data in Xano, you need to create a test Data source.

`Data source`
Creating a branch in Xano allows you to make changes to your API endpoints, functions, add-ons and tasks in a safe environment, without affecting your app in production.

In the example below, we created a v2 branch in Xano to add features related to admin permissions in our app:

`v2`


In WeWeb, we continue to use the Xano v1 branch in our app in production, but we use the Xano v2 branch to test things in the WeWeb Editor and in our app published in staging:

`v1`
`v2`


When we're ready, we can decide to make the v2 branch live in Xano and update the Xano data source plugin in WeWeb.

`v2`
WARNING

When working with workflows in WeWeb, we will list all the fields that are available in the LIVE Xano branch, even if you have chosen an EDITING Xano branch for the WeWeb Editor in the Xano data source plugin configuration.

`LIVE`
`EDITING`
To avoid confusion, we recommend that all your Xano branches include the same fields.


## Global headers (optional) ​

If you need to add custom global headers to all your Xano calls, you can configure these in the Xano data source plugin:



Or at collection level:




## Get data from Xano ​

Once you have configured the Xano data source plugin, you will be able to create a collection to get Xano data into WeWeb:




### Select a source ​

In the Data tab, when you create a new collection, you will be invited to:

`Data`
- name the collection,
- select a data source (for example Xano), and
- choose a collection mode (for example dynamic).

TIP

To build dynamic web applications, we highly recommend creating Dynamic collections.

However, at times, when you need to pre-render content or bypass API rate limits from a data source, you may want to consider working with a Static or Cached collection instead.

Static: the collection will be fetched once, on our servers, while the app is built. Everytime this collection is used in your app, the data will be pre-rendered (better for SEO, can slow down the publish process).

`Static`
Dynamic: the collection will be fetched on the client side, when the app is loaded. This is the best option if you want to fetch data that changes often (like a list of products).

`Dynamic`
Cached: the collection will be fetched on the client side, but from our servers. This is the best option if you want to fetch data that changes often, but you want to avoid hitting any API rate limit (but you'll need to refresh the data yourself when it changes).

`Cached`

### Configuration ​

When you create the collection, you will be invited to choose the API group and endpoint you want to use in WeWeb.

In the example below, we call a GET endpoint in Xano that returns all the tickets related to the user who is currently authenticated to our app:



WARNING

If authentication is enabled on your Xano endpoint, you will need to login as a user of your app in WeWeb to fetch data. Otherwise, Xano will return an Unauthorized error.

`Unauthorized`
Same goes if your endpoint requires a user to be have a specific role to read data. You will then need to login as a user with that role to create the collection and fetch data in WeWeb.


### Fetch data ​

By default, Xano collections are fetched automatically and preserved on navigation:



This means that:

- if a collection is used on a page of your app, it will be fetched automatically, and
- if the user navigates to another page, the collection will not be refetched.

There may be use cases where you want to change these default settings.

Why disable automatic fetch?

If you have a collection that you don't need immediately on page load, you should consider disabling the automatic fetch to improve performances. For example, you might want to fetch a collection when the user opens a modal on a page and not on page load.

If you disable the automatic fetch on a collection, you'll need to remember to trigger a workflow that fetches the collection every where you need it in the app.

Why disable preserve on navigation?

A common use case where you don't want to preserve on navigation: a collection that fetches a single item selected on a previous page (if you preserve on navigation, there might be a blink where the info from the previously selected item appears while the API call takes place to fetch the info of the new selected item)

This is especially problematic if the collection data concerns a specific user with potentially private information. You want to make sure that data is not preserved on navigation in case 2 users connect to your app using the same browser.


### Sort, filter, and pagination ​

Once you have fetched data from Xano, you can add sort it, filter it, and paginate it in the frontend:

WARNING

The video above was recorded on a previous version of the WeWeb editor but the same logic still applies.

Once you have added a data collection in WeWeb, you will be able to display that data on a WeWeb page. Learn how to display collection data.


## Update Xano data ​

To update a table in Xano from a WeWeb app, you'll have to create a workflow that makes a request to Xano.

In the screenshot below, you can see that:

- we make a request to Xano
- that will affect the Joyce's tutorial - careers API group
- we're making a POST call in the application table
- updating three fields in the table
- we pass the values of these three fields

`Joyce's tutorial - careers`
`POST`
`application`


Use case: when an authenticated user applies to a job, we make a request to Xano to update the application table with the id of the selected job and authenticated user as well as the URL of the resume that was uploaded by the user.

`application`


TIP

If the field in Xano is an integer, make sure to pass an integer value in your API call. If you try sending a string to an integer field, you will get an error. If you try sending an integer to a field that expects an array, you will also get an error.

Learn more about variables and data types.


## Using Xano Auth? ​

If you have added the Xano data source plugin and are using the Xano Auth plugin for authentication, you do NOT need to bind the user's auth token when adding a Xano collection or using a Xano action in your workflows.

The Xano data source plugin will automatically recognize the current user's authentication token and send it to Xano when making an API call.

You only need to manually bind the current user's authentication token if you are making API calls to Xano via the REST API plugin and not the Xano data source plugin.


## Migrating from Airtable to Xano? ​

It's fairly common for Airtable enthusiasts to switch to backends like Xano or Supabase when scaling web-apps.

WeWeb's Xano plugin facilitates the switch from Airtable to Xano.

Step 1 – You can use Xano's import function to import Airtable tables. The import will keep the same field names and references between tables: 

Step 2 – In WeWeb, you can then change the data source of your collection from Airtable to Xano.

Your collection lists and collection list items will remain unchanged on the page because WeWeb will automatically recognize the data structure.

TIP

There may be issues with table and column names that include spaces in Airtable because those spaces will automatically be replaced by underscores (_) in Xano. As a result, WeWeb will think it's two different tables or columns and your bindings will break.

`_`
To prevent this from happening, you may want to rename the tables and columns in Airtable with underscores instead of spaces, and refresh your Airtable collections in WeWeb before doing the import in Xano.

