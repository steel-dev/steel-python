# Steel

Types:

```python
from steel.types import PdfResponse, ScrapeResponse, ScreenshotResponse
```

Methods:

- <code title="post /v1/pdf">client.<a href="./src/steel/_client.py">pdf</a>(\*\*<a href="src/steel/types/client_pdf_params.py">params</a>) -> <a href="./src/steel/types/pdf_response.py">PdfResponse</a></code>
- <code title="post /v1/scrape">client.<a href="./src/steel/_client.py">scrape</a>(\*\*<a href="src/steel/types/client_scrape_params.py">params</a>) -> <a href="./src/steel/types/scrape_response.py">ScrapeResponse</a></code>
- <code title="post /v1/screenshot">client.<a href="./src/steel/_client.py">screenshot</a>(\*\*<a href="src/steel/types/client_screenshot_params.py">params</a>) -> <a href="./src/steel/types/screenshot_response.py">ScreenshotResponse</a></code>

# Sessions

Types:

```python
from steel.types import (
    Session,
    SessionContext,
    Sessionslist,
    SessionListResponse,
    SessionReleaseResponse,
    SessionReleaseAllResponse,
)
```

Methods:

- <code title="post /v1/sessions">client.sessions.<a href="./src/steel/resources/sessions.py">create</a>(\*\*<a href="src/steel/types/session_create_params.py">params</a>) -> <a href="./src/steel/types/session.py">Session</a></code>
- <code title="get /v1/sessions/{id}">client.sessions.<a href="./src/steel/resources/sessions.py">retrieve</a>(id) -> <a href="./src/steel/types/session.py">Session</a></code>
- <code title="get /v1/sessions">client.sessions.<a href="./src/steel/resources/sessions.py">list</a>(\*\*<a href="src/steel/types/session_list_params.py">params</a>) -> <a href="./src/steel/types/session_list_response.py">SyncSessionsCursor[SessionListResponse]</a></code>
- <code title="get /v1/sessions/{id}/context">client.sessions.<a href="./src/steel/resources/sessions.py">context</a>(id) -> <a href="./src/steel/types/session_context.py">SessionContext</a></code>
- <code title="post /v1/sessions/{id}/release">client.sessions.<a href="./src/steel/resources/sessions.py">release</a>(id) -> <a href="./src/steel/types/session_release_response.py">SessionReleaseResponse</a></code>
- <code title="post /v1/sessions/release">client.sessions.<a href="./src/steel/resources/sessions.py">release_all</a>() -> <a href="./src/steel/types/session_release_all_response.py">SessionReleaseAllResponse</a></code>
