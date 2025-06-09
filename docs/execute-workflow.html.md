# Project workflows ​


# Project workflows ​

Project workflows allow you to create reusable workflows that can be triggered from within any other workflow in your application. When adding an action to any workflow, you can find all project workflows in a dedicated "Project workflows" section of the action menu.

This feature is useful for:

- Creating reusable workflow logic across different parts of your application
- Breaking down complex workflows into smaller, manageable pieces
- Keeping your workflows organized and maintainable

By breaking down complex logic into reusable project workflows, you can build powerful, scalable features that can be easily reused across your application.


## How to Use ​


### Creating a Project Workflow ​

First, create a reusable project workflow:

- Go to the Logic tab in the left panel
- Click + New to create a new global workflow
- Give your workflow a name
- Set up the workflow with the actions you want to make reusable
- Add parameters if needed (optional)

`Logic`
`+ New`


For example, to create a project workflow that logs a message to the console:

- Add a Log action
- Access the Events tab to retrieve your defined workflow parameters

`Log`
`Events`



### Executing a Project Workflow ​

When you want to use your global workflow within another workflow:

- In your local workflow, add a new action
- Look for the Project workflows section in the action list
- Select the project workflow you want to execute from the list

`Project workflows`
- Provide any required parameters for the selected workflow



When your local workflow runs, it will execute the project workflow as part of its sequence:



TIP

Use project workflows whenever you find yourself repeating the same series of actions in different places, or when a workflow becomes too complex to manage. This approach helps keep your application maintainable and reduces duplication.

