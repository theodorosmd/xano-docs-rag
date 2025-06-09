# Return a value ​


# Return a value ​

The Return a value action passes data forward in your workflow - it is much like a variable, however it is only momentarily stored for the run of the workflow. The returned value can then be accessed via the 'result' field of the workflow action.

`Return a value`

## How it works ​

- Add a Return a value action to your workflow
- Set the value you want to return

Add a Return a value action to your workflow

`Return a value`
Set the value you want to return



In subsequent actions, access the returned value via the 'result' field of the workflow action:



While this is a dedicated action for returning values, other actions like Custom JavaScript can also make data available via its respective 'result' field through their return statements.

TIP

This action provides a clean way to pass processed data back when used in reusable workflows that are executed within other workflows. It's also useful for storing intermediate results that you need to use in later steps of your workflow, making your data flow clearer and more organized.

