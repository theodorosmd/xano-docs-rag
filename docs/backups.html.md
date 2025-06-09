# Backups ​


# Backups ​

In the Backups tab of a project, you can see all the different versions of the Editor that you can potentially rollback to.

`Backups`

## Backups tab ​

From your workspace dashboard, you can access a project's backups by going to the project's Settings > Backups:

`Settings`
`Backups`


In the example above, you can see:

- we have several commits of the project over two different days
- there are many commits are automatic, and
- there is one manual commit with a custom message
- some commits reference a version in their name (v1) and (v2)

`(v1)`
`(v2)`
We can:

- hide automatic commits,
- search for a specific commit,
- preview a specific version of the Editor, and
- rollback to a specific version of the Editor.


## Automatic commits ​

WeWeb generates automatic commits of your project Editor:

- once a day if you're on a Starter plan,
- once an hour if you're on a Scale or Enterprise plan, and
- every time you publish your app in staging or in production.

TIP

The commits that are linked to a publication will display the publication version in their name.

In the example below, in the Deployments tab, you can see we published a v3 of our app in staging. As a result, an automatic commit of the Editor is available in the Backups tab (with the (v3) reference in its name):

`Deployments`
`Backups`
`(v3)`



## Manual commits ​

When you're inside a project, you can create a manual commit of the Editor with a custom message to describe the update by going to the Commit button inside the Editor:

`Commit`


