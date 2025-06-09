# States ​


# States ​

A state is a combination of CSS properties that you want to trigger at a specific moment on an element.

It can be classic CSS states like hover, or user-generated ones that you define while building your app.




## How to create a State ​

To create a new CSS state, click on the element you want to create the state on, then on Default > Add State:

`Default > Add State`



## How to configure a state ​

When the state if created, open its tab and set 3 options:

- the state's name
- the condition under which the state should trigger, which is bindable and should return true when the state is to be active, false otherwise
- whether to apply the state the the element's children or not

`true`
`false`


When the state is selected at the top of the style sidebar, any CSS changes that you'll do will be only applied for this state.

Example: here the color and display will only change when the state Please Click Me! is activated:

`Please Click Me!`



## How to apply a State to an element's children ​

When Apply to children is set to On, you can use the state on any of the element's children by simply using it. It should be called {{Parent}}:{{State name}}.

`Apply to children`
`On`
`{{Parent}}:{{State name}}`
For example, if a button has a state called Please Click Me!, an icon inside this button can use the same state which would be called Button:Please Click Me!:

`Please Click Me!`
`Button:Please Click Me!`



## Focus state ​

The button and input elements recognize the focus state if you add it as a custom state on the element.

`focus`
In the example below, we have a focus state on an input that changes the border color when a user navigates to the input:

`focus`


