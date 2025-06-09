# React to realtime database changes ​


# React to realtime database changes ​


## Pre-requisites ​

Before users of your WeWeb app can listen and react to Supabase realtime database changes, there are two pre-requisites:

- In Supabase, enable realtime on the table you want to monitor.
- In a WeWeb workflow, subscribe to a realtime channel where message events can come and go.

Please refer to the related documentation if you haven't done so already.

Once that's done, you can think of reacting to database changes.


## Listen for database changes ​

If we want users in the channel to receive database change events, we need to create a page or app workflow that is triggered when there's a new realtime database change event in a channel.

`database change`
WARNING

Workflows that listen to realtime events must be executed at page or app level because you are essentially saying: when this app or this specific page is open in a browser, I want the browser to listen for events so it can react to it.

In the example below, we setup a workflow on a page that updates a notification counter:

- The workflow listens for realtime Database changes.
- It is triggered every time there's an INSERT event in the releases channel we subscribed to previously.
- Every time there's such a new event, we update a variable in our app.

`Database changes`
`INSERT`
`releases`


WARNING

Note that users will only receive events of channels they have subscribed to. If the user has not subscribed to the releases channel, the workflow will not be triggered.

`releases`
