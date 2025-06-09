# Styling Properties ​


# Styling Properties ​

Styling properties are all the options you can use to change an element's design inside your WeWeb app.

They're available on the right sidebar, under the styling tab.

`styling`


TIP

All of available stlying properties are standard CSS properites, the WeWeb editor simply gives you a visual way to edit them.

Learn more about CSS in the WeWeb editor


## Specific ​

This section is a shortcut to find the most used CSS properties for a given element. It's different for every element.

Here are the available styling properties in this section (all elements included):


### Text - {lang} ​

`Text - {lang}`
This is where you can bind the text displayed to a variable, typically, when you want to display some text that comes from a plugin or 3rd-party API.

You'll have to bind it for every language that's currently activated on this page.


### Typography ​

`Typography`
This option is useful when you want to standardise text styles in your app. Here, you can select a text type (for example: heading, subtitle, etc) that you created in the typography section of your app.


### Size ​

`Size`
To set the element text's size (in px, em or rem). Equivalent to CSS' font-size.

`font-size`
Using REM and EM Units

To use relative units like rem or em, you need to bind the Size property and manually type the size value. For example: '1.5rem', '2em', or '0.875rem'.

`rem`
`em`
`Size`
Understanding relative units:

- rem - Relative to the root element's font size (html element)
- em - Relative to the parent element's font size

`rem`
`em`
Customizing the root font size:

To change the base size that rem units are calculated from, you need to add custom code at the head level of your page or entire app to change the root font fize using CSS, like so:

`rem`
```
<style>
:root {
  font-size: 16px; 
}
</style>
```

`<style>
:root {
  font-size: 16px; 
}
</style>`

### Font family ​

`Font family`
To set the font of the text element. Equivalent to CSS' font-family.

`font-family`

### Font weight ​

`Font weight`
To set the weight of the text element (for example: bold, semibold, etc). Equivalent to CSS' font-weight.

`font-weight`

### Line height ​

`Line height`
To set the height between two lines of text in the element. Equivalent to CSS' line-height.

`line-height`

### Alignment ​

`Alignment`
To align the text right, center, left of justified. Equivalent to CSS' text-justified.

`text-justified`

### Text color ​

`Text color`
To set the color of the text. Equivalent to CSS' color.

`color`

### Text decoration ​

`Text decoration`
To set the decoration of the text (for example: underline, overline, etc). Equivalent to CSS' text-decoration.

`text-decoration`

### No-wrap ​

`No-wrap`
To prevent the text from wrapping to the next line. Equivalent to CSS' white-space.

`white-space`

### Character case ​

`Character case`
To set the case of the text (for example: uppercase, lowercase, etc). Equivalent to CSS' text-transform.

`text-transform`

### Text shadows ​

`Text shadows`
To add a shadow to the text. Equivalent to CSS' text-shadow.

`text-shadow`

### Letter spacing ​

`Letter spacing`
To set the space between each letter of the text. Equivalent to CSS' letter-spacing.

`letter-spacing`

### Word spacing ​

`Word spacing`
To set the space between each word of the text. Equivalent to CSS' word-spacing.

`word-spacing`

### Text background ​

`Text background`
To set the background color of the text. Equivalent to CSS' background-color.

`background-color`

### Image ​

`Image`
This is where you can bind an image source, typically, when it comes from an external tool or API. Equivalent to HTML's src.

`src`

### Fit ​

`Fit`
To set how the image should be displayed (for example: cover, contain, etc). Equivalent to CSS' object-fit.

`object-fit`

### Overlay ​

`Overlay`
To set the color of the image overlay. Equivalent to CSS' background-color.

`background-color`

### Filters ​

`Filters`
To apply filters to the image (for example: grayscale, blur, etc). Equivalent to CSS' filter.

`filter`

### Items ​

`Items`
This is where you can bind a list of items to be displayed inside a container (like a div, columns, etc).


### Direction ​

`Direction`
To set the direction of the items (for example: horizontal, vertical, etc). Equivalent to CSS' flex-direction.

`flex-direction`

### Rows gap ​

`Rows gap`
To set the space between each row of items. Equivalent to CSS' grid-row-gap.

`grid-row-gap`

### Columns gap ​

`Columns gap`
To set the space between each column of items. Equivalent to CSS' grid-column-gap.

