# Conditional rendering ​


# Conditional rendering ​

In this article, we will explain how to use the advanced Conditional Rendering setting available in the Settings tab of elements:

`Conditional Rendering`
`Settings`



## Difference with display:none ​

`display:none`
The Conditional Rendering setting can greatly improve the performances of your web app because, when you hide an element using this advanced setting, that element will not be built on page load by default. It will only be rendered in the DOM if / when the condition to display it is met. As a result, your pages will load faster.

`Conditional Rendering`
By comparison, when you use the standard display CSS property to hide an element on a page, the browser still needs to build that element on page load. If you have a lot of hidden elements on the page, it can significantly slow down your browser.

`display`
You may wonder why ever use the standard CSS display property anymore? Well, if you need to access input variables of an element that is hidden by the Conditional Rendering setting, you won't be able to because the element won't be in the DOM. In that use case, the standard display property will continue to be very useful.

`display`
`Conditional Rendering`
`display`

## Using Conditional Rendering ​

`Conditional Rendering`
The Conditional Rendering setting needs you to define a condition. When that condition is met, the element will be made available in the DOM and displayed on the page (provided you haven't used the standard CSS display property to hide it!).

`Conditional Rendering`
`display`
In the example below, we are saying that, if the user types in more than 225 characters (from index 0 to 224 in the string of characters that is user_description text), we will display a message warning them they are close to reaching the 280 character limit:

`user_description`


Like the standard CSS display property, the element will not appear on the page when the condition is not met:

`display`


The crucial difference with the standard CSS display property is that the element will not appear in the DOM either, the browser will only build it when the condition is met. In the WeWeb Navigator, you will see the little crossed-out eye icon that warns you an element is not displayed.

`display`
In the example below, you can see that, when we remove some text and fall below the 225 characters limit, the warning text element disappears completely from the DOM in the browser:



If we were using the display CSS property, the element would still be visible in the DOM in the browser.

`display`
