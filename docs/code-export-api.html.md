# WeWeb Public API ​


# WeWeb Public API ​

The WeWeb Public API enables customers to automate and streamline their deployment processes for WeWeb projects.

This API is designed for organizations managing multiple WeWeb applications across various domains or server instances.


## Key benefits ​

- Automated deployments: integrate WeWeb projects into your CI/CD pipelines.
- Version control: programmatically manage different versions of your WeWeb applications.
- Multi-environment support: easily deploy to staging and production environments.
- Scalability: efficiently manage deployments across multiple domains or server instances.
- Customized workflows: tailor the deployment process to fit your organization's specific needs.

The WeWeb Public API offers significant productivity gains for teams handling complex deployment scenarios.

Instead of manually downloading the application code and/or then manually deploying it to a web server running on your infrastructure, you can trigger custom deployment scripts from within the WeWeb Editor.

Create a fully automated DevOps environment

By leveraging this API, you can create a fully automated DevOps environment to reduce manual tasks, minimize human error, and ensure consistent deployments across your infrastructure.

This documentation provides detailed information on authentication, available endpoints, and typical usage patterns to help you integrate WeWeb deployments into your existing systems and workflows.

WARNING

The WeWeb Public API has a rate limit of 3 calls per seconds and will return 429 Too many requests error if the limit is hit.

`429 Too many requests error`

## Access to WeWeb Public API ​

Please contact the WeWeb team to get access to WeWeb Public API.


## Authentication ​

WeWeb Public API authentication is done using an Authorization header in every requests.

`Authorization`
The value of this header should be Bearer <YOUR WORKSPACE PRIVATE KEY>.

`Bearer <YOUR WORKSPACE PRIVATE KEY>`
You workspace Private Key can be found under the Settings tab in your workspace.

`Settings`
You can generate a new Private Key at any time but this will invalidate the old one.

Example : headers: {"Authorization": "Bearer WW-PRIVATE-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"}

`headers: {"Authorization": "Bearer WW-PRIVATE-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"}`

## Available requests ​

The WeWeb Public API allows you to make the following requests:

- Method: POST
- URL: https://api.weweb.io/public/v1/workspaces/{{:workspaceId}}/projects/{{:projectId}}/deploy:workspaceId can be found in the URL of the workspace:projectId can be found in the URL of the project
- :workspaceId can be found in the URL of the workspace
- :projectId can be found in the URL of the project
- Data:
- env [REQUIRED] : accepts values production or staging and defines the target of the deployment. Deploying to production will also deploy to staging.
- commit [OPTIONAL] : String that will be used as the commit info.
- rawZip [OPTIONAL] : accepts values true or false and defines if the deployment generates a ZIP containing raw project files.
- builtZip [OPTIONAL] : accepts values true or false and defines if the deployment generates a ZIP containing built project files.
- githubEnabled [OPTIONAL] : accepts values true or false and defines if the deployment pushes raw project files to the configured Github repository.
- Returns:

Method: POST

`POST`
URL: https://api.weweb.io/public/v1/workspaces/{{:workspaceId}}/projects/{{:projectId}}/deploy

`https://api.weweb.io/public/v1/workspaces/{{:workspaceId}}/projects/{{:projectId}}/deploy`
- :workspaceId can be found in the URL of the workspace
- :projectId can be found in the URL of the project

`:workspaceId`
`:projectId`
Data:

env [REQUIRED] : accepts values production or staging and defines the target of the deployment. Deploying to production will also deploy to staging.

`env`
`production`
`staging`
`staging`
commit [OPTIONAL] : String that will be used as the commit info.

`commit`
rawZip [OPTIONAL] : accepts values true or false and defines if the deployment generates a ZIP containing raw project files.

`rawZip`
`true`
`false`
builtZip [OPTIONAL] : accepts values true or false and defines if the deployment generates a ZIP containing built project files.

