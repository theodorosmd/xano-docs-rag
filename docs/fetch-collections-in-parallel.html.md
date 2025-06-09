# Fetch collections in parallel ​


# Fetch collections in parallel ​

The Fetch collections in parallel action allows you to trigger multiple collection fetches simultaneously in WeWeb. Unlike the basic Fetch collection action which handles one collection at a time, this action lets you select multiple collections that should be fetched concurrently. When triggered, it makes fresh requests to your data sources in parallel and updates all selected collections with their latest data.

`Fetch collections in parallel`
`Fetch collection`
Imagine you're building a dashboard page that needs to show:

- A list of recent orders
- Current inventory levels
- Customer reviews
- Sales statistics

Without parallel fetching, the requests works sequentially, like this:

- Get orders
- Once orders retrieved, THEN get inventory
- Once inventory retrieved, THEN get reviews
- Once reviews retrieved, THEN get sales

Total: If each retrieval took 1 second, then it would take 4 seconds to load everything.

With parallel fetching, these requests would happen simultaneously:

- Get orders
- Get inventory
- Get reviews
- Get sales

Total: If each retrieval took 1 second, then it would only take 1 second to load everything as all the requests would happen at the same time.

So instead of waiting for each piece of data one after another (which takes longer), parallel fetching gets all the data at once. This is akin to Promise.all() in JavaScript.

`Promise.all()`
TIP

While parallel fetching can significantly improve performance, actual loading times depend on various factors such as your backend server capacity, API rate limits, network conditions, and the complexity of your data queries. Monitor your application's performance to ensure optimal results.

