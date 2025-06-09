# Adding logic to popups ​


# Adding logic to popups ​

Popups in WeWeb have their own powerful logic system that lets you create dynamic, interactive experiences. You can make your popups respond to user actions, display different content based on conditions, and create more personalized user experiences.

WORKING WITH LOGIC

The popup logic system in WeWeb follows similar patterns to how logic works with components. If you're already familiar with WeWeb components, you'll find these concepts familiar.

Learn more about components →


## Properties - the foundation of dynamic popups ​

Properties allow you to create popups that can display different content each time they're shown, making them reusable across your application.


### Creating popup properties ​

To add properties to your popup:

- In the Properties section, click the + New button to create a new property
- name your property
- select its type (text, number, boolean, etc.)
- give it a default value (optional)

`Properties`
`+ New`
Each property you create becomes available to use within your popup, and can be passed values when the popup is opened.


#### Product detail properties examples ​

Imagine you're creating a popup to display product details:

- Product Name (Text) - The name of the product to display
- Product Description (Text) - The description of the product to display
- Product Price (Number) - The current price of the product
- Product Image (Image URL) - URL to the product's image
- Available Stock (Number) - Number of the product available in stock
- Product ID (Number) - The ID of the product

These properties allow you to reuse the same popup design for any product in your catalog.


### Binding elements to properties ​

Once you've set up properties, you can bind them to elements inside your popup:

- select any element in your popup
- in the right panel, find the property you want to make dynamic (text, visibility, etc.)
- click the binding icon
- select your property or variable, or create an expression

For example, to bind text content to a property:

- select a text element
- click the binding icon next to the Text field
- select your property (e.g., Product Name)

`Text`
`Product Name`

### Passing values to popups ​

When opening a popup via a workflow, you can pass values to its properties:

- select the element you want to act as a trigger for opening the popup
- add a new workflow
- add the Open popup action to your workflow
- select the popup you want to open
- define the values you want to pass in for the available properties
- test in preview mode to ensure the properties are used as expected

`Open popup`

## Creating internal popup data ​


### Variables ​

Variables in popups are scoped to the popup instance and help you manage state within the popup.

WHAT DOES "SCOPED" MEAN?

When we say variables are "scoped" to the popup, it means they only exist inside that specific popup. They can't be accessed from outside the popup, and they don't affect other parts of your application. Think of it like each popup having its own private notebook for storing information.

To create a variable:

- in the Data section, click the + New button
- name your variable
- select its type (text, number, boolean, etc.)
- give it an initial value (optional)

`Data`
`+ New`
Variables are perfect for:

- tracking user input within a form
- toggling between different views in a multi-step popup
- storing temporary data that doesn't need to be passed from outside


### Product detail variables examples ​

- Selected Quantity (Number) - Set to 1 initially, tracks how many items the user wants to purchase

By updating these variables with workflows, you can create an interactive experience without needing to close and reopen the popup.


## Adding interactivity with workflows ​

Workflows let you create interactive behavior within your popups.


### Creating popup workflows ​

- in the Workflows section, click the + New button
- name your workflow
- select your desired trigger
- add actions to define what happens when the workflow runs

`Workflows`
`+ New`
Workflows can be triggered by any element inside the popup.


### Product detail workflow examples ​

Workflow name: Increase QuantityTriggered by: "+" button click

Actions:

- Check stock availabilityCondition: Selected Quantity < Available Stock
- Condition: Selected Quantity < Available Stock
- If condition passes:Set Selected Quantity to Selected Quantity + 1
- Set Selected Quantity to Selected Quantity + 1

- Condition: Selected Quantity < Available Stock

`Selected Quantity < Available Stock`
- Set Selected Quantity to Selected Quantity + 1

`Selected Quantity`
`Selected Quantity + 1`
Workflow name: Decrease QuantityTriggered by: "-" button click

Actions:

- Check minimum quantityCondition: Selected Quantity > 1
- Condition: Selected Quantity > 1
- If condition passes:Set Selected Quantity to Selected Quantity - 1
- Set Selected Quantity to Selected Quantity - 1

- Condition: Selected Quantity > 1

`Selected Quantity > 1`
- Set Selected Quantity to Selected Quantity - 1

`Selected Quantity`
`Selected Quantity - 1`
These workflows handle the quantity selection functionality, ensuring that users can't select a quantity less than 1 or more than the available stock.


## Formulas for dynamic calculations ​

Formulas let you create reusable calculations or logic within your popup.

- in the Formulas section, click the + New button
- name your formula
- add any needed input parameters
- configure the formula's logic
- add a description to the formula (optional)

`Formulas`
`+ New`
Formulas are useful for:

- calculating values based on user input
- formatting display text
- determining visibility conditions


### Product detail formula examples ​

- Formatted PriceParameters: price (Number)Formula: Adds currency symbol to price of the productUse: Displaying consistent price formatting throughout the popup
- Parameters: price (Number)
- Formula: Adds currency symbol to price of the product
- Use: Displaying consistent price formatting throughout the popup
- Is Out Of StockParameters: available_stock (Number)Formula: Checks if the available quantity is zeroUse: Showing "Out of Stock" message and disabling the Add to Cart button
- Parameters: available_stock (Number)
- Formula: Checks if the available quantity is zero
- Use: Showing "Out of Stock" message and disabling the Add to Cart button

Formatted Price

- Parameters: price (Number)
- Formula: Adds currency symbol to price of the product
- Use: Displaying consistent price formatting throughout the popup

Is Out Of Stock

- Parameters: available_stock (Number)
- Formula: Checks if the available quantity is zero
- Use: Showing "Out of Stock" message and disabling the Add to Cart button

VIDEO GUIDE

Want to see the product detail popup being built in full? Check out our complete video walkthrough for building a product details popup with properties, variables, workflows, and formulas.

View the product details popup example →

