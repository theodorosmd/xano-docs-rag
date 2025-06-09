# Subscribe & unsubscribe to a Supabase channel ​


# Subscribe & unsubscribe to a Supabase channel ​


## Why subscribing matters ​

If you want users of your app to be able to listen and react to events in a realtime channel, you first need to make them subscribe to the channel.

✈️ Realtime events are like flying objects ☄️

You can picture a user subscribing to a realtime channel as someone who is entering a room where a bunch of objects (events) are flying around.

If the user is in the room, they can see and intercept these objects. If the user is outside the room (unsubscribed), they can't see or react to anything.


## Use cases ​

A few use cases:

- When user clicks on help icon, they subscribe to the chat channel where instant messages come and go.
- When user signs up to the app, they subscribe to the releases channel where new events are created every time a new product update is inserted in the database.
- When user opens a tab, they subscribe to the cursor channel where new events are created with their mouse position every time their mouse moves.

`chat`
`releases`
`cursor`

## Two types of channels ​

There are two types of Supabase realtime channels users can subscribe to:

- Broadcast: Send ephemeral messages from client to clients with low latency. For example, to track users' cursors in a collaborative tool.
- Postgres Changes: Listen to Postgres database changes and send them to authorized clients. For example, to notify users of a new comment in one of their projects.


## Subscribe to broadcast ​

There are use cases where you don't need to store realtime events in a database. For example, live collaboration tools or online games that track every active user's cursor position.

For users to send and receive realtime cursor positions, they first need to subscribe to a realtime Broadcast channel:

`Broadcast`


The Channel name can be anything you want. Here we named it canvas. It's the name we will need to reference later when we want to send and receive messages in this channel.

`Channel`
`canvas`
The Type is Broadcast because we are working with ephemereal events that don't need to be stored in our database.

`Type`
`Broadcast`
We chose to subscribe to only the cursor events because we only want to listen to this specific event type but we could leave the input empty or type in * to subscribe to all the events that go through this channel. What you choose will depend on your use case.

`cursor`
`*`
The Listen self and Listen presence can be toggled on or off depending on your preferences and use case.

`Listen self`
`Listen presence`
Learn more about these options here in the Supabase user docs.


### Next steps ​

Once we have subscribed to a Broadcast channel, we can send, receive and react to realtime events from that channel.

`Broadcast`

## Subscribe to db changes ​

WARNING

Users can only subscribe to a channel that listens to database changes if you have enabled realtime on the table that you want to monitor:



In many cases, you want users to be able to receive and react to realtime changes in a database. For example, when someone at your company adds a record in the releases table of your database, you want to let users know there's a new product update.

`releases`
For users to send and receive realtime database events, they first need to subscribe to a Database changes channel:

`Database changes`


In the example above, you can see the user is subscribing to:

- All events
- in the releases table
- that can be found in the public schema of my Supabase db

`All events`
`releases`
`public`
The Channel name can be anything you want. Here we named it releases. It's the name we will need to reference later when we want to send and receive events in this channel.

`Channel`
`releases`
TIP

We chose to subscribe to All events but we could have decided to subscribe only to INSERT events for example. What you choose will depend on your use case.

`All events`
`INSERT`
We could also use the Filter input to refine the subscription further. Learn more about filtering for specific changes here.

`Filter`
The Listen presence can be toggled on or off depending on your preferences and use case.

`Listen presence`

### Next steps ​

Once we have subscribed to a Database changes channel, we can receive and react to realtime events from that channel.

`Database changes`
