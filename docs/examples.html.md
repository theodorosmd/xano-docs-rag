# Popup examples ​


# Popup examples ​

This guide provides practical examples of different popups you can create in WeWeb. Each example includes step-by-step instructions and demonstrations to help you implement common popup patterns.


## Product details popup ​

A product details popup allows users to view additional information about a product without navigating away from the current page. This is commonly used in e-commerce applications to show product details when a user clicks on a product card.


### Creating the popup ​

- Click on the Popups tab in the left panel
- Click the New button to create a popup
- Choose the Modal type
- Design your popup with image, text, and button elements

`Popups`
`New`
`Modal`

### Adding properties ​

Create the following properties for your product details popup:

- Product Name (Text) - The name of the product to display
- Product Description (Text) - The description of the product to display
- Product Price (Number) - The current price of the product
- Product Image (Image URL) - URL to the product's image
- Available Stock (Number) - Number of the product available in stock
- Product Data (any) - The entire product data object of the product


### Adding variables ​

Add these variables to manage the popup's internal state:

- Selected Quantity (Number) - Set to 1 initially, tracks how many items the user wants to purchase


### Creating workflows ​

Create quantity selection workflows for the popup buttons:

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

### Creating the quantity selector ​

Create a quantity selector UI with the following elements:

- A container with three elements:A decrease button with a "-" icon or textA text element showing the current quantityAn increase button with a "+" icon or text
- A decrease button with a "-" icon or text
- A text element showing the current quantity
- An increase button with a "+" icon or text
- Style the container and elements:Align elements horizontally with appropriate spacingAdd borders, backgrounds, and hover states for buttonsCenter the quantity text
- Align elements horizontally with appropriate spacing
- Add borders, backgrounds, and hover states for buttons
- Center the quantity text
- Bind elements to data:Bind the quantity text's content to the Selected Quantity variable
- Bind the quantity text's content to the Selected Quantity variable
- Add workflows to the buttons:Add the "Increase Quantity" workflow to the "+" buttonAdd the "Decrease Quantity" workflow to the "-" button
- Add the "Increase Quantity" workflow to the "+" button
- Add the "Decrease Quantity" workflow to the "-" button

A container with three elements:

- A decrease button with a "-" icon or text
- A text element showing the current quantity
- An increase button with a "+" icon or text

Style the container and elements:

- Align elements horizontally with appropriate spacing
- Add borders, backgrounds, and hover states for buttons
- Center the quantity text

Bind elements to data:

- Bind the quantity text's content to the Selected Quantity variable

`Selected Quantity`
Add workflows to the buttons:

- Add the "Increase Quantity" workflow to the "+" button
- Add the "Decrease Quantity" workflow to the "-" button


### Using formulas ​

Add these formulas to enhance the popup's functionality:

- Formatted PriceParameters: price (Number)Formula: Adds currency symbol to Product PriceExample: "$" + priceUse: Displaying consistent price formatting throughout the popup
- Parameters: price (Number)
- Formula: Adds currency symbol to Product Price
- Example: "$" + price
- Use: Displaying consistent price formatting throughout the popup
- Is Out Of StockParameters: available_stock (Number)Formula: Checks if the Available Stock is less than 1Example: available_stock < 1Use: Showing "Out of Stock" message and disabling the Add to Cart button
- Parameters: available_stock (Number)
- Formula: Checks if the Available Stock is less than 1
- Example: available_stock < 1
- Use: Showing "Out of Stock" message and disabling the Add to Cart button

Formatted Price

- Parameters: price (Number)
- Formula: Adds currency symbol to Product Price
- Example: "$" + price
- Use: Displaying consistent price formatting throughout the popup

`Product Price`
`"$" + price`
Is Out Of Stock

- Parameters: available_stock (Number)
- Formula: Checks if the Available Stock is less than 1
- Example: available_stock < 1
- Use: Showing "Out of Stock" message and disabling the Add to Cart button

`Available Stock`
`available_stock < 1`

### Binding elements to properties ​

- Bind the product image to the Product Image property
- Bind the title text to the Product Name property
- Bind the description text to the Product Description property
- Bind the price text to the Formatted Price formula
- Bind the quantity value text to the Selected Quantity variable
- Bind the "Add to Cart" button's disabled state to the Is Out Of Stock formula
- Bind the increase button to the "Increase Quantity" workflow
- Bind the decrease button to the "Decrease Quantity" workflow

`Product Image`
`Product Name`
`Product Description`
`Formatted Price`
`Selected Quantity`
`Is Out Of Stock`

### Setting up the Add to Cart button ​

- Select the "Add to Cart" button in the popup
- Create a new workflow triggered by the button's click
- Add a "Close this popup instance" action
- In the data field of this action, add the following object:{
  action: "add_to_cart",
  product_data: Product Data,
  quantity: Selected Quantity
}
- This data will be returned to the original workflow that opened the popup

```
{
  action: "add_to_cart",
  product_data: Product Data,
  quantity: Selected Quantity
}
```

`{
  action: "add_to_cart",
  product_data: Product Data,
  quantity: Selected Quantity
}`

### Opening the popup ​

- On your product listing page, select the product card "View" button
- Create a workflow triggered by click
- Add an Open popup action
- Select your product details popup
- Map the product data to the popup's properties: Product Name: product.nameProduct Description: product.descriptionProduct Price: product.priceProduct Image: product.image_urlAvailable Stock: product.stockProduct Data: product (the entire product object)
- Product Name: product.name
- Product Description: product.description
- Product Price: product.price
- Product Image: product.image_url
- Available Stock: product.stock
- Product Data: product (the entire product object)
- Turn Wait close event on

`Open popup`
- Product Name: product.name
- Product Description: product.description
- Product Price: product.price
- Product Image: product.image_url
- Available Stock: product.stock
- Product Data: product (the entire product object)

`product.name`
`product.description`
`product.price`
`product.image_url`
`product.stock`
`product`
`Wait close event`

### Processing the popup return data ​

After the popup closes, you can access the returned data in your workflow that opens the popup:

- Add a Multi-option split action after the Open popup action
- Bind the split condition to the action returned by the popup
- Create a branch for "add_to_cart"
- In the "add_to_cart" branch, add an action to process the cart item: Use the product_data to access the product informationUse quantity to access the selected quantity
- Use the product_data to access the product information
- Use quantity to access the selected quantity

`Multi-option split`
`Open popup`
`action`
- Use the product_data to access the product information
- Use quantity to access the selected quantity

`product_data`
`quantity`

### Testing the popup ​

- Preview your page
- Click on a product card's "View" button
- Verify that the popup shows the correct product information
- Test the quantity selector (should not go below 1 or above available stock)
- Click the "Add to Cart" button
- Verify that the item appears in your cart with the correct quantity


## Alert popup ​

Learn more about adding logic to popups →