`builtZip`
`true`
`false`
githubEnabled [OPTIONAL] : accepts values true or false and defines if the deployment pushes raw project files to the configured Github repository.

`githubEnabled`
`true`
`false`
Returns:

```
{
	"message": "Fetching data",    //Progress message
	"status": "deploying",    //Status of the deployment. Can be : deploying / deployed / failed
	"version": 33,    //Version of current publish
	"createdAt": "2022-12-12T16:13:47.142Z"    //Date of creation
}
```

`{
	"message": "Fetching data",    //Progress message
	"status": "deploying",    //Status of the deployment. Can be : deploying / deployed / failed
	"version": 33,    //Version of current publish
	"createdAt": "2022-12-12T16:13:47.142Z"    //Date of creation
}`
- Method: GET
- URL: https://api.weweb.io/public/v1/workspaces/{{:workspaceId}}/projects/{{:projectId}}/deploy/last:workspaceId can be found in the URL of the workspace:projectId can be found in the URL of the project
- :workspaceId can be found in the URL of the workspace
- :projectId can be found in the URL of the project
- Data: no data.
- Returns:

`GET`
`https://api.weweb.io/public/v1/workspaces/{{:workspaceId}}/projects/{{:projectId}}/deploy/last`
- :workspaceId can be found in the URL of the workspace
- :projectId can be found in the URL of the project

`:workspaceId`
`:projectId`
```
{
	"message": "Fetching data",    //Progress message
	"status": "deploying",    //Status of the deployment. Can be : deploying / deployed / failed
	"environment": "production",    //Target environment
	"version": 33,    //Version of current publish
	"logs": "deploy logs",    //Full logs of the deployment
	"rawZip": true,    //rawZip option entered on deploy start
    "builtZip": true,    //builtZip option entered on deploy start
    "githubEnabled": false,    //githubEnabled option entered on deploy start
	"createdAt": "2022-12-12T16:13:47.142Z"    //Date of creation
}
```

`{
	"message": "Fetching data",    //Progress message
	"status": "deploying",    //Status of the deployment. Can be : deploying / deployed / failed
	"environment": "production",    //Target environment
	"version": 33,    //Version of current publish
	"logs": "deploy logs",    //Full logs of the deployment
	"rawZip": true,    //rawZip option entered on deploy start
    "builtZip": true,    //builtZip option entered on deploy start
    "githubEnabled": false,    //githubEnabled option entered on deploy start
	"createdAt": "2022-12-12T16:13:47.142Z"    //Date of creation
}`
- Method: GET
- URL: https://api.weweb.io/public/v1/workspaces/{{:workspaceId}}/projects/{{:projectId}}/versions/{{:version}}/download/raw:workspaceId can be found in the URL of the workspace:projectId can be found in the URL of the project:version can be found in the Versions tab of the project or as a result of previous requests.
- :workspaceId can be found in the URL of the workspace
- :projectId can be found in the URL of the project
- :version can be found in the Versions tab of the project or as a result of previous requests.
- Data: no data.
- Returns: a ZIP file containing the Raw project files.

Method: GET

`GET`
URL: https://api.weweb.io/public/v1/workspaces/{{:workspaceId}}/projects/{{:projectId}}/versions/{{:version}}/download/raw

`https://api.weweb.io/public/v1/workspaces/{{:workspaceId}}/projects/{{:projectId}}/versions/{{:version}}/download/raw`
- :workspaceId can be found in the URL of the workspace
- :projectId can be found in the URL of the project
- :version can be found in the Versions tab of the project or as a result of previous requests.

`:workspaceId`
`:projectId`
`:version`
`Versions`
Data: no data.

Returns: a ZIP file containing the Raw project files.

- Method: GET
- URL: https://api.weweb.io/public/v1/workspaces/{{:workspaceId}}/projects/{{:projectId}}/versions/{{:version}}/download:workspaceId can be found in the URL of the workspace:projectId can be found in the URL of the project:version can be found in the Versions tab of the project or as a result of previous requests.
- :workspaceId can be found in the URL of the workspace
- :projectId can be found in the URL of the project
- :version can be found in the Versions tab of the project or as a result of previous requests.
- Data: no data.
- Returns: a ZIP file containing the project files ready for deployment.

