# Insert ​


# Insert ​

Insert is a SQL operation that adds new records to a database table. When you insert data, you create one or more new rows containing values for specified columns. Each insert operation can add a single record or multiple records at once, similar to adding new rows to a spreadsheet. All new records must follow the table's rules for required fields and data types.

If you have installed the Supabase data source plugin, you will have access to the Supabase Database | Insert action in workflows:

`Database | Insert`


In the example above, we are inserting one row in the cars table.

`cars`
WARNING

By default Supabase tables have RLS (Row-Level Security) enabled. Before you insert a record in a Supabase table, make sure that table has the correct INSERT policies.

`INSERT`
If the table requires a user to be authenticated to insert a record, make sure you are logged in as a user of your app when you test your workflow in WeWeb.

If you try to create a record without the proper authorization, Supabase will return an error.

Learn more about implementing Supabase RLS policies.


## Single insert ​

With the Supabase insert action, you can create a Single record or Multiple records at once.

`Single`
`Multiple`
When creating a single new record in Supabase, all the table fields will be listed by default:



TIP

Fields with a placeholder that starts with Default: will be filled out automatically by Supabase if left empty.

`Default:`
You can choose to select only the fields that you need upon creation of the record:




## Multiple (bulk) insert ​

To insert multiple records at once, you have two options.

- Bind the Rows with a list of items

`Rows`


In the example above, we are creating two records with the same values for both the make and model fields.

`make`
`model`
- Click on Add item and bind each Row to an object

`Add item`
`Row`


TIP

When binding Rows, the Current value should be a list of items (i.e. an array of objects).

`Rows`
`Current value`
When binding a single item, i.e. a Row, the Current value should be a single object with key value pairs.

`Row`
`Current value`



## Return inserted rows ​

By default, when you successfully insert a new record, Supabase will simply return a success message.

Depending on your use case, you may want Supabase to include the row(s) just created in its response.

To achieve this, you will need to enable the Return inserted rows option when configuring the insert action in WeWeb:

`Return inserted rows`


WARNING

If you enable this option, make sure you are testing the workflow with a user that has the rights to SELECT data from this table.

`SELECT`
Otherwise, you will get an error because you are trying to read data without being authorized to do so.

Learn more about implementing Supabase RLS policies.


## Using explain ​

EXPLAIN is a PostgreSQL command that can help you understand and optimize how your queries are performing.

`EXPLAIN`
This is an advanced backend feature that we recommend learning through the user documentation of Supabase and its underlying technology PostgreSQL.

