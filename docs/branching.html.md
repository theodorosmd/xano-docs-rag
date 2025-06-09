# Branching ​


# Branching ​

Branching allows you to create conditional logic flows in your workflows. At their core, these actions evaluate a condition you define - a value or formula that returns either true or false. The condition can compare values, check variables, or use any valid dynamic expression from your application. There are two types of branching:

- True/False split
- Multi-option split

`True/False split`
`Multi-option split`

## True/False split ​



Splits the workflow into two paths based on a condition:

- If condition is true, executes the "True" branch
- If condition is false, executes the "False" branch


## Multi-option split ​

The Multi-option split action lets you create multiple conditional paths in your workflow. Each path can handle different scenarios with their own set of actions.

`Multi-option split`

### Configuration ​

- Default branch: optional fallback if no conditions match
- Branches: add multiple conditions and their corresponding actions

`Default branch`
`Branches`

### Example: error handling ​

Here's how you can use it to handle different error types by changing a variable based on the condition:



```
├── When: invalid email
│     └── Then: Set specific error message
├── When: duplicate entry
│     └── Then: Set duplicate error message
└── Default Case:
      └── Set generic error message
```

`├── When: invalid email
│     └── Then: Set specific error message
├── When: duplicate entry
│     └── Then: Set duplicate error message
└── Default Case:
      └── Set generic error message`
TIP

Multi-option split is incredibly flexible - you can add as many branches as your logic requires. Use the zoom controls located at the bottom of the editor to manage visibility when building complex workflows with multiple branches. This makes it perfect for creating sophisticated decision trees and handling multiple scenarios in your application.

`Multi-option split`
