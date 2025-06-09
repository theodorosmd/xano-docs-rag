# Log ​


# Log ​

The Log action is a debugging and monitoring tool that outputs messages to the Logs tab

`Log`

## Configuration ​

Name: you can give your log action a name for better organization in your workflow. This is optional but helpful when managing multiple log actions.

`Name`

### Type ​

The log type determines how your message appears in the console:

- Info: for standard log messages
- Verbose: for detailed debugging information
- Warning: for potential issues that need attention
- Error: for critical problems and errors
- Message: enter the text you want to output to the console. This is required and can be a static message or a dynamic value from your workflow.
- Data to display: optionally include additional data alongside your message. This could be variable values, API responses, or any other data you need to monitor. The data can be input as JSON or JavaScript expressions.

Info: for standard log messages

`Info`
Verbose: for detailed debugging information

`Verbose`
Warning: for potential issues that need attention

`Warning`
Error: for critical problems and errors

`Error`
Message: enter the text you want to output to the console. This is required and can be a static message or a dynamic value from your workflow.

`Message`
Data to display: optionally include additional data alongside your message. This could be variable values, API responses, or any other data you need to monitor. The data can be input as JSON or JavaScript expressions.

`Data to display`

## Common applications ​

When building, you might use logs to track API responses, verify calculations, or monitor user interactions. For example, placing a Log action after a button click can confirm the click was registered and show what data was captured.

`Log`
When debugging complex workflows, logs help verify that actions are executing in the expected order and that variables contain the correct values at each step. They're particularly useful for tracking data transformations and catching potential issues before they cause problems.

In error scenarios, log actions can capture and display detailed error information, making it easier to identify and fix issues in your application.

