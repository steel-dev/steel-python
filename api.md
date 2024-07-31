# API

## Schema

Types:

```python
from steel.types.api import SchemaRetrieveResponse
```

Methods:

- <code title="get /api/schema/">client.api.schema.<a href="./src/steel/resources/api/schema.py">retrieve</a>(\*\*<a href="src/steel/types/api/schema_retrieve_params.py">params</a>) -> <a href="./src/steel/types/api/schema_retrieve_response.py">SchemaRetrieveResponse</a></code>

## SDK

### Context

Types:

```python
from steel.types.api.sdk import Context, ContextListResponse
```

Methods:

- <code title="post /v1/sdk/context/">client.api.sdk.context.<a href="./src/steel/resources/api/sdk/context.py">create</a>(\*\*<a href="src/steel/types/api/sdk/context_create_params.py">params</a>) -> <a href="./src/steel/types/api/sdk/context.py">Context</a></code>
- <code title="get /v1/sdk/context/{id}/">client.api.sdk.context.<a href="./src/steel/resources/api/sdk/context.py">retrieve</a>(id) -> <a href="./src/steel/types/api/sdk/context.py">Context</a></code>
- <code title="patch /v1/sdk/context/{id}/">client.api.sdk.context.<a href="./src/steel/resources/api/sdk/context.py">update</a>(id, \*\*<a href="src/steel/types/api/sdk/context_update_params.py">params</a>) -> <a href="./src/steel/types/api/sdk/context.py">Context</a></code>
- <code title="get /v1/sdk/context/">client.api.sdk.context.<a href="./src/steel/resources/api/sdk/context.py">list</a>() -> <a href="./src/steel/types/api/sdk/context_list_response.py">ContextListResponse</a></code>
- <code title="delete /v1/sdk/context/{id}/">client.api.sdk.context.<a href="./src/steel/resources/api/sdk/context.py">delete</a>(id) -> None</code>

### Pdf

Types:

```python
from steel.types.api.sdk import PdfCreateResponse
```

Methods:

- <code title="post /v1/sdk/pdf/">client.api.sdk.pdf.<a href="./src/steel/resources/api/sdk/pdf.py">create</a>(\*\*<a href="src/steel/types/api/sdk/pdf_create_params.py">params</a>) -> <a href="./src/steel/types/api/sdk/pdf_create_response.py">object</a></code>

### Scrape

Types:

```python
from steel.types.api.sdk import ScrapeCreateResponse
```

Methods:

- <code title="post /v1/sdk/scrape/">client.api.sdk.scrape.<a href="./src/steel/resources/api/sdk/scrape.py">create</a>(\*\*<a href="src/steel/types/api/sdk/scrape_create_params.py">params</a>) -> <a href="./src/steel/types/api/sdk/scrape_create_response.py">object</a></code>

### Screenshot

Types:

```python
from steel.types.api.sdk import ScreenshotCreateResponse
```

Methods:

- <code title="post /v1/sdk/screenshot/">client.api.sdk.screenshot.<a href="./src/steel/resources/api/sdk/screenshot.py">create</a>(\*\*<a href="src/steel/types/api/sdk/screenshot_create_params.py">params</a>) -> <a href="./src/steel/types/api/sdk/screenshot_create_response.py">object</a></code>

### Sessions

Types:

```python
from steel.types.api.sdk import Session, SessionListResponse
```

Methods:

- <code title="post /v1/sdk/sessions/">client.api.sdk.sessions.<a href="./src/steel/resources/api/sdk/sessions.py">create</a>(\*\*<a href="src/steel/types/api/sdk/session_create_params.py">params</a>) -> <a href="./src/steel/types/api/sdk/session.py">Session</a></code>
- <code title="get /v1/sdk/sessions/{id}/">client.api.sdk.sessions.<a href="./src/steel/resources/api/sdk/sessions.py">retrieve</a>(id) -> <a href="./src/steel/types/api/sdk/session.py">Session</a></code>
- <code title="patch /v1/sdk/sessions/{id}/">client.api.sdk.sessions.<a href="./src/steel/resources/api/sdk/sessions.py">update</a>(id, \*\*<a href="src/steel/types/api/sdk/session_update_params.py">params</a>) -> <a href="./src/steel/types/api/sdk/session.py">Session</a></code>
- <code title="get /v1/sdk/sessions/">client.api.sdk.sessions.<a href="./src/steel/resources/api/sdk/sessions.py">list</a>() -> <a href="./src/steel/types/api/sdk/session_list_response.py">SessionListResponse</a></code>
- <code title="delete /v1/sdk/sessions/{id}/">client.api.sdk.sessions.<a href="./src/steel/resources/api/sdk/sessions.py">delete</a>(id) -> None</code>
