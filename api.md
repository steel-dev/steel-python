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
    SessionEventsResponse,
    SessionLiveDetailsResponse,
    SessionReleaseResponse,
    SessionReleaseAllResponse,
)
```

Methods:

- <code title="post /v1/sessions">client.sessions.<a href="./src/steel/resources/sessions/sessions.py">create</a>(\*\*<a href="src/steel/types/session_create_params.py">params</a>) -> <a href="./src/steel/types/session.py">Session</a></code>
- <code title="get /v1/sessions/{id}">client.sessions.<a href="./src/steel/resources/sessions/sessions.py">retrieve</a>(id) -> <a href="./src/steel/types/session.py">Session</a></code>
- <code title="get /v1/sessions">client.sessions.<a href="./src/steel/resources/sessions/sessions.py">list</a>(\*\*<a href="src/steel/types/session_list_params.py">params</a>) -> SyncSessionsCursor[Session]</code>
- <code title="get /v1/sessions/{id}/context">client.sessions.<a href="./src/steel/resources/sessions/sessions.py">context</a>(id) -> <a href="./src/steel/types/session_context.py">SessionContext</a></code>
- <code title="get /v1/sessions/{id}/events">client.sessions.<a href="./src/steel/resources/sessions/sessions.py">events</a>(id) -> <a href="./src/steel/types/session_events_response.py">SessionEventsResponse</a></code>
- <code title="get /v1/sessions/{id}/live-details">client.sessions.<a href="./src/steel/resources/sessions/sessions.py">live_details</a>(id) -> <a href="./src/steel/types/session_live_details_response.py">SessionLiveDetailsResponse</a></code>
- <code title="post /v1/sessions/{id}/release">client.sessions.<a href="./src/steel/resources/sessions/sessions.py">release</a>(id) -> <a href="./src/steel/types/session_release_response.py">SessionReleaseResponse</a></code>
- <code title="post /v1/sessions/release">client.sessions.<a href="./src/steel/resources/sessions/sessions.py">release_all</a>() -> <a href="./src/steel/types/session_release_all_response.py">SessionReleaseAllResponse</a></code>

## Files

Types:

```python
from steel.types.sessions import File, Fileslist, FileDeleteResponse, FileDeleteAllResponse
```

Methods:

- <code title="get /v1/sessions/{sessionId}/files/{fileId}">client.sessions.files.<a href="./src/steel/resources/sessions/files.py">retrieve</a>(file_id, \*, session_id) -> <a href="./src/steel/types/sessions/file.py">File</a></code>
- <code title="get /v1/sessions/{sessionId}/files">client.sessions.files.<a href="./src/steel/resources/sessions/files.py">list</a>(session_id) -> <a href="./src/steel/types/sessions/fileslist.py">Fileslist</a></code>
- <code title="delete /v1/sessions/{sessionId}/files/{fileId}">client.sessions.files.<a href="./src/steel/resources/sessions/files.py">delete</a>(file_id, \*, session_id) -> <a href="./src/steel/types/sessions/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="delete /v1/sessions/{sessionId}/files">client.sessions.files.<a href="./src/steel/resources/sessions/files.py">delete_all</a>(session_id) -> <a href="./src/steel/types/sessions/file_delete_all_response.py">FileDeleteAllResponse</a></code>
- <code title="get /v1/sessions/{sessionId}/files/{fileId}/download">client.sessions.files.<a href="./src/steel/resources/sessions/files.py">download</a>(file_id, \*, session_id) -> BinaryAPIResponse</code>
- <code title="post /v1/sessions/{sessionId}/files">client.sessions.files.<a href="./src/steel/resources/sessions/files.py">upload</a>(session_id, \*\*<a href="src/steel/types/sessions/file_upload_params.py">params</a>) -> <a href="./src/steel/types/sessions/file.py">File</a></code>
