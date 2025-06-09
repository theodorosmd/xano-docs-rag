# Get channel history ​


# Get channel history ​

The Realtime | Request history action allows you to access past conversations or data exchanges that occurred in the channel before the current user joined or connected.

`Realtime | Request history`
It's useful for providing context in chat applications, showing recent updates in collaborative tools, or displaying a backlog of events in real-time systems.


## Pre-requisite ​

In order to get history, we first need to enable Message History in the settings of our Xano Realtime channel settings:

`Message History`


Xano can retrieve up to 1,000 of the most recent messages per channel when accessing Message History. For our demo example, you can select any number of messages available on the list.


## Overview ​

Now we want our users to see past messages from other users once they join our chatroom. To achieve this, we will:

- add a Request history action
- create a workflow to listen for the history event type
- process history data to extract messages
- merge historical messages with current messages
- update UI to display combined message history

`Request history`
`history`

## Request history action ​

In your Realtime | Open channel action, set Get history on join to On. This will enable new users to see past messages when they join:

`Realtime | Open channel action`
`Get history on join`
`On`


Add the Realtime | Request history action after your Open channel action, provide the channel name, and test the action:

`Realtime | Request history`
`Open channel`


We can see the Request History action succeeded, but where exactly is the history data?

`Request History`
The Request history action doesn't immediately give you the message history. Instead, it asks Xano to prepare the history. Once ready, Xano sends this history through a separate history event, which we need to listen for to receive and use the historical messages.

`history`

## Listen for history events ​

`history`
To ensure we can access our requested history, we can create a new page or app workflow that listens for the history event:



WARNING

Workflows that listen to realtime events must be executed at page or app level because you are essentially saying: when this app or this specific page is open in a browser, I want the browser to listen for events so it can react to it.

This workflow will listen to history events from the selected Xano channel.

`history`
We can store information from this event in a WeWeb variable and display it in our UI.

In the example below, we created a history array variable and saved the history part of the event we received from Xano:

`history`
`history`


We can then use our WeWeb variable to display history data in our UI in whichever way we like.

TIP

Note that the history array sent by Xano contains a lot of information that you may or may not need, depending on your use case: 

`history`
Feel free to tweak what you save to the WeWeb variable to adjust to your needs.

