# Sessions

Types:

```python
from steel.types import ReleaseSessionResponse, SessionResponse, SessionListResponse
```

Methods:

- <code title="post /v1/sessions">client.sessions.<a href="./src/steel/resources/sessions.py">create</a>(\*\*<a href="src/steel/types/session_create_params.py">params</a>) -> <a href="./src/steel/types/session_response.py">SessionResponse</a></code>
- <code title="get /v1/sessions/{id}">client.sessions.<a href="./src/steel/resources/sessions.py">retrieve</a>(id) -> <a href="./src/steel/types/session_response.py">SessionResponse</a></code>
- <code title="get /v1/sessions">client.sessions.<a href="./src/steel/resources/sessions.py">list</a>(\*\*<a href="src/steel/types/session_list_params.py">params</a>) -> <a href="./src/steel/types/session_list_response.py">SessionListResponse</a></code>
- <code title="get /v1/sessions/{id}/release">client.sessions.<a href="./src/steel/resources/sessions.py">release</a>(id) -> <a href="./src/steel/types/release_session_response.py">ReleaseSessionResponse</a></code>

# BrowserTools

Types:

```python
from steel.types import ScrapeResponse
```

Methods:

- <code title="post /v1/pdf">client.browser_tools.<a href="./src/steel/resources/browser_tools.py">pdf</a>(\*\*<a href="src/steel/types/browser_tool_pdf_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v1/scrape">client.browser_tools.<a href="./src/steel/resources/browser_tools.py">scrape</a>(\*\*<a href="src/steel/types/browser_tool_scrape_params.py">params</a>) -> <a href="./src/steel/types/scrape_response.py">ScrapeResponse</a></code>
- <code title="post /v1/screenshot">client.browser_tools.<a href="./src/steel/resources/browser_tools.py">screenshot</a>(\*\*<a href="src/steel/types/browser_tool_screenshot_params.py">params</a>) -> BinaryAPIResponse</code>

# Contexts

Types:

```python
from steel.types import (
    CreateContextResponse,
    DeleteContextResponse,
    GetContextResponse,
    GetContextsResponse,
)
```

Methods:

- <code title="post /v1/context">client.contexts.<a href="./src/steel/resources/contexts.py">create</a>(\*\*<a href="src/steel/types/context_create_params.py">params</a>) -> <a href="./src/steel/types/create_context_response.py">CreateContextResponse</a></code>
- <code title="get /v1/context/{id}">client.contexts.<a href="./src/steel/resources/contexts.py">retrieve</a>(id) -> <a href="./src/steel/types/get_context_response.py">GetContextResponse</a></code>
- <code title="get /v1/context">client.contexts.<a href="./src/steel/resources/contexts.py">list</a>() -> <a href="./src/steel/types/get_contexts_response.py">GetContextsResponse</a></code>
- <code title="delete /v1/context/{id}">client.contexts.<a href="./src/steel/resources/contexts.py">delete</a>(id) -> <a href="./src/steel/types/delete_context_response.py">DeleteContextResponse</a></code>
