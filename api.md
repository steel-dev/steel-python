# Steel

Types:

```python
from steel.types import ScrapeResponse
```

Methods:

- <code title="post /v1/pdf">client.<a href="./src/steel/_client.py">pdf</a>(\*\*<a href="src/steel/types/top_level_pdf_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v1/scrape">client.<a href="./src/steel/_client.py">scrape</a>(\*\*<a href="src/steel/types/top_level_scrape_params.py">params</a>) -> <a href="./src/steel/types/scrape_response.py">ScrapeResponse</a></code>
- <code title="post /v1/screenshot">client.<a href="./src/steel/_client.py">screenshot</a>(\*\*<a href="src/steel/types/top_level_screenshot_params.py">params</a>) -> BinaryAPIResponse</code>

# Sessions

Types:

```python
from steel.types import DeleteSessionResponse, SessionResponse, SessionsResponse
```

Methods:

- <code title="post /v1/sessions">client.sessions.<a href="./src/steel/resources/sessions.py">create</a>(\*\*<a href="src/steel/types/session_create_params.py">params</a>) -> <a href="./src/steel/types/session_response.py">SessionResponse</a></code>
- <code title="get /v1/sessions">client.sessions.<a href="./src/steel/resources/sessions.py">list</a>() -> <a href="./src/steel/types/sessions_response.py">SessionsResponse</a></code>
- <code title="delete /v1/sessions/{id}">client.sessions.<a href="./src/steel/resources/sessions.py">delete</a>(id) -> <a href="./src/steel/types/delete_session_response.py">DeleteSessionResponse</a></code>

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
