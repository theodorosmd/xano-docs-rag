# Broadcast messages with Supabase realtime ​


# Broadcast messages with Supabase realtime ​


## Pre-requisites ​

Before users of your WeWeb app can send and receive Supabase realtime broadcast messages, they need to subscribe to a realtime broadcast channel.

Once that's done, they can start sending & receiving realtime broadcast messages.


## Broadcast a message ​

To allow users to send messages in a channel, use the Broadcast a message action:

`Broadcast a message`


In the example above, you can see:

- We triggered the Broadcast a message action.
- To send a message to a channel we named room1.
- We said these messages should be called a chat event.
- We configured the payload of the event to be an object with the user's name and the text from a chat input.

`Broadcast a message`
`room1`
`chat`
Note that the Event name can be whatever you like. It's important you remember it if you want to filter on specific events later, when you start listening and reacting to events.

`Event`
WARNING

The Channel name should match a channel that the user already subscribed to.

`Channel`


When the Broadcast a message action is successful, the workflow Logs will simply inform you that the message was sent:

`Broadcast a message`
`Logs`


The action sends the realtime event to the channel but that's it.

Receiving (and displaying) messages is a separate matter.


## Receive broadcast events ​

If we want users in the channel to receive messages from other users, we need to create a page or app workflow that is triggered when there's a new realtime broadcast event in a channel.

`broadcast`
WARNING

Workflows that listen to realtime events must be executed at page or app level because you are essentially saying: when this app or this specific page is open in a browser, I want the browser to listen for events so it can react to it.

In the example below, we setup a workflow on a page with a chatroom:

- The workflow is triggered when there's a new broadcast event in the room1 channel.
- To help us debug things, we used the Logs action and bound it to the entire workflow Event object.
- Then we updated a variable with the payload of the workflow Event.

`broadcast`
`room1`
`Logs`
`Event`
`payload`
`Event`


TIP

Note that, the preview of the Event object and event payload in the workflow editor displays placeholder information.

`Event`
`payload`
When you test your setup in preview mode, the payload of the broadcast event you receive here will match the Payload value you defined when you created the Broadcast a message action before:

`payload`
`Payload`
`Broadcast a message`



## Display broadcast events ​

Broadcast events are ephemereal by design (see Supabase docs on the topic).

To display these events in your WeWeb app, you'll want to update a variable every time there's a new event and bind that variable to an item on your page. That way, your UI can react dynamically to the event it receives.

For example, in the case of a live collaboration tool that tracks cursor positions, you might have a cursors array variable with a seperate objet for every active user. Each object would include the user's cursor position. On your page, you could use that variable to move cursor icons around the page based on each user's position.

`cursors`

## Realtime debugger ​

In Supabase, you can open the Realtime page to check if messages go through ok:

`Realtime`


