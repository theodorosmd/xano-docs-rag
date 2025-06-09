# Logs ​


# Logs ​

In the Navigator of the WeWeb editor, you can open the Logs tab in the Debugging panel to see what is happening in your app:

`Navigator`
`Logs`
`Debugging`


In the example above, you can see what happens when you open a project in the WeWeb editor:

- the application is started,
- collections start being fetched,
- the authenticated user value is set,
- data from collections are fetched, etc.

The Logs panel is helpful:

`Logs`
- to understand what's happening in a workflow that is not behaving as expected, and
- to improve the UX and performance of a page by looking at what happens when the user arrives on the page.


## Workflow debugging ​

When you are working with workflows, it can be helpful to look at the logs of what's happening when you execute the workflow:



In the example above, we can see that:

- our backend returned an error,
- the error was caused by a user trying to login with invalid credentials,
- the workflow moved on to the error branch as a result, and
- started going through the actions in the error branch.

TIP

Before testing a workflow, try clearing the logs to get a nice clean view of what is happening:




## UX & performance audit ​

When you develop an app, things can start getting complex quickly.

In order to scale your projects, it helps to audit the UX and performance of your pages on a regular basis.

For example, you can use the Logs panel to check that:

`Logs`
- only essential data collections are fetched on page load, and
- variables are updated in the order you would expect.


### Example 1 - flow of actions ​

If a displayError variable is updated before an errorMessage variable, you might see an unwanted blink before the text of the errorMessage is updated.

`displayError`
`errorMessage`
`errorMessage`
Changing the order of these actions will greatly improve the experience of your users.


### Example 2 - collections fetched ​

On one page, we couldn't figure out why the list of jobs always appeared as empty on page load, only to be populated when the user interacted with filters on the page.

It turns out we were fetching an old collection on page load (jobs instead of jobs_):

`jobs`
`jobs_`


The jobs_ collection was only fetched On change when the user interacted with a filter on the page.

`jobs_`
`On change`
After identifying the problem, we were able to get rid of the old collection (decluttering our developer environment along the way) and optimize the loading of the jobs_ collection.

`jobs_`
