# Load more button ​


# Load more button ​

A simple way to paginate a collection is to use the Paginator element.

Another way is to add a button on the page with a workflow to load more items from your collection every time a user clicks on the button.


## Step 1: Add a button ​

Drag-and-drop a Button on the Canvas or Navigator, wherever you want to display it on the Page.

In the example below, we placed it below our list of calls:




## Step 2: Create a variable ​

This Variable will be called loadMore and of type Number.

`loadMore`
`Number`
Its default value will be the number of items you want to display on the page by default.

In the example below, we want to display 5 items by default.




## Step 3: Add a workflow ​

On the button you created in step 1, add a workflow to Change variable value of the variable you created in step 2.

`Change variable value`
In the example below, we are saying:

- when the user clicks on the button,
- add 5 to the loadMore variable

`loadMore`
As a result, every time a user clicks on the button, the loadMore variable will be incremented by 5:

`loadMore`



## Step 4: Link the collection to the variable ​

Now, when we bind our Collection List, we need to tell the browser to display the number of items in the loadMore variable we defined in step 2.

`loadMore`
In order to do that, we have to slice our list:

`slice`


WARNING

The slice formula is an Array function so you need to bind to your collection['data']. If you bind to collection, it will not work because you are binding to an Object.

`slice`
`collection['data']`
`collection`
In the screenshot above, we see that:

- we are binding to a list of items calls['data'] instead of the entire collection object calls
- we are using the slice no-code formula to display the items from index 0 to the index X
- X changes based on the value of the loadMore variable, which changes every time the user clicks on the button (see step 3)

`calls['data']`
`calls`
`slice`
`loadMore`

## Step 5: Test in Preview ​

Ok, that should work.

Back in Preview mode, you can click on the button to see the loadMore variable be updated in the Navigator and the additional items displayed on the page:

`loadMore`
