# Intro to libraries ​


# Intro to libraries ​

A library is a collection of reusable design assets and UI elements that helps you build applications faster while maintaining consistency. It includes typographies, colors, spacings, components, templates, and classes that can be shared across your workspace and reused across different projects. It is essentially a way for you to build your design system.

WARNING

In our previous UI, you would access the Library panel via Libraries in the top bar. However, this has now been replaced by the Assets menu in the top bar. Please keep this in mind if you still see mention of the Libraries button in the top bar throughout our documentation.

`Library`
`Libraries`
`Assets`
`Libraries`

## Why use libraries ​

Colors, spacings, and typographies allow you to build user interfaces with a consistent look-and-feel, while templates and components help you build faster.

To access the library of your project:

- Open the Assets menu in the top bar
- Click Library

`Assets`
`Library`


You will now see the library of your project:



If you start with a blank project, it will be empty but you can add:

- Components.
- Templates.
- Classes.
- Spacings, colors, and typographies.

TIP

Each WeWeb project has its own library, but you can:

- share that library with the rest of your workspace, and
- add other libraries from your workspace to a project.

Learn more about sharing libraries in WeWeb.


## Typographies ​

In the fourth tab of the Library panel, inside the Typographies section, you can create and edit typographies so that all text elements bound to a typography are updated accordingly when a typography is updated:

`Library`
`Typographies`


In the example below, you can see:

- In the Typographiessection, we created the Small typography in the Label folder.
- We bound that typography in the Styles tab of the selected text on the page.

`Typographies`
`Small`
`Label`
`Styles`
TIP

When creating a typography, we recommend using a default font:



That way, users will be able to use the library without needing to add a specific font to their project.

If you associate a typography to a specific font, users will need to have that font installed in their project for the library to work as expected. Otherwise, when the project is published, the font displayed on the page will fall back to the browser's default font.


## Colors ​

In the fourth tab of the Library panel, inside the Colors section, you can add and organize colors that you can then bind to the CSS color property in the Styles tab of the right panel.

`Library`
`Colors`
`color`
`Styles`
In the example below, we bound the text of one of our labels to the Blue 600 color in our project library:

`Blue 600`


You can also use library colors in formulas:



In the example above, the text color will be different if it's in a primary or secondary button.


## Spacings ​

In the fourth tab of the Library panel, inside the Spacings section, you can add and organize spacing styles that you can then bind to the CSS properties in the Styles tab of the right panel:

`Library`
`Spacings`
`Styles`


In the example above, we bound the corner radius of our label container to a 16px spacing.


## Classes ​

In the third tab of the Library panel, you will be able to see all the style classes in your library.

`Library`
While you won't be able to rename or delete classes through this panel, it can be helpful to get an overview of what classes are used in an external library or to check if a class is attached to a specific library.

Learn more about working with CSS classes in WeWeb.


## Components ​

In the first tab of the Library panel, you will find reusable components that you can use to build a UI that has a consistent look-and-feel, without having to no-code the same functionalities multiple times.

`Library`
Learn more about WeWeb components.


## Templates ​

In the second tab of the Library panel, you will find section and element templates that you can use as UI building blocks to design the frontend of your apps faster:

`Library`



### How to add a template in a library ​

To save an element or section as a template, select it on the page, and click on the Save to library icon:

`Save to library`

### How to add a template on a page ​

Once you have saved templates to your project library, you will be able to drag-and-drop them on the page.

Go to Add > Assets to view available templates and components:

`Add`
`Assets`


TIP

Elements with a green icon are components.


## Rename library item ​

In the Library panel, select the tab where the item is located, select the item you wish to rename, rename it and save it:

`Library`



## Delete library item ​

In the Library panel, select the tab where the item is located, hover over the item you want to delete, click on the three dots next to it and click on delete:

`Library`



## Templates vs components ​

When you drag-and-drop a template on a page, it will create a copy of the template. If you later make a change to the template, those changes will not be reflected in the copies you created before.

When you drag-and-drop a component on a page, it will create a new instance of the component. If you make a change to the component, those changes will be reflected in all the instances of the component you created before.

