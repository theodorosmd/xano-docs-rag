# Presence state in Supabase realtime ​


# Presence state in Supabase realtime ​


## What is presence? ​

When working with realtime, it's often useful to receive and display information about online users. Enter "presence".

Presence is what allows you to see who is present in a realtime channel.

If you’re building a collaborative tool, for instance, presence allows you to see who is actively editing or viewing a document:



If you are building a message board or a game, it allows users to see who is available to join a game or who is actively participating.

Ultimately, the choice of using presence depends on your specific use case.


## Presence in Supabase ​

To get information about presence in a Supabase channel, you will need to listen for Supabase presence events via a page or app workflow:



TIP

Depending on your use case, you may choose to listen to only specific type of presence events:

`presence`
- sync
- leave
- join

`sync`
`leave`
`join`
In the example above, you can see:

- We are listening to all presence events in the room1 channel.
- We used the Log action to log a presence message in case we need to debug things.
- We use branches to update a number variable called supabaseOnlineUsers: If Supabase sends a join event, we add 1 to our active user count.If Supabase sends a leave event, we remove 1 from our active user count.
- If Supabase sends a join event, we add 1 to our active user count.
- If Supabase sends a leave event, we remove 1 from our active user count.

`room1`
`Log`
`supabaseOnlineUsers`
- If Supabase sends a join event, we add 1 to our active user count.
- If Supabase sends a leave event, we remove 1 from our active user count.

`join`
`leave`
On our UI, we can easily bind the supabaseOnlineUsers value to a text element to display the number of active users:

`supabaseOnlineUsers`



## Debugging ​

When working with event listeners, we highly recommend getting into the habit of adding a Log action that's bound to the Event you receive from Supabase:

`Log`
`Event`


This is helpful because it allows you to see the event as it comes in.

In the example above, despite only one user joining the channel, the workflow was triggered twice. That's because, when a user joins a channel, Supabase triggers two presence events: first a join event, followed by a sync event.

`join`
`sync`
If we didn't see that information in the logs, we might have been confused and counted two users instead of one.

