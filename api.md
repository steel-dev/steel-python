# Steel

Types:

```python
from steel.types import (
    PdfRequest,
    PdfResponse,
    ScrapeRequest,
    ScrapeResponse,
    ScreenshotRequest,
    ScreenshotResponse,
)
```

Methods:

- <code title="post /v1/pdf">client.<a href="./src/steel/_client.py">generate_pdf</a>(\*\*<a href="src/steel/types/top_level_generate_pdf_params.py">params</a>) -> <a href="./src/steel/types/pdf_response.py">PdfResponse</a></code>
- <code title="get /v1/sessions">client.<a href="./src/steel/_client.py">list_sessions</a>(\*\*<a href="src/steel/types/top_level_list_sessions_params.py">params</a>) -> <a href="./src/steel/types/session.py">SyncCursorPage[Session]</a></code>
- <code title="post /v1/scrape">client.<a href="./src/steel/_client.py">scrape</a>(\*\*<a href="src/steel/types/top_level_scrape_params.py">params</a>) -> <a href="./src/steel/types/scrape_response.py">ScrapeResponse</a></code>
- <code title="post /v1/screenshot">client.<a href="./src/steel/_client.py">screenshot</a>(\*\*<a href="src/steel/types/top_level_screenshot_params.py">params</a>) -> <a href="./src/steel/types/screenshot_response.py">ScreenshotResponse</a></code>

# Session

Types:

```python
from steel.types import (
    CreateSessionRequest,
    ReleaseSessionResponse,
    Session,
    SessionGetContextResponse,
)
```

Methods:

- <code title="post /v1/sessions">client.session.<a href="./src/steel/resources/session.py">create</a>(\*\*<a href="src/steel/types/session_create_params.py">params</a>) -> <a href="./src/steel/types/session.py">Session</a></code>
- <code title="get /v1/sessions/{id}/context">client.session.<a href="./src/steel/resources/session.py">get_context</a>(id) -> <a href="./src/steel/types/session_get_context_response.py">object</a></code>
- <code title="get /v1/sessions/{id}">client.session.<a href="./src/steel/resources/session.py">get_data</a>(id) -> <a href="./src/steel/types/session.py">Session</a></code>
- <code title="get /v1/sessions/{id}/release">client.session.<a href="./src/steel/resources/session.py">release</a>(id) -> <a href="./src/steel/types/release_session_response.py">ReleaseSessionResponse</a></code>
