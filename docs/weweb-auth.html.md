# WeWeb Auth ​


# WeWeb Auth ​


## Plugin limitations ​

At WeWeb, we specialize in frontend development. The WeWeb Auth plugin was built on top of Amazon Cognito to help you build a proof-of-concept app with basic authentication needs.

WARNING

The WeWeb Auth plugin is helpful to test an idea inside the WeWeb Editor or with a small user base on a published app.

It is not intended to build a web-app that scales with a large user base or complex roles and permissions.

Plugin limitations include:

- the number of user signup emails you can send is limited to 20/day.
- the number of password recovery emails you can send is limited to 20/day.
- the list of users cannot be synced with backend.

To develop a secure web-app that scales, we recommend integrating an external authentication system, using:

- one of our native integrations (e.g. Xano Auth, Supabase Auth, Auth0), or
- one of our backend-agnostic plugins (e.g. token-based auth, OpenID).


# WeWeb authentication ​

You can use WeWeb's native authentication system to build a proof-of-concept app with basic authentication needs.

WARNING

The video was recorded before the latest WeWeb UI update but the logic remains the same. If you're unsure where to find something in the new interface of the WeWeb editor, you can see what changed here.


## Add the plugin ​

To add WeWeb Auth, go to Plugins > Authentication > WeWeb Auth.

`Plugins`
`Authentication`
`WeWeb Auth`
Leave the default Configuration options and choose the page where users are redirected when they are not signed in. For example, a login page:

`Configuration`


TIP

Note that, if you click on the Configuration options, you'll see the template emails we send out when you invite new users to join your app. If you'd like to change those template emails, please use the contact us link to let us know.

`Configuration`
`contact us`
WARNING

If you remove the WeWeb Auth plugin from your project, it will delete all users, roles, and groups from WeWeb. You will not be able to retrieve this information after removing the plugin.


## Manage users ​

In the Auth panel, you can add users one by one manually or import a CSV file with a list of users:

`Auth`



### Add Users ​

Attributes The email address is required. All other attributes are optional.

Note that, for now, you can only add string attributes. So if you select the image attribute, you will need to pass it a URL in string format.

`image`
Password For each user, you can generate a password or set one manually. If you set one manually, it will need to be at least 6 characters long.

Invitation email Here you decide if you want to send an invitation email to the user or not.


### Update user ​

In the Auth > Users sub-menu, you can select a user to edit their info, attributes, password, and user roles.

`Auth`
`Users`
Note that, while you can update a user's password, you cannot see their current password for obvious security and privacy reasons.

You can also:

- Block a user. Blocked users will not be able to authenticate to your WeWeb app.
- Unblock a blocked user.
- Copy a user's ID.
- Delete a user. Deleted users will not be able to authenticate to your WeWeb app.




## User roles & user groups ​

To assign a role to a user, go to Auth > Users and select the user you want to assign a role to:

`Auth`
`Users`


To gate content in WeWeb based on user roles and permissions, you will need to:

- open the Auth panel,
- go to the Roles tab,
- create user roles,
- create user groups, and
- restrict access to pages based on user groups.

`Auth`
`Roles`



### How user groups work ​

A user group is a combination of user roles.

Let's say you're building a web app for a car rental company. You could have 3 user roles:

- Admin, for employees,
- Customers, and
- Premium, for employees and loyal customers.

`Admin`
`Customers`
`Premium`
And 2 user groups:

- Admin, that would allow you to gate content so non-employees can't access it
- Premium customer, that would display the best cars to premium customers

`Admin`
`Premium customer`
WARNING

It's important to understand that a user needs to have all the roles listed in the user group.

In the example below, the members of the Premium customer user group must have both the Customer and the Premium roles associated with their user profile:

`Premium customer`
`Customer`
`Premium`



## Private pages ​

One of the main uses for user groups is to gate content.

When you setup the WeWeb Auth plugin, an Authenticated users user group will be created by default even if you don't define additional user groups.

`WeWeb Auth`
`Authenticated users`
You can use this user group to restrict access to a page:



If you have defined user roles, you can add user groups that refer to those user roles and restrict access to pages further:




## Signup, login, logout flows ​

Once you have added the WeWeb Auth plugin, you'll want users to be able to:

- signup,
- login,
- logout,
- change their password,
- update their user profile, etc.

You can do this with dedicated WeWeb Auth workflow actions:



You can build your own designs or use the WeWeb Auth UI elements in the Add menu to get started:

`WeWeb Auth`
`Add`


