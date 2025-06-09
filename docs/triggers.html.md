# Triggers ​


# Triggers ​

Triggers define when your workflows should execute, allowing you to create interactive applications that respond to user actions and system events. From a button click to a page load, triggers are your way to make things happen at the right moment.

TIP

The available triggers sometimes vary depending on the element or custom component type. For example, input fields have specific triggers like On change that aren't available for buttons, while forms have unique triggers like On submit. Some triggers are also exclusive to page-level workflows, such as On page load.

`On change`
`On submit`
`On page load`
Additionally, if using the Supabase plugin, you can access Supabase Realtime triggers, such as Realtime | Subscribe to channel

`Realtime | Subscribe to channel`

## Element triggers ​

Element triggers activate when users interact with WeWeb elements:



- On focus: Fires when an element receives focus (e.g., clicking into an input field)
- On blur: Fires when an element loses focus (e.g., clicking away from an input field)

`On focus`
`On blur`

## Mouse events ​

Mouse-related triggers capture various pointer interactions:



- On click: Triggers when an element is clicked
- On double click: Activates upon two rapid successive clicks
- On right click: Fires when the right mouse button is clicked
- On mouse down: Triggers when a mouse button is pressed down
- On mouse up: Fires when a mouse button is released
- On mouse move: Activates when the mouse pointer moves
- On mouse enter: Fires when the pointer enters an element's bounds
- On mouse leave: Triggers when the pointer exits an element's bounds

`On click`
`On double click`
`On right click`
`On mouse down`
`On mouse up`
`On mouse move`
`On mouse enter`
`On mouse leave`

## Touch events ​

Touch event triggers support mobile and touch-screen interactions:



- On touch start: Fires when a touch point is placed on the screen
- On touch move: Triggers when a touch point moves along the screen
- On touch end: Activates when a touch point is removed from the screen
- On touch cancel: Fires when a touch event is interrupted

`On touch start`
`On touch move`
`On touch end`
`On touch cancel`

## Other events ​

Additional triggers for broader interaction scenarios:

- On scroll: Activates when an element or the window is scrolled

`On scroll`



## Lifecycle events ​

When you visit a webpage, your browser creates something called the DOM (Document Object Model). Think of the DOM as a live representation of your webpage - like a blueprint that shows how all elements (buttons, text, images) are organized and connected. Every time you interact with a webpage, you're actually interacting with its DOM.

Every modern web browser includes Developer Tools (often called "Dev Tools") that let you inspect the DOM. The most common way to access it is:

- Right-click on any element of a webpage
- Select "Inspect" or "Inspect Element"

This opens the browser's Dev Tools, usually showing you the "Elements" panel:



WeWeb elements and components go through different stages from initialization to deletion in the DOM - this is called their lifecycle. Events related to component and element lifecycle:



- On created: Fires when an element is initialized in the DOM
- On mounted: Triggers after an element is placed and ready to use on the page
- Before unmount: Executes just before an element is removed from the page

`On created`
`On mounted`
`Before unmount`
TIP

The 'On created' event is fired before the 'On mounted' event.

When an element is 'created', it exists in the DOM but it may not have rendered on the page and/or be ready for user interaction. The 'On mounted' event signifies the element has been rendered on the page and is now ready for user interaction.


## Page and app triggers ​




### Lifecycle ​

- On app load (before fetching collections): The first trigger that fires when your app starts up. Happens before any data is loaded from your database, good for initial setup tasks.
- On app load: Happens after your app is completely ready and all data has been loaded. Everything is set up and ready to use.
- On page load (before fetching collections): Fires when someone opens a page, but before that page's data is loaded. Good for page preparation tasks.
- On page load: Triggers when a page and all its data is fully loaded and ready. The page is now complete and usable.
- On page unload: Happens when someone leaves a page - whether going to another page or closing the tab. Good for saving changes or cleanup.

`On app load (before fetching collections)`
`On app load`
`On page load (before fetching collections)`
`On page load`
`On page unload`

### Listeners ​

- On page scroll: Triggers when page is scrolled
- On page resize: Fires when browser window is resized
- On keydown: Triggers when a keyboard key is pressed
- On keyup: Fires when a keyboard key is released

`On page scroll`
`On page resize`
`On keydown`
`On keyup`
TIP

The On page load (before fetching collections) trigger can be helpful when the data you load on the page depends on the current user's information.

`On page load (before fetching collections)`
For example, you might want to display news items that the user has not yet read or load only the data that matches the user's role in the organization.

Common use cases for app triggers include but are not limited to:

- Triggering the display of a cookie banner if applicable,
- Display a custom alert whenever there is a collection fetch error in your app,
- Change the color of a top navbar when the user scrolls down any page in your app.


## On error ​

The On error workflow triggers when an error occurs at any step of the workflow execution. If any action/step in the workflow fails (e.g., an API call returns an error, or an action encounters an invalid value), the On error branch will execute.

`On error`
`On error`


You can define specific actions under On error to:

`On error`
- Notify users of the issue (e.g., display an error message).
- Log the error for debugging purposes.
- Retry the failed action or workflow step.


## On error vs on collection fetch error ​

The on collection fetch error trigger is a special trigger that fires whenever any collection in your application fails to fetch its data. So if you have multiple collections like:

`on collection fetch error`
- users collection
- products collection
- orders collection

`users`
`products`
`orders`
And you create a workflow starting with the on collection fetch error trigger, that workflow will run whenever any of these collections fails to fetch its data. This is different from the on error tab in a workflow which only handles errors within its specific workflow's actions.

`on collection fetch error`
`on error`
