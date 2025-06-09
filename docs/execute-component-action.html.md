# Execute component action ​


# Execute component action ​

In WeWeb, components can have actions that allow you to control their behavior. These actions are available for:

- Components you create directly in WeWeb
- Built-in WeWeb elements (like the video element)
- Custom imported Vue.js components


## Components created with the editor ​

Components are designed to be self-contained with their own variables and workflows. By default, component workflows are encapsulated and only accessible from within the component to maintain clean separation of concerns and prevent unwanted external interference.

To make a workflow available as an action that can be triggered from outside the component, select the component workflow and enable Allow execution from outside. This allows the workflow to be triggered from anywhere using the Execute component action action.

`Allow execution from outside`
`Execute component action`

## Built-in elements ​

Some WeWeb elements come with pre-configured actions. For example, the default WeWeb video element comes with 3 actions that help you control video playback:



In the example below, we used the component actions configured in the default WeWeb video element to build our own custom controls:


## Coded components: adding actions ​

In WeWeb, you can import custom Vue.js components with your own config file. If you need inspiration, our components are open source.

Learn more about developing custom components with Aurélie and Q:

