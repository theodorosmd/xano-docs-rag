# PostgreSQL functions ​


# PostgreSQL functions ​

PostgreSQL or database functions are built-in database tools that handle data tasks directly inside your database. Think of them like automatic helpers that can:

- Add up all your monthly sales
- Fix customer names that were entered with typos
- Create reports showing which products sold best last week
- And much more!

For example, when a customer clicks "View Sales Report" on your web app, it could call a PostgreSQL function named get_monthly_sales that instantly calculates and returns total sales for each month, instead of having to write complex code in your frontend to do these calculations.

`get_monthly_sales`
TIP

Supabase is built on PostgreSQL, a database system which uses SQL. SQL is a language for interacting with databases to get, delete, and update data using queries. A query is a command that tells the database what action to perform. In SQL, you can retrieve data from a table using the SELECT statement.

`SELECT`
if you run:

```
SELECT CustomerName, City FROM Customers;
```

`SELECT CustomerName, City FROM Customers;`
This query will:

- Retrieve the CustomerName and City columns from the Customers table.

`CustomerName`
`City`
`Customers`
It will return a list of all customer names and their corresponding cities stored in the table.


## Beyond basic queries ​

Let's imagine you’re building an app that helps track user activity by calculating important metrics based on three connected tables:

- logins: tracks when users log in.
- posts: tracks posts created by users.
- comments: tracks comments written by users.

`logins`
`posts`
`comments`
While you could use SELECT with multiple table joins to gather this information, it creates lengthy, complex queries that need to be repeated everywhere you need these metrics. Using a database function instead lets you write the logic once and reuse it by simply calling get_user_activity_stats(). This makes your code cleaner and easier to maintain, since any changes only need to be made in one place.

`SELECT`
`get_user_activity_stats()`
Like having a reusable report template, database functions give you:

- Single source of truth for your query logic
- Consistent data calculations and formatting
- Simpler code maintenance

This is what our function would look like:

```
CREATE OR REPLACE FUNCTION get_user_activity_stats(user_id INT)
RETURNS TABLE(logins INT, posts INT, comments INT) AS $$
BEGIN
    RETURN QUERY
    SELECT
        (SELECT COUNT(*) FROM logins WHERE user_id = user_id AND login_date >= NOW() - INTERVAL '30 days') AS logins,
        (SELECT COUNT(*) FROM posts WHERE user_id = user_id AND post_date >= NOW() - INTERVAL '30 days') AS posts,
        (SELECT COUNT(*) FROM comments WHERE user_id = user_id AND comment_date >= NOW() - INTERVAL '30 days') AS comments;
END;
$$ LANGUAGE plpgsq
```

`CREATE OR REPLACE FUNCTION get_user_activity_stats(user_id INT)
RETURNS TABLE(logins INT, posts INT, comments INT) AS $$
BEGIN
    RETURN QUERY
    SELECT
        (SELECT COUNT(*) FROM logins WHERE user_id = user_id AND login_date >= NOW() - INTERVAL '30 days') AS logins,
        (SELECT COUNT(*) FROM posts WHERE user_id = user_id AND post_date >= NOW() - INTERVAL '30 days') AS posts,
        (SELECT COUNT(*) FROM comments WHERE user_id = user_id AND comment_date >= NOW() - INTERVAL '30 days') AS comments;
END;
$$ LANGUAGE plpgsq`
If the code above seems a bit intimidating, don't fret, let's go through it line by line:

```
CREATE OR REPLACE FUNCTION get_user_activity_stats(user_id INT)
```

`CREATE OR REPLACE FUNCTION get_user_activity_stats(user_id INT)`
This line creates a new function named get_user_activity_stats that needs a user ID number to work.

`get_user_activity_stats`
```
RETURNS TABLE(logins INT, posts INT, comments INT) AS $$
```

`RETURNS TABLE(logins INT, posts INT, comments INT) AS $$`
This tells us what information we'll get back: a table with three numbers - count of logins, posts, and comments.

```
BEGIN
    RETURN QUERY
```

`BEGIN
    RETURN QUERY`
- BEGIN tells the database "start following these instructions".
- RETURN QUERY is like saying "collect and bring back this information."

`BEGIN`
`RETURN QUERY`
```
(SELECT COUNT(*) FROM logins WHERE user_id = user_id AND login_date >= NOW() - INTERVAL '30 days') AS logins,
```

`(SELECT COUNT(*) FROM logins WHERE user_id = user_id AND login_date >= NOW() - INTERVAL '30 days') AS logins,`
This counts how many times the user logged in during the last 30 days

```
(SELECT COUNT(*) FROM posts WHERE user_id = user_id AND post_date >= NOW() - INTERVAL '30 days') AS posts,
```

`(SELECT COUNT(*) FROM posts WHERE user_id = user_id AND post_date >= NOW() - INTERVAL '30 days') AS posts,`
This counts how many posts they made in the last 30 days

```
(SELECT COUNT(*) FROM comments WHERE user_id = user_id AND comment_date >= NOW() - INTERVAL '30 days') AS comments;
```

`(SELECT COUNT(*) FROM comments WHERE user_id = user_id AND comment_date >= NOW() - INTERVAL '30 days') AS comments;`
This counts their comments from the last 30 days