`GET`
`https://api.weweb.io/public/v1/workspaces/{{:workspaceId}}/projects/{{:projectId}}/versions/{{:version}}/download`
- :workspaceId can be found in the URL of the workspace
- :projectId can be found in the URL of the project
- :version can be found in the Versions tab of the project or as a result of previous requests.

`:workspaceId`
`:projectId`
`:version`
`Versions`
- Method: GET
- URL: https://api.weweb.io/public/v1/workspaces/{{:workspaceId}}/projects/{{:projectId}}/versions/{{:version}}/config:workspaceId can be found in the URL of the workspace:projectId can be found in the URL of the project:version can be found in the Versions tab of the project or as a result of previous requests.
- :workspaceId can be found in the URL of the workspace
- :projectId can be found in the URL of the project
- :version can be found in the Versions tab of the project or as a result of previous requests.
- Data: no data.
- Returns: Returns a JSON containing all the data needed to configure the weweb-server.

`GET`
`https://api.weweb.io/public/v1/workspaces/{{:workspaceId}}/projects/{{:projectId}}/versions/{{:version}}/config`
- :workspaceId can be found in the URL of the workspace
- :projectId can be found in the URL of the project
- :version can be found in the Versions tab of the project or as a result of previous requests.

`:workspaceId`
`:projectId`
`:version`
`Versions`
The result of this request should be saved in a weweb-server.config.json file that is at in the root folder of weweb-server. At the next start, weweb-server will look for this file and create a new version on it's database. This is only useful if your weweb-server cannot be reached on the internet by our servers.

`weweb-server.config.json`
This request is done directly to your weweb-server

- Method: POST
- URL: https://<YOUR WEWEB-SERVER URL>/public/v1/projects/{{:projectId}}/versions/{{:version}}/active:projectId can be found in the URL of the project:version can be found in the Versions tab of the project or as a result of previous requests.
- :projectId can be found in the URL of the project
- :version can be found in the Versions tab of the project or as a result of previous requests.
- Data: env accepts values production or staging and defines the target of the activation.
- Returns:

`POST`
`https://<YOUR WEWEB-SERVER URL>/public/v1/projects/{{:projectId}}/versions/{{:version}}/active`
- :projectId can be found in the URL of the project
- :version can be found in the Versions tab of the project or as a result of previous requests.

`:projectId`
`:version`
`Versions`
`env`
`production`
`staging`
```
{
	"success": true,    //Success, can be `true` or `false`
}
```

`{
	"success": true,    //Success, can be `true` or `false`
}`

## Monitoring a publication ​

Check the status field in the response to determine when the publication is complete. The value will be deployed when the publication is finished.

`status`
`deployed`

## Typical auto deploy ​

A typical auto deploy script should be:

```
 1. Start the publication of a project with "builtZip" set to true.
 2. Store the version provided by the previous request
 3. While the project is publishing, check the publication status of a project. The publication is done when the progress is 100 and status is "published".
 6. Download project files ZIP by version using the version provided in the start publication step
 7. Save the downloaded ZIP file
 8. Extract the download zip file to your weweb-server storage at the right place (defined by FILES_PATH)
 9. Activate the published version in you weweb-server using the version provided in the start publication step
```

` 1. Start the publication of a project with "builtZip" set to true.
 2. Store the version provided by the previous request
 3. While the project is publishing, check the publication status of a project. The publication is done when the progress is 100 and status is "published".
 6. Download project files ZIP by version using the version provided in the start publication step
 7. Save the downloaded ZIP file
 8. Extract the download zip file to your weweb-server storage at the right place (defined by FILES_PATH)
 9. Activate the published version in you weweb-server using the version provided in the start publication step`
