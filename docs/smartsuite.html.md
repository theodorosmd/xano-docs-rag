# SmartSuite ​


# SmartSuite ​

WARNING

SmartSuite's API is still in alpha. You might encounter issues when trying to use it in your project. Please refer to: https://help.smartsuite.com/en/articles/4356333-smartsuite-api-overview


## Connect a SmartSuite account ​

In order to get data from SmartSuite, you first need to add SmartSuite as a data source in WeWeb:



To find your SmartSuite API key and Workspace ID, follow the in-app "How to find it" instructions:




## Add a SmartSuite collection ​

Once you’ve connected a SmartSuite account to WeWeb, you will be able to create SmartSuite data collections in WeWeb:

At this stage, you have fetched the data from SmartSuite. It is available for use in WeWeb.

You can add frontend filters and pagination and display the data in your WeWeb project.


## Update and Delete SmartSuite data ​

You can update, and even delete, data in SmartSuite from WeWeb. To do this, you'll need to use the SmartSuite actions in your workflows.

For example, let's say that you bound a SmartSuite collection to a Datagrid in WeWeb. Then, you could set up the on row update and on row delete workflows this way:

`on row update`
`on row delete`
For the delete a record action, you just need to pass the ID of the record to delete.

`delete a record`

## How to Update Single and Multi-select Fields in SmartSuite? ​

SmartSuite has a specific format for single and multi-select fields. To help you update these fields, we've created a custom action that you can use in your workflows.

This action, named get field choices will return all the current available values for such a field. Then, when updating the record, you can pass the ID of the value you want to set using a lookup formula.

`get field choices`
`lookup`
Here's a video on how to use it:

