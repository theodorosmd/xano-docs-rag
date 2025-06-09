# Adding interactivity to your app ​


# Adding interactivity to your app ​

After adding elements to your page and styling them, the next step is to make your app interactive. Interactivity is what transforms a static webpage into a dynamic application that responds to user actions.


## The building blocks of interactivity ​

Creating interactive experiences in WeWeb involves three key components:

- variables - store and track changing information
- workflows - execute a set of actions when a trigger occurs, like a button click or hovering over an element
- binding - connect your variables to visual elements

Let's explore each of these components and how they work together.


## Creating variables ​

Variables are containers that store information in your application. They allow you to keep track of changing data, like:

- a user's name or account details
- the number of items in a shopping cart
- whether a dropdown menu is open or closed
- the current step in a multi-step form


### How to create a variable ​

Here's a short interactive tutorial on creating a variable:

The steps are:

- open the Data tab in the left panel
- click New in the Variables section
- give your variable a name
- choose a variable type (Text, Number, Boolean, etc.)
- optionally set a default value
- decide if you want the variable preserved on navigation or saved in local storage
- click Create

`Data`
`New`
`Variables`
`Create`

### Common variable types ​

- text - for storing words, names, descriptions
- number - for counters, prices, quantities
- boolean - for true/false states (on/off, visible/hidden)
- object - for storing complex grouped data, like a user's information
- array - for lists of items

Learn more about variables →


## Binding properties to create dynamic experiences ​

Binding connects your variables (or collections) to your UI elements, creating dynamic experiences that change based on user interactions or data.


### How to bind properties ​

To bind a property in WeWeb, click on the plug icon beside the property:

You'll then see the formula window, where you can bind any formula or data:

Here's an interactive example of binding a text element to display a user's name:


### Binding styling properties ​

You can also bind styling properties to create visual feedback based on data or user interactions. Here's an example of conditionally displaying a warning message:


### What you can bind ​

Almost any property in WeWeb can be bound to variables:

- content - change text, images, or other content
- styling - modify colors, sizes, or visibility
- repeating items - show multiple elements from a list

VISUALLY IDENTIFYING BOUND PROPERTIES

Bound properties can always be identified by their purple visual appearance:

OR

You can also identify when an element has a bound property, as it will have a plug icon beside it in the layout tree:


## Advanced example: styling based on user input ​

Here's a more complex example where we change the background color of an input field based on password length:

In this example, we're using WeWeb AI to create a binding that changes the input's background color to green when the password is long enough and red when it's too short.

Learn more about binding →


## Using formulas to transform data ​

Formulas are powerful tools that allow you to manipulate and transform data in your application. They act as the logic layer between your data and how it's displayed or used.


### What are formulas? ​

Formulas in WeWeb let you:

- transform data (like formatting text, dates, or numbers)
- create conditional logic (if/else statements)
- perform calculations
- combine multiple pieces of data

To use formulas:

- open any binding menu by clicking the plug icon
- navigate to the formulas tab
- select from available formulas or write custom JavaScript

`formulas`

### Examples of formula use ​

- displaying a user's full name by combining first and last name
- showing "In stock" or "Out of stock" based on inventory numbers
- formatting currency values properly
- calculating totals or percentages

Formulas can be used directly in bindings, or created as global formulas to reuse throughout your application.

Learn more about formulas →


## Building workflows ​

Workflows define what happens when users interact with your app. They consist of triggers (what starts the workflow) and actions (what happens next).


### Creating a simple workflow ​

Here's an interactive tutorial on creating a workflow, where:

- we select an element (a button)
- create a new workflow on the element
- select the trigger to use (On click)
- define the actions (increment a counter variable)
- test the workflow in Preview mode

`On click`

### Common triggers ​

- on click - when an element is clicked
- on change - when text is entered in an input
- on submit - when a form is submitted


### Common actions ​

- change variable value - change a variable's value
- navigate to page - go to another page
- fetch collection - retrieve data

Learn more about workflows →


## Best practices for interactive elements ​

When adding interactivity to your WeWeb app:

- use descriptive variable names that clearly indicate what they store
- provide visual feedback to users when their actions trigger changes in the app
- test your interactions frequently to ensure they work as expected
- use global workflows for functionality you'll reuse across your app

CONTINUE LEARNING

Now that you know how to add basic interactivity to your app, learn how to choose the right backend for your application:

Choosing a backend →

