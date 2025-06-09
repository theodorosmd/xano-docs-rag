# NPM ​


# NPM ​


## Add plugin ​

To start working with npm packages in your project, go to Plugins > Extensions:

`Plugins`
`Extensions`


This plugin will allow you to load popular utility libraries from npm and utilize them directly in the editor.


## Plugin limitations ​

Any type of npm package can be installed, as long as it:

- is available on unpkg.com, and
- is packed in a UMD file,
- adds an instance to the window, and
- correctly instructs unpkg about what file to serve.

However, it's crucial to understand that not all loaded packages will be functional.

For the loaded library to be usable, it must be registered in the window. This import method is unique to each library, even though most libraries utilize this method.

After adding a library, you must specify the name of the instance it exposes. This allows weweb to establish a connection and incorporate it into the no-code interface.

In the example provided, the xlsx (or SheetJS) library can be accessed through the XLSX instance (in uppercase):



Most of the time, you'll find the instance name in the library documentation.


## E.g. parse a CSV ​


### Code snippets ​

If you'd like to reproduce the exact same use case, here are the code snippets we used:


#### users collection ​

`users`
```
return [
  { user: "jane", age: 28, active: true },
  { user: "barney", age: 25, active: true },
  { user: "fred", age: 40, active: false },
];
```

`return [
  { user: "jane", age: 28, active: true },
  { user: "barney", age: 25, active: true },
  { user: "fred", age: 40, active: false },
];`

#### csv variable ​

`csv`
```
Country,Population (Millions),Area (Square Kilometers)
United States,331.4,9,525,067
Canada,37.8,9,984,670
Brazil,212.6,8,515,767
Australia,25.8,7,692,024
China,1443.7,9,596,961
India,1393.4,3,287,263
Russia,145.9,17,125,191
United Kingdom,67.1,242,495
Germany,83.1,357,022
France,67.1,551,695
```

`Country,Population (Millions),Area (Square Kilometers)
United States,331.4,9,525,067
Canada,37.8,9,984,670
Brazil,212.6,8,515,767
Australia,25.8,7,692,024
China,1443.7,9,596,961
India,1393.4,3,287,263
Russia,145.9,17,125,191
United Kingdom,67.1,242,495
Germany,83.1,357,022
France,67.1,551,695`

## E.g. generate a QR code ​

In this video, Ray Deck of StateChange uses WeWeb's NPM plugin to build a QR code generator:

