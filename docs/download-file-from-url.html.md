# Download file from URL ​


# Download file from URL ​

The Download file from URL action allows you to trigger file downloads without opening a new tab.

`Download file from URL`
You can pass two parameters:

- the URL of the file to download (required)
- the name of the file to download (optional)


## File URL (required) ​

This is a required field and implies that you know where the file is hosted.

In the example below, we bound to the file URL returned by our backend:



TIP

Notice in the example above that we bound to the url field, not the vault field of the image object. This is because the vault value is a relative path that is missing the domain where the file is hosted.

`url`
`vault`
`image`
`vault`
To check that you are binding to the correct URL, paste the URL in a new tab in your browser. You should be able to see the file as we do here:




## File name (optional) ​

Here you can bind the name of the file that will be downloaded on your user's computer:



This field is optional. If you leave it empty, a random name will be generated (e.g. 50700faa-3ba6-4f97-8bc8-a9476711f694.jpeg)

`50700faa-3ba6-4f97-8bc8-a9476711f694.jpeg`
WARNING

You can leave the File name field empty but if you do add a file name, it must include the file extension (e.g. .pdf, .png, .jpg, etc)

`File name`
`.pdf`
`.png`
`.jpg`
