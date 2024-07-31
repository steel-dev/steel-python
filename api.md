# API

## Schema

Types:

```python
from steel.types.api import SchemaRetrieveResponse
```

Methods:

- <code title="get /api/schema/">client.api.schema.<a href="./src/steel/resources/api/schema.py">retrieve</a>(\*\*<a href="src/steel/types/api/schema_retrieve_params.py">params</a>) -> <a href="./src/steel/types/api/schema_retrieve_response.py">SchemaRetrieveResponse</a></code>

# V1

## SDK

### Context

Types:

```python
from steel.types.v1.sdk import Context, ContextListResponse
```

Methods:

- <code title="post /v1/sdk/context/">client.v1.sdk.context.<a href="./src/steel/resources/v1/sdk/context.py">create</a>(\*\*<a href="src/steel/types/v1/sdk/context_create_params.py">params</a>) -> <a href="./src/steel/types/v1/sdk/context.py">Context</a></code>
- <code title="get /v1/sdk/context/{id}/">client.v1.sdk.context.<a href="./src/steel/resources/v1/sdk/context.py">retrieve</a>(id) -> <a href="./src/steel/types/v1/sdk/context.py">Context</a></code>
- <code title="patch /v1/sdk/context/{id}/">client.v1.sdk.context.<a href="./src/steel/resources/v1/sdk/context.py">update</a>(id, \*\*<a href="src/steel/types/v1/sdk/context_update_params.py">params</a>) -> <a href="./src/steel/types/v1/sdk/context.py">Context</a></code>
- <code title="get /v1/sdk/context/">client.v1.sdk.context.<a href="./src/steel/resources/v1/sdk/context.py">list</a>() -> <a href="./src/steel/types/v1/sdk/context_list_response.py">ContextListResponse</a></code>
- <code title="delete /v1/sdk/context/{id}/">client.v1.sdk.context.<a href="./src/steel/resources/v1/sdk/context.py">delete</a>(id) -> None</code>

### Pdf

Types:

```python
from steel.types.v1.sdk import PdfCreateResponse
```

Methods:

- <code title="post /v1/sdk/pdf/">client.v1.sdk.pdf.<a href="./src/steel/resources/v1/sdk/pdf.py">create</a>(\*\*<a href="src/steel/types/v1/sdk/pdf_create_params.py">params</a>) -> <a href="./src/steel/types/v1/sdk/pdf_create_response.py">object</a></code>

### Scrape

Types:

```python
from steel.types.v1.sdk import ScrapeCreateResponse
```

Methods:

- <code title="post /v1/sdk/scrape/">client.v1.sdk.scrape.<a href="./src/steel/resources/v1/sdk/scrape.py">create</a>(\*\*<a href="src/steel/types/v1/sdk/scrape_create_params.py">params</a>) -> <a href="./src/steel/types/v1/sdk/scrape_create_response.py">object</a></code>

### Screenshot

Types:

```python
from steel.types.v1.sdk import ScreenshotCreateResponse
```

Methods:

- <code title="post /v1/sdk/screenshot/">client.v1.sdk.screenshot.<a href="./src/steel/resources/v1/sdk/screenshot.py">create</a>(\*\*<a href="src/steel/types/v1/sdk/screenshot_create_params.py">params</a>) -> <a href="./src/steel/types/v1/sdk/screenshot_create_response.py">object</a></code>

### Sessions

Types:

```python
from steel.types.v1.sdk import Session, SessionListResponse
```

Methods:

- <code title="post /v1/sdk/sessions/">client.v1.sdk.sessions.<a href="./src/steel/resources/v1/sdk/sessions.py">create</a>(\*\*<a href="src/steel/types/v1/sdk/session_create_params.py">params</a>) -> <a href="./src/steel/types/v1/sdk/session.py">Session</a></code>
- <code title="get /v1/sdk/sessions/{id}/">client.v1.sdk.sessions.<a href="./src/steel/resources/v1/sdk/sessions.py">retrieve</a>(id) -> <a href="./src/steel/types/v1/sdk/session.py">Session</a></code>
- <code title="patch /v1/sdk/sessions/{id}/">client.v1.sdk.sessions.<a href="./src/steel/resources/v1/sdk/sessions.py">update</a>(id, \*\*<a href="src/steel/types/v1/sdk/session_update_params.py">params</a>) -> <a href="./src/steel/types/v1/sdk/session.py">Session</a></code>
- <code title="get /v1/sdk/sessions/">client.v1.sdk.sessions.<a href="./src/steel/resources/v1/sdk/sessions.py">list</a>() -> <a href="./src/steel/types/v1/sdk/session_list_response.py">SessionListResponse</a></code>
- <code title="delete /v1/sdk/sessions/{id}/">client.v1.sdk.sessions.<a href="./src/steel/resources/v1/sdk/sessions.py">delete</a>(id) -> None</code>