```
END;
$$ LANGUAGE plpgsql;
```

`END;
$$ LANGUAGE plpgsql;`
This just tells the database we're done writing our function.

If you call the function with user_id = 123, an example output could be:

`user_id = 123`
If we tried to achieve the same for three users using only SELECT statements, our code would look like this:

`SELECT`
```
-- Stats for User 123
SELECT
    (SELECT COUNT(*) FROM logins WHERE user_id = 123 AND login_date >= NOW() - INTERVAL '30 days') AS logins,
    (SELECT COUNT(*) FROM posts WHERE user_id = 123 AND post_date >= NOW() - INTERVAL '30 days') AS posts,
    (SELECT COUNT(*) FROM comments WHERE user_id = 123 AND comment_date >= NOW() - INTERVAL '30 days') AS comments;

-- Stats for User 456
SELECT
    (SELECT COUNT(*) FROM logins WHERE user_id = 456 AND login_date >= NOW() - INTERVAL '30 days') AS logins,
    (SELECT COUNT(*) FROM posts WHERE user_id = 456 AND post_date >= NOW() - INTERVAL '30 days') AS posts,
    (SELECT COUNT(*) FROM comments WHERE user_id = 456 AND comment_date >= NOW() - INTERVAL '30 days') AS comments;

-- Stats for User 789
SELECT
    (SELECT COUNT(*) FROM logins WHERE user_id = 789 AND login_date >= NOW() - INTERVAL '30 days') AS logins,
    (SELECT COUNT(*) FROM posts WHERE user_id = 789 AND post_date >= NOW() - INTERVAL '30 days') AS posts,
    (SELECT COUNT(*) FROM comments WHERE user_id = 789 AND comment_date >= NOW() - INTERVAL '30 days') AS comments;
```

`-- Stats for User 123
SELECT
    (SELECT COUNT(*) FROM logins WHERE user_id = 123 AND login_date >= NOW() - INTERVAL '30 days') AS logins,
    (SELECT COUNT(*) FROM posts WHERE user_id = 123 AND post_date >= NOW() - INTERVAL '30 days') AS posts,
    (SELECT COUNT(*) FROM comments WHERE user_id = 123 AND comment_date >= NOW() - INTERVAL '30 days') AS comments;

-- Stats for User 456
SELECT
    (SELECT COUNT(*) FROM logins WHERE user_id = 456 AND login_date >= NOW() - INTERVAL '30 days') AS logins,
    (SELECT COUNT(*) FROM posts WHERE user_id = 456 AND post_date >= NOW() - INTERVAL '30 days') AS posts,
    (SELECT COUNT(*) FROM comments WHERE user_id = 456 AND comment_date >= NOW() - INTERVAL '30 days') AS comments;

-- Stats for User 789
SELECT
    (SELECT COUNT(*) FROM logins WHERE user_id = 789 AND login_date >= NOW() - INTERVAL '30 days') AS logins,
    (SELECT COUNT(*) FROM posts WHERE user_id = 789 AND post_date >= NOW() - INTERVAL '30 days') AS posts,
    (SELECT COUNT(*) FROM comments WHERE user_id = 789 AND comment_date >= NOW() - INTERVAL '30 days') AS comments;`
We are repeating SELECT many times. This approach is prone to errors and hard to maintain, hence the usefulness of database functions.

`SELECT`
Learn more about how to create database functions here

TIP

The example above (consolidating complex queries) is popular because it's a common pain point, but database functions are really a Swiss Army knife for database operations. They're particularly valuable when you need consistent behavior across different applications or users accessing the same database.

A couple of additional use cases include but are not limited to:

- Automating business logic: automatically assigning tickets when a new issue is created.
- Trigger-based functions for event handling: when a user likes a post, update the likes_count in a summary table.

`likes_count`

## Call a Postgres function ​

The Call a Postgres function action in WeWeb, available after installing the Supabase plugin, lets you execute database functions directly from your application.

`Call a Postgres function`


Consider a customer service ticket management app with these connected tables:

- tickets: basic ticket info.
- ticket_status_history: how many times the ticket was reopened.
- ticket_comments: how many comments are waiting for a response.
- agents: how many tickets the agent is handling.
- departments: SLA rules for the ticket.

`tickets`
`ticket_status_history`
`ticket_comments`
`agents`
`departments`
We could create a function to return ticket stats. For example, you might want to know:

- The total number of tickets in the system
- How many tickets are currently open vs closed
- The number of high-priority tickets that need attention
- The average time it takes to resolve tickets

Once you are done writing the code for the function, you can add the Call a Postgres function action to call that function.

`Call a Postgres function`
To verify your Postgres function execution, use the Logs tab to inspect the returned values:

`Logs`


WARNING

If Row-Level Security (RLS) is enabled, your function might not return data unless you explicitly allow it.


## PostgreSQL functions vs. Edge Functions ​

It's easy to mix up database functions with Edge Functions. Database functions operate directly within your database, working on your data at its source. On the other hand, edge functions run on distributed servers located closer to users, managing tasks such as authentication, data transformations, and integrations with external services like payment processors.

Here is a comparison table:

