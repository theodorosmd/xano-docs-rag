# Xano request action ​


# Xano request action ​

When you add the Xano data source plugin to a WeWeb project, it unlocks the Xano Request action in workflows.

`Request`

## Request action ​

The Xano Request action in workflows allows you to make requests to the endpoints of the Xano instance you configured in WeWeb's Xano data source plugin:

`Request`


In the example above, you can see that we are configuring a call to:

- the POST poems endpoint,
- in the library API group of our Xano instance.

`POST poems`
`library`
This endpoint includes 3 inputs – poem, title, and author – which I bound to input variables from my WeWeb project.

`poem`
`title`
`author`
As a result, the values I send to Xano will vary based on the values in my WeWeb variables.


## Streaming ​

A streaming response in Xano is a method of data transfer where information is sent and processed in chunks, rather than all at once. In the context of APIs, it means sending parts of the response to the client as they become available, instead of waiting for the entire response to be ready before sending anything.

✅ Common use cases include:

- AI chatbots.
- Large datasets.
- Real-time updates.
- Long-running operations.
- Improve perceived performance.

❌ When not to use streaming:

- small responses.
- Client limitations.
- Simple CRUD operations.
- Atomic operations (when the entire operation needs to succeed or fail as a unit, streaming partial results might not be appropriate).


### Pre-requisites ​

To work with a streaming response from Xano in WeWeb, you will first need to create a streaming API endpoint in Xano.

To set up your streaming API endpoint in Xano, we strongly recommend that you watch their video on “Streaming API Responses with Xano“:


### Request settings in WeWeb ​

To receive a streaming response from Xano in WeWeb, you'll need to trigger a standard Xano Request action in a WeWeb workflow and ensure two things:

`Request`
- The option Stream response is enabled.
- You created (and selected) a WeWeb array variable where you can store the streaming response.

`Stream response`


When we test the action, we can see our stream variable being updated line by line:

`stream`


This is because, in Xano, our variable was an array of lines. When we looped through the variable, each item was a line:



If we wanted to stream the response character by character, we would need to change the function stack of our Xano endpoint so each item is a character.

In the example below, instead of having an array variable in Xano formatted as a raw JSON, we have a strong variable and applied a split function to return the text as an array of character:

`split`


Here's what it would look like in action:



