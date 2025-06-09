# Update ​


# Update ​

Update is a SQL operation that modifies existing records in a database table. When you update data, you can change the values stored in one or more columns for records that match specific conditions. Think of it like editing cells in a spreadsheet - you're changing existing values rather than adding or removing rows.

In the example below, we are using the Update row workflow that comes by default with WeWeb's data grid element and added a Supabase Update action:

`Update row`
`Update`


In our Update action, we:

`Update`
- selected the vehicles table, and
- mapped the id of the record we want to update in Supabase to the id of the record we edited in the data grid:

`vehicles`
`id`


Then we bound the mileage field in our Supabase table to the data grid event to send the value in the mileage column of our data grid:

`mileage`
`mileage`


And that's it!

If you switch to Preview mode, you will be update your Supabase table from your WeWeb Data Grid:



TIP

The way we mapped the values of the record to the Supabase fields we want to update is very specific to the Update row workflow of the data grid element, but you get the idea: you need to tell Supabase what record it should update and where it can find the new values.

`Update row`
In the case of the data grid element, this information can be found in the Event of the Update row workflow.

`Event`
`Update row`
