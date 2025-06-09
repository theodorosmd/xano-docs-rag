# Reset variable value ​


# Reset variable value ​

The Reset variable value action allows you to reset a variable back to its default value. This action is useful when you need to clear or restore a variable to its starting state.

`Reset variable value`

## Use cases ​

- Form handling: reset form fields after submission
- Counter reset: return counters or incrementors back to their starting value
- State management: clear temporary states or flags after they're no longer needed
- Filter reset: clear applied filters back to their default values
- Navigation: reset page-specific variables when leaving a page


## How to use ​

- Select the Reset variable value action
- Choose the variable you want to reset

`Reset variable value`
The variable will return to its default value when the action is triggered

TIP

Use this action in combination with other workflow actions to create clean state management in your application. For example, after processing a form submission, you can reset all form variables to create a fresh start for the next entry.

WARNING

You shouldn’t trigger workflows on submit buttons. For your users to benefit from automatic form field validation, you should trigger submit workflows on the form container. Unless you are 100% sure of what you’re doing and want to bypass this behavior.