`grid-column-gap`

### Justify ​

`Justify`
To set how the items should be aligned horizontally (for example: left, center, right, etc). Equivalent to CSS' justify-content.

`justify-content`

### Alignment ​

`Alignment`
To set how the items should be aligned vertically (for example: top, center, bottom, etc). Equivalent to CSS' align-items.

`align-items`

### Reverse order ​

`Reverse order`
To reverse the order of the items. Equivalent to CSS' flex-direction.

`flex-direction`

### Push last to the end ​

`Push last to the end`
To push the last item to the end of the container. Equivalent to CSS' justify-content.

`justify-content`

### Display type ​

`Display type`
To set the display type of the items (for example: list, grid, etc). Equivalent to CSS' display.

`display`

### Presets ​

`Presets`
Set of predefined display types for columns. Equivalent to CSS' display.

`display`

## Text ​


### Sanitize ​

`Sanitize`
This is for when you bind a text to a data provided by the user, for example a comment you have register in the database.

This will escape special characters, so that you are not vulnerable to XSS attacks.

The option is not active by default because sometimes you want these characters to be interpreted (for example making some part of the text bold with markup).




## Sizing ​


### Width ​

`Width`
To set the width of the element. Equivalent to CSS' width.

`width`

### Height ​

`Height`
To set the height of the element. Equivalent to CSS' height.

`height`

### Max-width ​

`Max-width`
To set the maximum width of the element. Equivalent to CSS' max-width.

`max-width`

### Min-width ​

`Min-width`
To set the minimum width of the element. Equivalent to CSS' min-width.

`min-width`

### Max-height ​

`Max-height`
To set the maximum height of the element. Equivalent to CSS' max-height.

`max-height`

### Min-height ​

`Min-height`
To set the minimum height of the element. Equivalent to CSS' min-height.

`min-height`

## Spacing ​


### Padding ​

`Padding`
To set the padding of the element. Equivalent to CSS' padding.

`padding`

### Margin ​

`Margin`
To set the margin of the element. Equivalent to CSS' margin.

`margin`

## Display ​


### Alignment ​

`Alignment`
To set how the element should be aligned vertically (for example: top, center, bottom, etc). Equivalent to CSS' align-items.

`align-items`

### Display ​

`Display`
To set if an element should be displayed or not. Equivalent to CSS' display: none.

`display: none`
TIP

This is how you can hide an element on responsive mode or when a condition is met.


### Opacity ​

`Opacity`
To set the opacity of the element. Equivalent to CSS' opacity.

`opacity`

### Position ​

`Position`
To set the position of the element. Equivalent to CSS' position.

`position`

### Z axis ​

`Z axis`
To set the z-index of the element. Equivalent to CSS' z-index.

`z-index`

### Cursor ​

`Cursor`
To set the cursor of the element. Equivalent to CSS' cursor.

`cursor`

### Overflow ​

`Overflow`
To set the overflow of the element. Equivalent to CSS' overflow.

`overflow`

## Background ​


### Color ​

`Color`
To set the background color of the element. Equivalent to CSS' background-color.

`background-color`

### Element ​

`Element`
To set the background element (like and image or video) of the element. Equivalent to CSS' background.

`background`

## Borders & Shadows ​


### Borders ​

`Borders`
To set the borders of the element. Equivalent to CSS' border.

`border`

### Corner radius ​

`Corner radius`
To set the corner radius of the element. Equivalent to CSS' border-radius.

`border-radius`

### Shadows ​

`Shadows`
To set the shadows of the element. Equivalent to CSS' box-shadow.

`box-shadow`

## Advanced ​


### Transform ​

`Transform`
To set the transform of the element. Equivalent to CSS' transform.

`transform`

### Transition ​

`Transition`
To set the transition of the element. Equivalent to CSS' transition.

`transition`

### Perspective ​

`Perspective`
To set the perspective of the element. Equivalent to CSS' perspective.

`perspective`

## Custom CSS ​

Here, you can add custom CSS to the element. Equivalent to CSS' style.

`style`

## Binding Properties ​

Note that, you can bind the value of any CSS Property to another formula or variable. You can use this feature to manipulate the properties based on interactions elsewhere in the app, or even with workflows

