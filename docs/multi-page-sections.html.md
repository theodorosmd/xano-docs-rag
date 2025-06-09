# Multi-page sections ​

Academy

Want to learn how to create faster, smoother user experiences in WeWeb? Check out our Build a Proof of Concept course which covers multi-page sections and other techniques for optimizing performance.


# Multi-page sections ​


## WeWeb apps are SPAs ​

When you publish a WeWeb app, you publish a standard Vue.js Single-Page Application.

Single-Page Applications are great to build smooth user experiences where users can navigate seemlessly between different views in the app.

TIP

Compared to Multi-Page Applications, SPAs achieve increased speed and responsiveness because, instead of loading all the content of a page on page load, it only loads new content.

For example, when a user navigates from page A to page B, the navigation menu that was loaded when the user arrived on page A is not loaded a second time when they arrive on page B.

To leverage that feature of Single-Page Applications in WeWeb, you would need to create a new instance of a multi-page section.


## Multi-page sections ​

In WeWeb, you can add multi-page sections by going to the Add > Multi-page sections menu:

`Add`
`Multi-page sections`


Once you're on the Multi-page sections menu, you can drag a section that exists on one page, and drop it on the current page.

`Multi-page sections`
When you do this, you will be invited to choose between creating an instance or creating a copy of that section:




## Benefits of instances ​

When you create a new instance of a section, the changes you make on one instance of the section will be reflected in all the other instances of that section.

Create a new instance if you want the section to remain the same on all pages no matter what changes you make.

When you publish your app, the section will be loaded once. Other instances of the section will not be reloaded.


## Benefits of copies ​

When you create a new copy of a section, the changes you make in the original will not be reflected in the copy, and vice versa.

Create a new copy if you want to take inspiration from an existing section but want the new section to be independent of the other.

When you publish your app, both sections will be loaded.


## Instance vs copy example ​

In the example below, you can see that we chose to:

- create a new instance of the sidebar menu because we don't want to have to reload this menu when the user navigates to a new page,
- create new copies of the header and content sections because these sections will be different on each page and should be loaded when the user navigates to the new page



