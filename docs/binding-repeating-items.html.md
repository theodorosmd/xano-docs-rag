# Binding the repeating of items ​


# Binding the repeating of items ​

With binding, you can dynamically repeat items/elements and use each respective item's data inside bindings. This powerful feature allows you to create lists, grids, and other repetitive UI patterns that automatically update when your data changes.


## Creating repeating items ​

The main use-case would be to display a list of items coming from your backend. Let's say you want to display a list of products coming from your backend:

- Create the design for the product cards. You just need to create 1, as we will dynamically repeat the cards:

- Place the product card into an empty flexbox. You can do this very simply by pressing ⌘+G on Mac, or Ctrl+G on Windows to place the selected element into an empty flexbox:

- Turn on the repeating of items and bind our list of products:

Our product card is now being created for every item in our bound list of products

BINDING A LIST

When binding the repeating of items, you MUST bind it to a list of items (also known as an array). If you do not pass in a list of items, then it will not be able to automatically process the items and detect how many elements need to be created.

- Before we connect each piece of data from our products, let's style the list of products:

- Finally, let's bind each field of the product card to its respective item's data:

ITEM DATA

Whenever you dynamically repeat items using a bound list of data, each element created will automatically have access to its respective item's data.

To recap the steps in the example above:

- Created a blank product card whose content we would later dynamically bind
- Placed the blank product card into an empty flexbox (that we named 'Products List')
- With the parent flexbox selected, turned on Repeat Items and bound the Items property to our list of products data
- Styled the list so it appeared as desired
- Bound each content element inside the product card to its respective field in the item data

`Repeat Items`
`Items`

## Visually detecting repeated items ​

To tell if an element in the layout tree is repeating its child element, you can look for this purple icon:

This indicates that its child element is being repeated.

When you expand the element to see its child, the child element will be colored purple to also indicate that it is being repeated, and will display how many times it is being repeated.


## Working with item data ​

When working with repeated items, you can access the current item's data directly within the respective child elements:


## Common repeating patterns ​

Here are some common UI patterns you can create with repeated items:


## Using AI to create repeating items ​

WeWeb AI makes setting up repeating items much faster and more intuitive through natural language commands.


### Creating a repeating list with AI ​

Instead of manually configuring repeating items, you can describe what you want to the AI:

- select the element you want to repeat
- open the AI chat panel
- describe the repeating behavior you want to create
- pass in the list of items you want to repeat

For example, you could ask:

"I want to repeat this product card for each item in my products data in a 4 column grid with 24px spacing. I want to bind each field of the product card to its respective field in the item data"


### Ensuring the AI can correctly map fields ​

In the example above, the AI was able to correctly map the content of the product card to their corresponding fields in the item dat, due to the names of the elements closely mirroring that of the fields in the data:


### Creating filtered repeating lists with AI ​

WeWeb AI can also create sophisticated filtering logic for your repeated items:

- if you already have a repeating list you want to filter, select the list element. If not, select the element you want to repeat
- open the AI chat panel
- describe the filtering you want to create
- If you do not already have the list created, pass in the list of items you want to repeat

In this example, we are adding filtering to an already created list of items:

"In this Products Grid, I want to only show items whose price is less than 35 dollars"


## Best practices for repeating items ​

- Optimize for performance: if you're repeating many items, consider implementing pagination or infinite scrolling to avoid performance issues.
- Use the right container: choose the appropriate container type (flexbox, grid, etc.) based on your layout needs.
- Consider empty states: add visual feedback for when your data collection is empty.
- Implement sorting and filtering: allow users to sort and filter repeated items to find what they're looking for more easily.
- Handle loading states: show loading indicators while data is being fetched to improve the user experience.

Optimize for performance: if you're repeating many items, consider implementing pagination or infinite scrolling to avoid performance issues.

Use the right container: choose the appropriate container type (flexbox, grid, etc.) based on your layout needs.

Consider empty states: add visual feedback for when your data collection is empty.

Implement sorting and filtering: allow users to sort and filter repeated items to find what they're looking for more easily.

Handle loading states: show loading indicators while data is being fetched to improve the user experience.

