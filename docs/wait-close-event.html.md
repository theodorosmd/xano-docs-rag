# Using Wait Close Event ​


# Using Wait Close Event ​

The Wait close event feature in WeWeb's popup system is a powerful tool that allows your workflows to pause and wait for a popup to be closed before continuing. This creates more interactive and sequential user experiences where you can gather input from a popup and then act on that input in your original workflow.

`Wait close event`

## Understanding Wait Close Event ​

When you open a popup using the Open popup action in a workflow, you have the option to enable Wait close event:

`Open popup`
`Wait close event`

### How it works ​

- Your workflow reaches the Open popup action with Wait close event enabled
- The popup opens for the user
- Your workflow pauses at this point
- The user interacts with the popup and eventually closes it
- Your workflow resumes after the popup is closed

`Open popup`
`Wait close event`
This is different from the default behavior, where the workflow would execute all actions immediately after the trigger.


## Returning values from popups ​

One of the most powerful aspects of Wait close event is the ability to return values from the popup back to the original workflow.

`Wait close event`

### Setting up return values ​

In your popup:

- create a workflow on an element in the popup
- add a Close this popup instance action to the workflow
- in the data field of the action, add the information you want to return to the original workflow that opens the popup

`Close this popup instance`
`data`

### Accessing return values ​

- run your close workflow that passes data at least once
- navigate to your original workflow that opens the popup
- now, in any subsequent actions, you will be able to access the data returned from the popup


## Common use cases ​


### Confirmation dialogs ​

A classic use case is creating a confirmation dialog:

- user clicks "Delete" button on a customer record
- workflow opens a confirmation popup with Wait close event enabled
- user clicks "Delete" or "Cancel" in the popup
- popup closes with data indicating the choice and customer to delete
- original workflow continues and proceeds with deletion using the passed customer data if the condition to delete is met

`Wait close event`
