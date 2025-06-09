# Intro to formulas ​

Academy

Want to learn more about working with formulas in WeWeb? Check out our Build a Proof of Concept course which teaches you how to use formulas to manipulate data effectively in your web applications.


# Intro to formulas ​

Formulas in WeWeb allow you to manipulate and transform data in your application. They are the key to creating dynamic logic that responds to user actions, formats information, and connects different parts of your application together.


## Understanding formulas ​

Formulas are stored calculations that let you work with data in your WeWeb application. Think of them as mini-programs that take some input, process it according to rules you define, and return a result that you can use in your UI or workflows.

Common uses for formulas include:

- formatting text for display (like dates, currency, or user names)
- creating conditional logic to change styles or content
- calculating values based on user input or other data
- transforming data between different formats


## Accessing formulas ​

To access the formulas:

- open the binding menu
- navigate to the formulas tab
- select any of the available no-code formulas

`formulas`
If you are ever curious as to what a formulas does, you can hover its respective tooltip to find out more:

JAVASCRIPT UNDER THE HOOD

Behind the scenes, the formula window in WeWeb is powered by JavaScript. This means that alongside WeWeb's native formulas, you can use standard JavaScript expressions, methods, and operators in your formulas.

For example, if you wanted to make a piece of text uppercase:

- you could use the native no-code formula:

- or, you could do it using the standard JavaScript expression for making text uppercase:


## Using formulas ​

To use a formula, you need to pass in values inside the parenthesis (). Some formulas require just a single input, and some require multiple inputs.

`()`
CHECK FORMULA INPUT

To see what inputs a formula expects, hover over its tooltip.

It will detail exactly how many inputs and what type of inputs it expects:


### Single inputs ​

For example, if using a formula that requires a single input:


### Multiple inputs ​

Or, if using a formula that requires multiple inputs:

Adding more inputs is as simple as adding whatever values you like and seperating them with a comma ,:

`,`

## Types of formulas in WeWeb ​

WeWeb offers two main ways to create and use formulas in your application:


### Local formulas ​

Local formulas are created directly within a binding and are specific to that single use case:

In the example above:

- we select our tag text element
- open the binding menu for the text content property
- navigate to the formulas tab to access the native formulas
- use the if condition to dynamically change the text based on the stock of the product

`formulas`
`if`
Local formulas are limited to the specific place where you create them. If you need the same formula logic elsewhere, you would need to recreate or copy it.


### Global formulas ​

As your application grows in complexity, you'll often need to reuse the same formula logic throughout your project. Global formulas solve this problem by letting you define a formula once and use it everywhere:

In the example above:

- we navigate to the actions tab in the sidebar
- click new to create a global formula
- define the input parameters formula logic that will transform the input
- create the formulas logic utilizing the input parameters
- the formula is now available for use throughout the entire project

`actions`
`new`

## Using global formulas ​

Once you've created a global formula, you can easily use it anywhere in your application:

In the example above:

- we open the binding menu for a property
- navigate to the formulas tab
- find our global formula in the from project section
- add the formula, providing any required input parameters inside the parenthesis ()

`formulas`
`from project`
`()`

## Global formula input parameter ordering ​

When using a global formula that requires inputs, it is important to be conscious of the expected order of the inputs and pass them in the same sequence they appear in the creation window.

For example, in this formula:

The sequential ordering of the parameters is:

- text_input
- number_input

`text_input`
`number_input`
As such, when using this global formula, the values you pass inside the parentheses will be assigned to the parameters in this exact order:

```
// The first value 'Hello World' is assigned to text_input
// The second value 42 is assigned to number_input
exampleFormula('Hello World', 42)
```

`// The first value 'Hello World' is assigned to text_input
// The second value 42 is assigned to number_input
exampleFormula('Hello World', 42)`
If you were to reverse the order of the values:

```
exampleFormula(42, 'Hello World')
```

`exampleFormula(42, 'Hello World')`
This would cause unexpected results because the number 42 would be assigned to text_input and the string 'Hello World' would be assigned to number_input.

`42`
`text_input`
`'Hello World'`
`number_input`
This is why it's critical to know the order of parameters when using global formulas.


## When to use global vs. local formulas ​

Both local and global formulas have their place in WeWeb development:

Use local formulas when:

- the logic is simple and specific to one place
- you're prototyping or testing an idea
- the formula won't need to be reused elsewhere

Use global formulas when:

- you need the same logic in multiple places
- the formula logic is complex
- you want to maintain consistency across your application
- you anticipate needing to update the logic later and want to do it in one place

As a general rule, if you find yourself copying and pasting the same formula multiple times, it's a strong sign that you should convert it to a global formula.


## Formula management ​

In addition to allowing you to re-purpose logic across your project, global formulas give you ability to track their use across specific pages:



This can be particularly useful when you are trying to debug or refactor logic.

CONTINUE LEARNING

Formulas are a core building block in creating logic. The next core piece is being able to programatically use them.

That is where workflows come in.

Learn about workflows →

