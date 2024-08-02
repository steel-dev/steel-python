# SteelBrowser

Types:

```python
from steel.types import SteelBrowserListSessionsResponse, SteelBrowserScrapeResponse
```

Methods:

- <code title="post /v1/sessions">client.steel_browser.<a href="./src/steel/resources/steel_browser/steel_browser.py">create_session</a>(\*\*<a href="src/steel/types/steel_browser_create_session_params.py">params</a>) -> <a href="./src/steel/types/steel_browser/session.py">Session</a></code>
- <code title="get /v1/sessions">client.steel_browser.<a href="./src/steel/resources/steel_browser/steel_browser.py">list_sessions</a>(\*\*<a href="src/steel/types/steel_browser_list_sessions_params.py">params</a>) -> <a href="./src/steel/types/steel_browser_list_sessions_response.py">SteelBrowserListSessionsResponse</a></code>
- <code title="post /v1/pdf">client.steel_browser.<a href="./src/steel/resources/steel_browser/steel_browser.py">pdf</a>(\*\*<a href="src/steel/types/steel_browser_pdf_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /v1/sessions/{id}">client.steel_browser.<a href="./src/steel/resources/steel_browser/steel_browser.py">retrieve_session</a>(id) -> <a href="./src/steel/types/steel_browser/session.py">Session</a></code>
- <code title="post /v1/scrape">client.steel_browser.<a href="./src/steel/resources/steel_browser/steel_browser.py">scrape</a>(\*\*<a href="src/steel/types/steel_browser_scrape_params.py">params</a>) -> <a href="./src/steel/types/steel_browser_scrape_response.py">SteelBrowserScrapeResponse</a></code>
- <code title="post /v1/screenshot">client.steel_browser.<a href="./src/steel/resources/steel_browser/steel_browser.py">screenshot</a>(\*\*<a href="src/steel/types/steel_browser_screenshot_params.py">params</a>) -> BinaryAPIResponse</code>

## SteelSession

Types:

```python
from steel.types.steel_browser import Session, SteelSessionReleaseSessionResponse
```

Methods:

- <code title="get /v1/context/{id}">client.steel_browser.steel_session.<a href="./src/steel/resources/steel_browser/steel_session/steel_session.py">get_context</a>(id) -> <a href="./src/steel/types/steel_browser/steel_session/context.py">Context</a></code>
- <code title="get /v1/sessions/{id}">client.steel_browser.steel_session.<a href="./src/steel/resources/steel_browser/steel_session/steel_session.py">get_session_data</a>(id) -> <a href="./src/steel/types/steel_browser/session.py">Session</a></code>
- <code title="get /v1/sessions/{id}/release">client.steel_browser.steel_session.<a href="./src/steel/resources/steel_browser/steel_session/steel_session.py">release_session</a>(id) -> <a href="./src/steel/types/steel_browser/steel_session_release_session_response.py">SteelSessionReleaseSessionResponse</a></code>

### SteelContext

Types:

```python
from steel.types.steel_browser.steel_session import (
    Context,
    SteelContextCreateContextResponse,
    SteelContextDeleteContextResponse,
)
```

Methods:

- <code title="post /v1/context">client.steel_browser.steel_session.steel_context.<a href="./src/steel/resources/steel_browser/steel_session/steel_context.py">create_context</a>(\*\*<a href="src/steel/types/steel_browser/steel_session/steel_context_create_context_params.py">params</a>) -> <a href="./src/steel/types/steel_browser/steel_session/steel_context_create_context_response.py">SteelContextCreateContextResponse</a></code>
- <code title="delete /v1/context/{id}">client.steel_browser.steel_session.steel_context.<a href="./src/steel/resources/steel_browser/steel_session/steel_context.py">delete_context</a>(id) -> <a href="./src/steel/types/steel_browser/steel_session/steel_context_delete_context_response.py">SteelContextDeleteContextResponse</a></code>
- <code title="get /v1/context/{id}">client.steel_browser.steel_session.steel_context.<a href="./src/steel/resources/steel_browser/steel_session/steel_context.py">get_context_data</a>(id) -> <a href="./src/steel/types/steel_browser/steel_session/context.py">Context</a></code>
