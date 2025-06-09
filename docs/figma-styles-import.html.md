# Import Figma styles ​


# Import Figma styles ​


## Add WeWeb plugin in Figma ​

In order to import styles from Figma or any other source, you have to install our plugin in Figma:



LOOKING TO IMPORT A FIGMA DESIGN?

The present article is about importing Figma styles to a WeWeb library. With our plugin, you can also import Figma designs on a WeWeb page.

Learn how to import a Figma design.


## Export Figma style ​

In your Figma project, open the plugin and select whether you want to import colors or typography:



Clicking on generate will store the exported styles to your clipboard.




## Import style to WeWeb ​

To import the copied styles to WeWeb, navigate to the Library panel and click on the Figma icon.

`Library`


All you have to do next is paste your output from Figma to the input and click on Import styles:

`Import styles`


After you receive message of a successful import, you will find your styles in the library:




## Importing from other sources ​

If importing typography from other sources, input needs to be formatted as displayed in the sample input below.


### Typography ​

```
[
    {
        "type": "typo",
        "name": "Typography/Heading 1",
        "fontSize": "64px",
        "lineHeight": "72px",
        "fontWeight": "Medium"
    },
    {
        "type": "typo",
        "name": "Typography/Heading 2",
        "fontSize": "48px",
        "lineHeight": "56px",
        "fontWeight": "Semi Bold"
    },
    {
        "type": "typo",
        "name": "Typography/Heading 3",
        "fontSize": "32px",
        "lineHeight": "40px",
        "fontWeight": "Medium"
    }
]
```

`[
    {
        "type": "typo",
        "name": "Typography/Heading 1",
        "fontSize": "64px",
        "lineHeight": "72px",
        "fontWeight": "Medium"
    },
    {
        "type": "typo",
        "name": "Typography/Heading 2",
        "fontSize": "48px",
        "lineHeight": "56px",
        "fontWeight": "Semi Bold"
    },
    {
        "type": "typo",
        "name": "Typography/Heading 3",
        "fontSize": "32px",
        "lineHeight": "40px",
        "fontWeight": "Medium"
    }
]`

### Colors ​

```
[
    {
        "type": "color",
        "name": "Light/Background/bg",
        "value": "#ffffff"
    },
    {
        "type": "color",
        "name": "Light/Background/bg-secondary",
        "value": "#f7f7f7"
    },
    {
        "type": "color",
        "name": "Light/Background/bg-tertiary",
        "value": "#ebebeb"
    }
]
```

`[
    {
        "type": "color",
        "name": "Light/Background/bg",
        "value": "#ffffff"
    },
    {
        "type": "color",
        "name": "Light/Background/bg-secondary",
        "value": "#f7f7f7"
    },
    {
        "type": "color",
        "name": "Light/Background/bg-tertiary",
        "value": "#ebebeb"
    }
]`
