# Create URL from Base64 ​


# Create URL from Base64 ​

If your backend returns a file in Base64, you can use the Create URL from Base64 action to transform this file into an object URL that you can more easily work with.

`Create URL from Base64`
You can then use that object URL to reference that file in your app, allowing users to download it or preview it on the page of your app for example.


## Input ​

In the example below, our backend returns an image in Base64 but the info looks like this and is unreadable as is:




## Output ​

We can use the Create URL from Base64 action in a workflow to transform the Base64 into a object URL:

`Create URL from Base64`


The result from this action is an object URL:



We can use this object URL to reference the file in our app so that users can download it or see it on the page.


## Example ​

In the example below, we bound the object URL to an image element to display the image in our app:



