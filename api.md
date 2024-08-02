# Steel

Types:

```python
from steel.types import ListSessionsResponse, ScrapeResponse
```

Methods:

- <code title="post /v1/sessions">client.<a href="./src/steel/_client.py">create_session</a>(\*\*<a href="src/steel/types/top_level_create_session_params.py">params</a>) -> <a href="./src/steel/types/session.py">Session</a></code>
- <code title="get /v1/sessions">client.<a href="./src/steel/_client.py">list_sessions</a>(\*\*<a href="src/steel/types/top_level_list_sessions_params.py">params</a>) -> <a href="./src/steel/types/list_sessions_response.py">ListSessionsResponse</a></code>
- <code title="post /v1/pdf">client.<a href="./src/steel/_client.py">pdf</a>(\*\*<a href="src/steel/types/top_level_pdf_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /v1/sessions/{id}">client.<a href="./src/steel/_client.py">retrieve_session</a>(id) -> <a href="./src/steel/types/session.py">Session</a></code>
- <code title="post /v1/scrape">client.<a href="./src/steel/_client.py">scrape</a>(\*\*<a href="src/steel/types/top_level_scrape_params.py">params</a>) -> <a href="./src/steel/types/scrape_response.py">ScrapeResponse</a></code>
- <code title="post /v1/screenshot">client.<a href="./src/steel/_client.py">screenshot</a>(\*\*<a href="src/steel/types/top_level_screenshot_params.py">params</a>) -> BinaryAPIResponse</code>

# SteelSession

Types:

```python
from steel.types import Session, SteelSessionReleaseSessionResponse
```

Methods:

- <code title="get /v1/context/{id}">client.steel_session.<a href="./src/steel/resources/steel_session.py">get_context</a>(id) -> <a href="./src/steel/types/context.py">Context</a></code>
- <code title="get /v1/sessions/{id}">client.steel_session.<a href="./src/steel/resources/steel_session.py">get_session_data</a>(id) -> <a href="./src/steel/types/session.py">Session</a></code>
- <code title="get /v1/sessions/{id}/release">client.steel_session.<a href="./src/steel/resources/steel_session.py">release_session</a>(id) -> <a href="./src/steel/types/steel_session_release_session_response.py">SteelSessionReleaseSessionResponse</a></code>

# SteelContext

Types:

```python
from steel.types import (
    Context,
    SteelContextCreateContextResponse,
    SteelContextDeleteContextResponse,
)
```

Methods:

- <code title="post /v1/context">client.steel_context.<a href="./src/steel/resources/steel_context.py">create_context</a>(\*\*<a href="src/steel/types/steel_context_create_context_params.py">params</a>) -> <a href="./src/steel/types/steel_context_create_context_response.py">SteelContextCreateContextResponse</a></code>
- <code title="delete /v1/context/{id}">client.steel_context.<a href="./src/steel/resources/steel_context.py">delete_context</a>(id) -> <a href="./src/steel/types/steel_context_delete_context_response.py">SteelContextDeleteContextResponse</a></code>
- <code title="get /v1/context/{id}">client.steel_context.<a href="./src/steel/resources/steel_context.py">get_context_data</a>(id) -> <a href="./src/steel/types/context.py">Context</a></code>
