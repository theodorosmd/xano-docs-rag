# Stop click propagation ​


# Stop click propagation ​


### What is event bubbling? ​

Imagine you have a button inside a clickable card. When you click the button, by default in JavaScript, the click event "bubbles up" - meaning it triggers the button's click event, then the card's click event too. This bubbling is a core JavaScript behavior, like a ripple in water that spreads outward affecting larger and larger areas.


## The problem ​

This natural JavaScript bubbling behavior can cause unintended effects. For example:

- You click a "Delete" button inside a clickable card
- The button click deletes an item
- But then the click also bubbles up to the card, which might navigate to a different page
- Now you have unwanted navigation happening after your delete action


## The solution ​

The Stop propagation action stops this default JavaScript event bubbling. It tells the event "stop right here, don't spread any further." So in our example:

`Stop propagation`
- User clicks the Delete button
- Delete action happens
- Stop propagation prevents the click from reaching the card
- No unwanted navigation occurs

`Stop propagation`
TIP

This action executes both:

- Event.stopPropagation(): stops the event from bubbling up
- Event.preventDefault(): prevents the default browser behavior

`Event.stopPropagation()`
`Event.preventDefault()`
Set this action as the first action in your workflow for best results.

