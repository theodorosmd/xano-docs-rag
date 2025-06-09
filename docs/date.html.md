# Date formulas ​


# Date formulas ​

Date formulas are useful to manipulate date objects inside WeWeb.


## Date plugin ​

In order to access no-code date formulas, you'll first need to add the Date extension plugin:

`Date`


TIP

When you install the Date plugin, we add the Day.js library to your WeWeb project.

`Date`
It's a small 2kB library but we don't include it by default because not every project needs to work with dates and we don't want to add the weight of the library on projects that don’t need it.

Once you have added the Date plugin, you'll be able to see all the related no-code formulas in the explorer tab:

`Date`



## Favorite date format ​

In order to display dates in a uniform way throughout your project, you can configure your favorite date format at plugin level:



TIP

Working with dates can be tricky at first. If you get stuck on formatting, we recommend you to through this article on the ISO date format.


## date ​

If you use date in a formula with no parameters, you will get the current date and time in Coordinated Universal Time (i.e. the UTC timezone).

`date`
The no-code date formula can take the same parameters as the JavaScript newDate() function.

`date`
`newDate()`

## dateRealtime ​

Same as date, dateRealtime will return the current date and time in Coordinated Universal Time (i.e. the UTC timezone).

`date`
`dateRealtime`
That date, however, will be updated every second in real-time:




## toDateISO ​

This formula allows you to set a date in ISO format:

- the first parameter of the formula should be a date,
- the second parameter is the format you want to display the date in



TIP

If you have configured a favorite date format at plugin level, the second parameter of the toDateISO formula is optional:

`toDateISO`



## formatDate ​

This formula allows you to format a date:



In the example above, you see:

- first we start with a date formula that returns a date in ISO format,
- then we wrap the formatDate formula around it to display the date in the preferred format we configured at plugin level,
- we add a second parameter to the formatDate formula to display the date in a different format,
- finally, we change the display language to Spanish.

`date`
`formatDate`
`formatDate`

## toTime ​

This formula calculates the time between now and X, and returns the information in text format:



In the toTime formula, the relative time compares the date now, to the date in the first parameter.

`toTime`
For example:

- Today, August 23rd, 2023 was "2 months ago"
- Today, August 23rd, 2024 is "in 10 months"

The formula will accept the following parameters:

- a date in ISO format (required),
- whether to display the suffix or not (optional), and
- the language in which the text should be displayed (optional)


## fromTime ​

This formula calculates the time between X and now, and returns the information in a text format.

In the fromTime formula, the relative time compares the date in the first parameter, to the date now.

`fromTime`
For example:

- On August 23rd, 2023, today was "in 2 months"
- On August 23rd, 2024, today will be "10 months ago"

The formula will accept the following parameters:

- a date in ISO format (required),
- whether to display the suffix or not (optional), and
- the language in which the text should be displayed (optional)


## compareDate ​

This formula allows you to compare two dates:



You can count the number of:

- years (year or y),
- quarters (quarter or Q),
- months (month or M),
- weeks (week or w), etc.

`year`
`y`
`quarter`
`Q`
`month`
`M`
`week`
`w`
TIP

When you hover over a no-code formula name in the WeWeb, you can view tooltips on what parameters and values it expects.

By default, the result of the compareDate formula will be a round number.

`compareDate`
If the floating parameter is true, you can see decimals in the calculation. For example, there are 4.6 months between November 4th, 2023 and March 23rd, 2024:

`floating`
`true`



## toTimestamp ​

The toTimestamp formula expects a date in ISO format and will return the timestamp value for that date in a number format:

`toTimestamp`



## getBrowserTimezone ​

The getBrowserTimezone formula will return the timezone your user's browser is in.

`getBrowserTimezone`



## convertDateTimezone ​

The convertDateTimezone formula allows you to display a different date and time depending on the user's timezone.

`convertDateTimezone`
The first parameter must be a date that contains time and timezone information.

For example, the date formula returns the date and time in the UTC timezone. Here, we are converting the current date and time to the date and time in New York:

`date`


By default, or if you add false as a third parameter, the result will show the date and time in the new timezone.

`false`
You can, however, choose to preserve the date and time of the original timezone:




## formatDateTimezone ​

The formatDateTimezone formula allows you to take a date provided in ISO format, and display it:

`formatDateTimezone`
- in the format of your choice, e.g. "MMMM D, YYYY - HH:MM"
- converted to the timezone of your choice, e.g. "America/Mexico_City"
- in the language of your choice, e.g. es for Spanish

`"MMMM D, YYYY - HH:MM"`
`"America/Mexico_City"`
`es`



## Troubleshooting ​

Working with dates can be tricky at first.

Here are a few things to consider when a date formula is not behaving as you would expect:

- ISO date values and date formats should be strings. Make sure to enclose them in between quotes "like_this"
- Timestamp values should be numbers. If you are storing timestamps in a text format, use the toNumber formula around it to convert it so the date formulas can work with it
- ISO date formats are easy to mess up. When in doubt, check out this article with numerous examples of ISO date formats

ISO date values and date formats should be strings. Make sure to enclose them in between quotes "like_this"

`"like_this"`
Timestamp values should be numbers. If you are storing timestamps in a text format, use the toNumber formula around it to convert it so the date formulas can work with it

`toNumber`
ISO date formats are easy to mess up. When in doubt, check out this article with numerous examples of ISO date formats

