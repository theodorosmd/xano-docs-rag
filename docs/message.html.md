# Send & receive messages (Xano realtime) ​


# Send & receive messages (Xano realtime) ​


## Pre-requisites ​

Before users of your WeWeb app can send and receive Xano realtime messages, you need to:

- Enable and connect Xano realtime to your WeWeb project (as explained here).
- Open a channel where messages will flow (as explained here).

Once that's done, you can think of sending & receiving messages.


## Send messages ​

To send messages to a realtime channel, we need to use the Send message action.

`Send message`
In the example below, we created a workflow that sends a message to Everyone in the room1 channel when a user clicks on the "Send" button of a support chat:

`Everyone`
`room1`


TIP

Notice how you can customize the message event. In the example above, we sent an object with information about the user in addition to the chat input variable.

The only thing the Send message action does is send information to the channel.

`Send message`
If you test the action and get an error, it means the user is not subscribed to the channel:



Otherwise, Xano will return a simple success message:



That's because receiving (and displaying) messages is a separate matter.


## Receive messages ​

To receive realtime messages from other users, we need to create a page or app workflow that is triggered when there's a new realtime message event in a channel.

`message`
WARNING

Workflows that listen to realtime events must be executed at page or app level because you are essentially saying: when this app or this specific page is open in a browser, I want the browser to listen for events so it can react to it.

In the example below, we setup a workflow on a page with a chatroom:

- The workflow is triggered when there's a new message event in the room1 channel.
- To help us debug things, we used the Logs action and bound it to the entire workflow Event object.
- Then we updated a variable with the payload of the workflow Event.

`message`
`room1`
`Logs`
`Event`
`payload`
`Event`


TIP

Note that, the preview of the Event object and event payload in the workflow editor displays placeholder information.

`Event`
`payload`
When you test your setup in preview mode, the payload of the message event you receive here will match the Payload value you defined when you created the Send a message action before:

`payload`
`Payload`
`Send a message`



## Display message events ​

To display message events in your WeWeb app, you can update a WeWeb variable every time there's a new event and bind that variable to an item (or list of items) on your page.

That way, your UI can react dynamically to the event it receives.


### Live collaboration example ​

For example, in the case of a live collaboration tool that tracks every user's cursor position, you might have a cursors array variable with a seperate objet for every active user.

`cursors`
Each object would include the user's cursor position.

On your page, you could use that variable to move cursor icons around the page based on each user's position.



In the example above, you can see the page is open in three different clients (user browser tabs) and client A can see the cursor position of clients B and C.

