# Update collection ​


# Update collection ​

The Update collection action optimizes UI updates after back-end data modifications by eliminating the traditional pattern of making an API request followed by a fetch collection action to refresh the UI.

`Update collection`
WARNING

At present, Update collection will only work if your collection is a list. It will not work if your collection is an object. For example, if your API returns an object like so { id: 1, name: "item1" } or any other format that isn't an array/list of items, the action may not behave as expected. Make sure your data is always structured as a list of items.

`Update collection`
`{ id: 1, name: "item1" }`

## The problem it solves ​

Previously in WeWeb, when modifying data through an API request (like deleting a user or updating a record), you had to follow a two-step process:

- Make an API request to modify back-end data
- Fetch the entire collection again to update the UI



This approach had some drawbacks:

- Required two server requests
- Created unnecessary network traffic
- Increased server load

Ultimately, these meant potentially unnecessary load times for the user of your app.


## The solution ​

The Update collection action enables immediate UI updates by directly modifying the collection after a successful API request, eliminating the need to re-fetch the collection. This means you can:

`Update collection`
- Immediately update your collection
- Update your UI instantly
- Use just a single API request to update your back-end data




### Use cases ​

- Immediate user feedback
- Temporary data views
- Performance optimization
- Enhanced user experience
- Client-side data manipulation

WARNING

This action only changes what you see on the screen temporarily. These changes will be lost if you refresh the page. To permanently save your changes to your database, you must always use this action together with an API request.


## Update types ​


### Replace All ​

The Replace All update type overwrites the entire content of a collection with new data. In the example below, we are setting the collection to have a text value of "No collection" and using the Log action to display it in the editor's Logs tab. This will show you the updated content of the collection after it's been replaced:

`Replace All`
`Log`
`Logs`



### Update ​

Updates specific records in a collection while preserving the rest of the collection data.




#### Configuration ​

Position Type

- By index: Update by position (0 = first record)
- By id: Update by unique identifier

`By index`
`By id`
Merge

- ON: Updates only specified fields, keeps others
- OFF: Replaces entire record with new data

`ON`
`OFF`
Data

- Accepts an object: {"fieldName": "newValue"}
- Defines what to update in the record

`{"fieldName": "newValue"}`

#### Example with Merge ON: ​

When modifying records with Merge ON, you can update specific fields while preserving other data:

`ON`
- Collection : characters
- Position: 1 (second record)
- Merge: ON
- Data: {"status": "Dead"}

`characters`
`ON`
`{"status": "Dead"}`



#### Example with Merge OFF: ​

With Merge OFF, the provided data completely replaces the existing record:

`Merge`
`OFF`
- Collection: characters
- Position: 1 (second record)
- Merge: OFF
- Data: {"status": "Dead"}

`characters`
`OFF`
`{"status": "Dead"}`



### Insert ​

The Insert type adds a new record to your collection at a specified position (index), allowing you to temporarily add data while preserving existing records.

`Insert`


TIP

The Data property for all update types except Delete must match what's in your collection:

`Data`
`Delete`
- For simple values (text, numbers):

- Use the same type of value (example: for a collection of texts, provide a text value).

- For objects:

- With Merge ON: Provide just the fields you want to update
- With Merge OFF: Provide all fields since everything will be replaced

`ON`
`OFF`

### Delete ​

The Delete type removes a single record from your collection based on position or ID, leaving all other records unchanged.

`Delete`

## Refresh filters and sort ​

Refresh Filters and Refresh Sort control whether collection settings are reapplied after updating data.

`Refresh Filters`
`Refresh Sort`
Filters

- ON: items that no longer match your filters are automatically removed from the collection after your update
- OFF: items stay in the collection view until manual refresh, even if they no longer match filters

`ON`
`OFF`
Sort

- ON: items automatically move to their new positions when sorting values change
- OFF: items maintain their current positions regardless of value changes

`ON`
`OFF`
