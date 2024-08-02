# Sessions

Types:

```python
from steel.types import Session, SessionListResponse, SessionReleaseResponse
```

Methods:

- <code title="post /v1/sessions">client.sessions.<a href="./src/steel/resources/sessions.py">create</a>(\*\*<a href="src/steel/types/session_create_params.py">params</a>) -> <a href="./src/steel/types/session.py">Session</a></code>
- <code title="get /v1/sessions/{id}">client.sessions.<a href="./src/steel/resources/sessions.py">retrieve</a>(id) -> <a href="./src/steel/types/session.py">Session</a></code>
- <code title="get /v1/sessions">client.sessions.<a href="./src/steel/resources/sessions.py">list</a>(\*\*<a href="src/steel/types/session_list_params.py">params</a>) -> <a href="./src/steel/types/session_list_response.py">SessionListResponse</a></code>
- <code title="get /v1/sessions/{id}/release">client.sessions.<a href="./src/steel/resources/sessions.py">release</a>(id) -> <a href="./src/steel/types/session_release_response.py">SessionReleaseResponse</a></code>

# BrowserTools

Types:

```python
from steel.types import Scrape
```

Methods:

- <code title="post /v1/pdf">client.browser_tools.<a href="./src/steel/resources/browser_tools.py">pdf</a>(\*\*<a href="src/steel/types/browser_tool_pdf_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v1/scrape">client.browser_tools.<a href="./src/steel/resources/browser_tools.py">scrape</a>(\*\*<a href="src/steel/types/browser_tool_scrape_params.py">params</a>) -> <a href="./src/steel/types/scrape.py">Scrape</a></code>
- <code title="post /v1/screenshot">client.browser_tools.<a href="./src/steel/resources/browser_tools.py">screenshot</a>(\*\*<a href="src/steel/types/browser_tool_screenshot_params.py">params</a>) -> BinaryAPIResponse</code>

# Contexts

Types:

```python
from steel.types import Context, ContextCreateResponse, ContextListResponse, ContextDeleteResponse
```

Methods:

- <code title="post /v1/context">client.contexts.<a href="./src/steel/resources/contexts.py">create</a>(\*\*<a href="src/steel/types/context_create_params.py">params</a>) -> <a href="./src/steel/types/context_create_response.py">ContextCreateResponse</a></code>
- <code title="get /v1/context/{id}">client.contexts.<a href="./src/steel/resources/contexts.py">retrieve</a>(id) -> <a href="./src/steel/types/context.py">Context</a></code>
- <code title="get /v1/context">client.contexts.<a href="./src/steel/resources/contexts.py">list</a>() -> <a href="./src/steel/types/context_list_response.py">ContextListResponse</a></code>
- <code title="delete /v1/context/{id}">client.contexts.<a href="./src/steel/resources/contexts.py">delete</a>(id) -> <a href="./src/steel/types/context_delete_response.py">ContextDeleteResponse</a></code>
