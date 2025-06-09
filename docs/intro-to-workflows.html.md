# Intro to workflows ​

Academy

Want to learn how to add business logic to your WeWeb app? Check out our Build a proof of concept course for a comprehensive look at creating interactive experiences with workflows in WeWeb.


# Intro to workflows ​

Workflows are sequences of actions that automate tasks in your WeWeb application. They allow you to create dynamic, interactive experiences by defining what happens when specific events occur - such as a user clicking a button, submitting a form, or when a page loads.


## Understanding workflows ​

Every workflow consists of two main components:

- trigger - the event that starts the workflow (e.g., a button click, page load, or form submission)
- actions - the sequence of steps that WeWeb performs when the trigger occurs

For example, when a user submits a sign in form (On submit) trigger, you might want to:

`On submit`
- sign the user in
- check their role
- navigate them to the appropriate page


## Creating your first workflow ​

To create a local workflow:

In this example:

- we select an element (in this case, a button)
- create a new workflow on the element
- select the trigger to use (On click)
- define the actions (increment the value of our Counter Value variable)
- test the workflow in Preview mode (with the live value of the variable open in the Debug panel)

`On click`
`Counter Value`
`Preview`
`Debug`

## Types of workflows in WeWeb ​

WeWeb offers four different types of workflows, each with its own scope and purpose:


### Local workflows ​

Local workflows are attached to specific elements and are triggered by interactions with those elements. They're perfect for handling element-specific actions, like validating input fields or toggling visibility.


### Project workflows ​

Project workflows are defined once in the Logic tab and can be reused throughout your application. They help you maintain consistency and reduce duplication by centralizing common workflow logic.

`Logic`
Project workflows are ideal for:

- complex logic that needs to be reused in multiple places
- standardized processes like user authentication or data validation
- workflows that might need to be updated across your application

TIP

When you find yourself creating similar workflows in multiple places, consider converting them to project workflows. This makes maintenance easier and ensures consistent behavior throughout your application.

Learn more about how to create and reuse project workflows


### Page workflows ​

Page workflows apply to an entire page and can be triggered by page-level events such as page load or page scroll. They're useful for page-specific initialization or cleanup tasks.

To access page workflows:

- select the desired page in the page navigator
- go to page settings
- click on Trigger page workflows

`Trigger page workflows`
Page workflows are especially useful for:

- loading data when a page initializes
- setting up page-specific variables
- tracking page views
- performing clean-up when a user leaves a page


### App workflows ​

App workflows operate at the application level and run across your entire website. They're ideal for site-wide functionality like authentication checks or analytics tracking.

To access app workflows:

- click on More in the top navigation
- select Trigger app workflows

`More`
`Trigger app workflows`
App workflows are perfect for:

- global authentication checks
- site-wide analytics
- user preference management
- feature flags and site-wide settings


## Managing workflows ​

As your application grows, managing workflows becomes increasingly important:


### Finding project workflows ​

To see if a project workflow is used on a specific page:

- go to the Logic tab
- toggle the "All pages" switch to filter by the current page

`Logic`
This helps you track where workflows are being used and ensures you don't accidentally break functionality when making changes.


### Naming conventions ​

Always use clear, descriptive names for your workflows:

✅ Good: "ValidateUserInput", "SendWelcomeEmail", "UpdateCartTotal" ❌ Bad: "NewWorkflow", "Workflow1", "MyWorkflow"

Consistent naming makes debugging easier and improves team collaboration.


## Best practices for workflows ​

- keep workflows focused - each workflow should handle a specific task
- use project workflows for reusable logic - if you find yourself duplicating workflows, create a project version
- error handling - set up error workflows to gracefully handle failures
- testing - use the Debug panel to verify your workflows behave as expected
- documentation - add comments to complex workflows to explain their purpose

`Debug`
FRONTEND LIMITATIONS

WeWeb is a frontend builder, so workflows run in the user's browser. For recurring tasks (like scheduled jobs) or operations that should continue after the user closes their browser, you should use a proper backend service.

CONTINUE LEARNING

Ready to dive deeper into workflows? Learn about the different types of triggers available:

Learn about triggers →

