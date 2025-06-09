# Fetch collection ​


# Fetch collection ​

The Fetch collection action allows you to manually trigger data fetching for any collection in WeWeb. While collections can fetch data automatically when a page loads, there are times when you need more control over when and how data is refreshed.

`Fetch collection`
When you add a Fetch collection action to a workflow, you select which collection to fetch. Upon triggering, the action makes a fresh request to your data source (like REST API, Supabase, or Xano) and updates your collection with the latest data.

`Fetch collection`

## A common use case ​

A modal display scenario is a perfect example - rather than loading all possible data when your page loads, you might want to fetch specific collection data only when a user opens a modal. This improves initial page performance while ensuring data is fresh when needed.

