# Encode file as Base64 ​


# Encode file as Base64 ​


## What is it for ​

The Encode file as Base64 allows you to:

`Encode file as Base64`
- take a file that was uploaded by a user, and,
- encode in the Data URL or Base64 format.

Depending on your use case you will choose one output type or another.

The Encode file as Base64 is very useful if you want to upload files directly to your backend without going through WeWeb's CDN, and without resorting to custom code.

`Encode file as Base64`

## How it works ​

In the example below, we created a workflow on a file upload element:

- added the Encode file as Base64 action,
- decided what file we wanted to encode by selecting the component variable of our file upload element,
- chose to receive the encoded file in Data URL, and
- tested the action to see the result of the action

`Encode file as Base64`
`Data URL`


Then we made a couple of requests to our backend to upload the file there and create a new record in one of our database tables.

TIP

The requests you make in your workflow and the format you choose for the output of the Encode file as Base64 action will depend on what you need to do with the file afterwards or where you want to send it.

`Encode file as Base64`
In the example below, we show you how to use it to upload a file directly to Xano:

