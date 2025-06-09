# REST API data source ​


# REST API data source ​


## Add plugin ​

To work with external APIs that don't have a native WeWeb integration, you can go to Plugins > Data sources > REST API:

`Plugins`
`Data sources`
`REST API`


There is no configuration required.


## Make API calls ​

Once you have added the REST API plugin to a WeWeb project, you will be able to:

- create a data collection that fetches data from a REST API
- create a workflow that makes an API request

TIP

We recommend using collections when you are fetching data that might need to be filtered and paginated.

To make an API call that creates, updates, or deletes a record, you will need to create a workflow.


## Security ​

When you make an API call with the REST API plugin in WeWeb the request is made by your application (i.e. client-side request from the frontend, your browser).

You should never use private API keys in REST API calls made through the client.

Learn more about public and private API keys.


## Create a collection ​

To get and display data sets that might need to be filtered or paginated, you can create a collection in WeWeb.

In the example below, we fetched a list of characters from the Rick & Morty API:



You can see that:

- in the Data tab,
- we clicked on New to create a new collection,
- we gave it a name and chose REST API as a data source,
- we configured our API calls as we would in tools like Postman
- we have options to filter and paginate the collection in the frontend, decide when the collection will be fetched, and if we want it to be preserved on navigation

`Data`
`New`
`REST API`
WARNING

WeWeb's REST API plugin only accepts HTTPS requests. If you're trying to follow this tutorial with a public API that uses HTTP requests, WeWeb will return an error message.


### Headers ​

If your data can only be accessed by authenticated users, don't forget to add Authorization headers to your API call and login as a user of your WeWeb app. Otherwise, the API will return an error when you try to create the collection.

`Authorization`

### Result key ​

Sometimes, APIs will return the data you need in a nested object. When that happens, it can be helpful to use the Result key field to fetch only the information you need.

`Result key`
For example, when we get a list of characters from the Rick & Morty API, the API returns two objets:

- info, with info that we could use to setup backend pagination, and
- results, with a list of Rick & Morty characters.

`info`
`results`
If we don't intend to setup backend pagination on that collection, the info object is useless to us and adds uneccessary complexity when working with this data set.

`info`
To access the information inside the results object directly, we can add results as a value in our Result key field:

`results`
`results`
`Result key`


TIP

This is not a WeWeb specific practice. In web development, you always want to avoid fetching data you don't need.


## API calls in workflows ​

Once you've added the REST API plugin to your project, you will have access to the REST API Request action.

`REST API Request`
In the example below, you can see we:

- chose the REST API Request action type,
- decided to make a POST request,
- entered the URL or our endpoint,
- bound the name of two fields to update with values, and
- configured authorization headers to tell our API who is making the call

`REST API Request`
`POST`



## Resolving CORS Issues ​

When you make an API call in WeWeb the request is made by your application (i.e. client-side request from the frontend, your browser).

But sometimes, APIs only accept requests that come from a server (i.e. server-side requests from the backend) and return CORS errors. This is the case for the Twitter API for example.

You can bypass CORS issues by enabling the Proxy the request to bypass CORS issues option on your API call:

`Proxy the request to bypass CORS issues`


WARNING

When you enable the Proxy the request to bypass CORS issues option, WeWeb will proxy the request to bypass CORS errors but the information will still be visible in the client.

`Proxy the request to bypass CORS issues`
This option is not meant to keep private tokens private. You should never use private API keys in REST API calls made through the client.


## Debugging API Requests ​

When you start working with APIs, you'll run into a lot of errors.

It's completely normal and nothing to worry about 🙂

WeWeb will display error messages to help you figure out what went wrong.

The top 4 reasons for errors are:

- you're trying to make an http request when WeWeb only accepts https requests
- the API you are working doesn't accept client-side requests (see "Resolving CORS issues" section above)
- you are trying to get or udpate data that is protected in your backend but you are not logged in as an authorized user to get or update this data
- you are sending data to the API in a format it does not recognize. For example, trying to update an integer field but sending a string.

`http`
`https`
Learn more about debugging API requests.

