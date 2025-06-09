# Intro to variables ​

Academy

Want to learn the essentials of WeWeb? Check out our Build a Proof of Concept course for an introduction to the WeWeb editor and how to work with data effectively.


# Intro to variables ​

Variables are containers that store information in your WeWeb application. Think of them like labeled boxes where you can keep different types of data - text, numbers, lists, or even yes/no values. Just like how you'd label a box "Kitchen Items" to know what's inside, you give each variable a name to easily find and use its contents anywhere in your application.

For example, if you store the name "John Doe" in a variable called userName, you can display or use "John Doe" anywhere you need it on your website.

`userName`
Check out this video to learn more about variables in WeWeb:


## Create a variable ​

Here's a short interactive tutorial on how to create a global variable in WeWeb:

Let's take a look at each step:

- variables are in the Data tab of the WeWeb navigator
- click on the New in the Variables section of the panel
- name your variable
- choose the variable type from the dropdown menu (e.g., Text, Number, Boolean, Query, etc.)
- optionally, you can set a default value for the variable in the Default value field
- decide if you want the variable to be preserved on navigation and/or saved in local storage
- click on Create to create the variable.

`Data`
`New`
`Variables`
`Default value`
`Create`
Now, you can use this variable throughout your website by binding it to UI components or using it in workflows.


## Variables types ​

In programming, variables are helpful to store, send, and display information. For example, you can store the name of a user in a Text variable (also called a string) or a list of users in an Array variable in your frontend before sending the information to your backend.

`Text`
`string`
`Array`
However, if you try to send the value of a Text variable to a column in your backend that expects an Array, you'll get an error.

`Text`
`Array`
That's why it's important to understand the different data types you may encounter in web development.


### Text ​

A text variable is a variable that stores text. You can use text variables to store text values, such as names, addresses, or any other text data. It's equivalent to a string in JavaScript.


### Number ​

A number variable is a variable that stores numbers. You can use number variables to store numeric values, such as prices, quantities, or any other numeric data. It's equivalent to a number in JavaScript.


### Boolean ​

A boolean variable is a variable that stores a boolean value (true or false). You can use boolean variables to store boolean values, such as a flag that indicates whether a user is logged in or not. It's equivalent to a boolean in JavaScript.


### Object ​

An object variable is a variable that stores an object. You can use object variables to store complex data, such as a user profile, a product, or any other data that has multiple properties. It's equivalent to an object in JavaScript.


### Array ​

An array variable is a variable that stores an array. You can use array variables to store a list of values, such as a list of products, a list of users, or any other data that has multiple values. It's equivalent to an array in JavaScript.


### Query ​

You can use query variables to store the value of a query string parameter in an URL.

For example, you can use them to:

- customize what a user sees based on how they got to your site (like showing different content when they click an email link)
- remember which product someone wants to view (like going directly to a specific item when sharing a link)
- keep track of where visitors came from (like knowing if they clicked an Instagram ad)
- show personalized messages (like displaying "Welcome back!" when someone returns through a special link)


## Inspect current value of variables ​

In the example below, our text element is bound to the myName variable. When we change its current value or default value, it changes the text displayed on the page:

`myName`



## Utilizing variables in logic ​

CONTINUE LEARNING

The real power of variables comes in the ability to use them in bindings to create custom logic in your project:

Learn about binding →

