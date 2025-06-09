# Binding styling properties ​


# Binding styling properties ​

Along with directly displaying data via bindings, you can also bind the values of styling properties. This allows you to create dynamic visual effects based on data or user interactions.


## Display example ​

In the example below, we have a warning in our login form that we only want to display when the terms and conditions checkbox is ticked:


## Background color example ​

Another example could be binding the background color of an element.

Practically speaking, you will likely need to utilize formulas to achieve the logic you desire in your bindings. For example, conditionally showing two different background colors based on whether a condition is met or not would require the use of an if condition.

`if`
FORMULAS

Formulas are a superpower when creating conditions and calculations.

To learn more about formulas, check out the intro to formulas

In the example video below, the password input's background color is set to be red if the number of characters input is less than 6, and green if it is greater than 6:

BINDINGS vs STATES

In the example above, we used an if condition in our binding to conditionally change the background color.

However, we could alternatively have created a state to handle this. States are great when you have many different conditions that you need to cater for, as the formula editor may become difficult to read when working with multiple, very complex formulas.

Here is the same example from above of changing the background color, however, this time utilizing a custom state:

Learn more about states


## Common style properties to bind ​

Several styling properties are frequently bound to data to create dynamic interfaces:


## Using AI to create style bindings ​

WEWEB AI

If you are unsure of the basics of using WeWeb AI, check out the intro to WeWeb AI

WeWeb AI makes creating style bindings faster and more intuitive through natural language commands.


### Creating conditional style bindings with AI ​

Instead of manually writing formulas for style bindings, you can describe your desired styling behavior to the AI:

- select the element you want to bind the styling property of
- open the binding menu for the desired styling property
- click Edit with WeWeb AI
- describe the styling condition you want to create
- pass in any relevant data as context

`Edit with WeWeb AI`
For example, you could ask:

"Change the background color of this password input to green when more than 6 characters have been input, and red when not"

PASSING DATA AS CONTEXT

If you want the AI to use certain pieces of data in the bindings it creates, make sure to pass this data in as context. This will make it much more likely that the AI uses the correct data.


### Optimizing complex style bindings with AI ​

For more complex style bindings that involve multiple styling properties, you can prompt the AI for the desired styling without having the binding menu open – just the desired element selected. This way it will be able to bind multiple styling properties in one go, or create the needed states for the styling:

"When the number of characters in the password input is less than 6, I want it to have a low opacity, red border, and red background. When 6 or more characters are input, I want full opacity, a green border, and green background."

STATES

In the example above, the AI created states for each condition, and then in each state set the desired styling.

Using states here made sense as it is much more manageable and readable than having the same condition bound to each individual style property.

This way, if we want to change the condition in the future, the condition of the state only needs to be changed and not the conditions of every single bound styling property.

Learn more about states

CONTINUE LEARNING

The final core piece of functionality that bindings can add to your project is the ability to dynamically create elements from lists of data:

Learn about binding the repeating of items →

