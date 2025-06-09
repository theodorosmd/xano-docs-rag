# Working with popups ​


# Working with popups ​

Popups are essential UI elements that appear above the main content of your application to display information, capture user input, or provide notifications. WeWeb's popup system allows you to create and manage various types of popups like modals, alerts, and toasts with a dedicated popup management system.


## Understanding the popup system ​

In WeWeb, popups are treated as dedicated components with their own management system. This approach provides several advantages:

- centralized management - all popups are managed in one dedicated location
- instance-based control - open multiple instances of the same popup type with different content
- reusability - create popup templates that can be reused throughout your application
- customizability - configure various settings like animation, position, and backdrop


## Creating your first popup ​

To create a new popup in WeWeb:

- click on the Popups tab in the left panel
- click the New button to create a popup
- choose from available popup templates (Modal, Alert, Toast, etc.)
- customize your popup's content and appearance

`Popups`
`New`

## Types of popups ​

WeWeb offers several built-in popup types to cover different use cases:


## Customizing popup appearance ​

Each popup type has specific settings you can configure:


### Common settings ​

- animation - choose how the popup appears (Fade, Slide, Zoom, etc.)
- prevent scrolling - toggle whether the background content can be scrolled
- escape key to close - allow users to close the popup by pressing ESC
- overlay - toggle the background overlay
- overlay click closes - close the popup when clicking outside of it
- overlay background color - customize the overlay's appearance

`animation`
`prevent scrolling`
`escape key to close`
`overlay`
`overlay click closes`
`overlay background color`

### Position settings (varies by popup type) ​

- type - select the popup variant (Modal, Sheet, etc.)
- side - choose which side the popup appears from (Top, Bottom, Left, Right)
- align - set the alignment (Center, Start, End)

`type`
`side`
`align`
MIGRATING FROM DIALOG ELEMENT

If you've previously used the Dialog element, these settings match the Dialog's properties, making it easy to recreate your existing popups.


## Working with popup instances ​

A key concept in WeWeb's popup system is the notion of instances. An instance is a specific occurrence of a popup that is currently open in your application.


### Managing instances ​

In simple terms, an "instance" is just a specific popup that's currently open on your screen. Think of it like this:

- a popup is like an email template (the design and structure you've created)
- an instance is like each individual email sent from that template (what appears for users)

For example, you might have an "Alert" popup with a title, message, and action button. Each instance of this alert could show different content:

- one instance might display "Payment successful" with account details
- another instance might show "New message received" with a preview and reply button
- a third instance could present "Update available" with version info and download link

All these alerts use the same popup, but display as separate instances with their own content.

The Popups panel shows all currently open instances grouped by their popup model:

`Popups`
You can:

- see which popup instances are currently open
- close specific instances directly from the panel

DYNAMIC CONTENT IN INSTANCES

Popup instances are perfect for showing dynamic content based on user actions or data. You can create one popup design and use it in many different contexts by changing the content dynamically for each instance.

Learn more about adding logic to your popups →


## Opening and closing popups ​

Popups in the new system are controlled through workflows.

To control popups via workflow actions:

- create a workflow (local, global, page, or app)
- add an Open popup action
- select the popup model you want to open
- optionally, enable Wait close event if you want the workflow to pause until the popup is closed.

`Open popup`
`Wait close event`
WAIT CLOSE EVENT

The Wait close event property of the Open popup can be extremely powerful.

`Wait close event`
`Open popup`
Learn more about using 'Wait close event' →

To close all open popups, use the Close all popups action in your workflows:

`Close all popups`

## Passing data to popups ​

To make your popups dynamic, you can pass data when opening them:

- open the Edit menu of the popup you want to make dynamic
- create properties by clicking the + New button in the Properties section
- bind element properties in your popup to the popup properties (e.g., text content, image source, style properties)
- now, in the Open popup workflow action, you can pass in values for these properties
- test in Preview mode that your popup correctly uses the dynamic content

`Edit`
`+ New`
`Properties`
`Open popup`
`Preview`
REUSING POPUPS

By using properties, you can reuse the same popup in multiple scenarios with different content:

- Display user profiles with different user data
- Show product details with varying product information
- Create confirmation dialogs with custom messages and actions
- Build error/success notifications with dynamic messages

Learn more about adding logic to your popups →


## Best practices for popups ​

- use sparingly - popups interrupt the user experience, so use them only when necessary
- provide clear dismissal options - always give users an obvious way to close popups
- consider mobile users - ensure popups work well on smaller screens
- use appropriate types - choose the right popup type for each use case (toast for non-critical notifications, modals for important interactions)
- keep content focused - popups should contain only the information or controls needed for the specific task


## Common popup patterns ​

Here are some common ways to use popups in your WeWeb application:


### Confirmation dialogs ​

Use a modal popup to confirm user actions before proceeding with potentially destructive operations:


### Form popups ​

Collect user input without navigating away from the current page:


#### Submitting forms with external action buttons ​

A common pattern in popup forms is to have the form content in the main popup area with action buttons (Submit, Cancel) positioned outside the form container, often in a dedicated footer area. This creates a clean separation between content and actions.

To submit a form using buttons outside the form container:

Step 1: Give your form an ID

- Select your Form Container element
- In the Settings panel, find the id field
- Enter a unique identifier for your form (e.g., "contact-form", "signup-form")

`Settings`
`id`
Step 2: Configure the external button

- Select the button that should submit the form
- In the Settings panel, make sure the button's Type is Submit Button
- Also in the Settings panel, add an attribute
- The name of the attribute should be form, and the value should be the id you assigned to your form
- Now, on click, the button will trigger the submission of your given form

`Settings`
`Type`
`Submit Button`
`Settings panel`
`form`
This approach is particularly useful for:

- Multi-step forms in popups where you want consistent action button placement
- Complex popup layouts where form content and actions are visually separated
- Maintaining clean, professional popup designs with dedicated action areas

TIP

Learn more about external form submission in the Form container documentation.


### Notification toasts ​

Provide non-intrusive feedback about system events or action results:

CONTINUE LEARNING

Ready to dive deeper into creating interactive user experiences? Learn how to make your popups smarter with logic:

Learn more about adding logic to your popups →

