# Steel

Types:

```python
from steel.types import PdfResponse, ScrapeResponse, ScreenshotResponse
```

Methods:

- <code title="post /v1/pdf">client.<a href="./src/steel/_client.py">pdf</a>(\*\*<a href="src/steel/types/client_pdf_params.py">params</a>) -> <a href="./src/steel/types/pdf_response.py">PdfResponse</a></code>
- <code title="post /v1/scrape">client.<a href="./src/steel/_client.py">scrape</a>(\*\*<a href="src/steel/types/client_scrape_params.py">params</a>) -> <a href="./src/steel/types/scrape_response.py">ScrapeResponse</a></code>
- <code title="post /v1/screenshot">client.<a href="./src/steel/_client.py">screenshot</a>(\*\*<a href="src/steel/types/client_screenshot_params.py">params</a>) -> <a href="./src/steel/types/screenshot_response.py">ScreenshotResponse</a></code>

# Credentials

Types:

```python
from steel.types import (
    CredentialCreateResponse,
    CredentialUpdateResponse,
    CredentialListResponse,
    CredentialDeleteResponse,
)
```

Methods:

- <code title="post /v1/credentials">client.credentials.<a href="./src/steel/resources/credentials.py">create</a>(\*\*<a href="src/steel/types/credential_create_params.py">params</a>) -> <a href="./src/steel/types/credential_create_response.py">CredentialCreateResponse</a></code>
- <code title="put /v1/credentials">client.credentials.<a href="./src/steel/resources/credentials.py">update</a>(\*\*<a href="src/steel/types/credential_update_params.py">params</a>) -> <a href="./src/steel/types/credential_update_response.py">CredentialUpdateResponse</a></code>
- <code title="get /v1/credentials">client.credentials.<a href="./src/steel/resources/credentials.py">list</a>(\*\*<a href="src/steel/types/credential_list_params.py">params</a>) -> <a href="./src/steel/types/credential_list_response.py">CredentialListResponse</a></code>
- <code title="delete /v1/credentials">client.credentials.<a href="./src/steel/resources/credentials.py">delete</a>(\*\*<a href="src/steel/types/credential_delete_params.py">params</a>) -> <a href="./src/steel/types/credential_delete_response.py">CredentialDeleteResponse</a></code>

# Files

Types:

```python
from steel.types import File, Fileslist
```

Methods:

- <code title="get /v1/files">client.files.<a href="./src/steel/resources/files.py">list</a>() -> <a href="./src/steel/types/fileslist.py">Fileslist</a></code>
- <code title="delete /v1/files/{path}">client.files.<a href="./src/steel/resources/files.py">delete</a>(path) -> None</code>
- <code title="get /v1/files/{path}">client.files.<a href="./src/steel/resources/files.py">download</a>(path) -> BinaryAPIResponse</code>
- <code title="post /v1/files">client.files.<a href="./src/steel/resources/files.py">upload</a>(\*\*<a href="src/steel/types/file_upload_params.py">params</a>) -> <a href="./src/steel/types/file.py">File</a></code>

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

Methods:

- <code title="get /v1/sessions/{sessionId}/files">client.sessions.files.<a href="./src/steel/resources/sessions/files.py">list</a>(session_id) -> <a href="./src/steel/types/fileslist.py">Fileslist</a></code>
- <code title="delete /v1/sessions/{sessionId}/files/{path}">client.sessions.files.<a href="./src/steel/resources/sessions/files.py">delete</a>(path, \*, session_id) -> None</code>
- <code title="delete /v1/sessions/{sessionId}/files">client.sessions.files.<a href="./src/steel/resources/sessions/files.py">delete_all</a>(session_id) -> None</code>
- <code title="get /v1/sessions/{sessionId}/files/{path}">client.sessions.files.<a href="./src/steel/resources/sessions/files.py">download</a>(path, \*, session_id) -> BinaryAPIResponse</code>
- <code title="get /v1/sessions/{sessionId}/files.zip">client.sessions.files.<a href="./src/steel/resources/sessions/files.py">download_archive</a>(session_id) -> BinaryAPIResponse</code>
- <code title="post /v1/sessions/{sessionId}/files">client.sessions.files.<a href="./src/steel/resources/sessions/files.py">upload</a>(session_id, \*\*<a href="src/steel/types/sessions/file_upload_params.py">params</a>) -> <a href="./src/steel/types/file.py">File</a></code>

## Captchas

Types:

```python
from steel.types.sessions import CaptchaSolveImageResponse, CaptchaStatusResponse
```

Methods:

- <code title="post /v1/sessions/{sessionId}/captchas/solve-image">client.sessions.captchas.<a href="./src/steel/resources/sessions/captchas.py">solve_image</a>(session_id, \*\*<a href="src/steel/types/sessions/captcha_solve_image_params.py">params</a>) -> <a href="./src/steel/types/sessions/captcha_solve_image_response.py">CaptchaSolveImageResponse</a></code>
- <code title="get /v1/sessions/{sessionId}/captchas/status">client.sessions.captchas.<a href="./src/steel/resources/sessions/captchas.py">status</a>(session_id) -> <a href="./src/steel/types/sessions/captcha_status_response.py">CaptchaStatusResponse</a></code>

# Extensions

Types:

```python
from steel.types import (
    ExtensionUpdateResponse,
    ExtensionListResponse,
    ExtensionDeleteResponse,
    ExtensionDeleteAllResponse,
    ExtensionDownloadResponse,
    ExtensionUploadResponse,
)
```

Methods:

- <code title="put /v1/extensions/{extensionId}">client.extensions.<a href="./src/steel/resources/extensions.py">update</a>(extension_id, \*\*<a href="src/steel/types/extension_update_params.py">params</a>) -> <a href="./src/steel/types/extension_update_response.py">ExtensionUpdateResponse</a></code>
- <code title="get /v1/extensions">client.extensions.<a href="./src/steel/resources/extensions.py">list</a>() -> <a href="./src/steel/types/extension_list_response.py">ExtensionListResponse</a></code>
- <code title="delete /v1/extensions/{extensionId}">client.extensions.<a href="./src/steel/resources/extensions.py">delete</a>(extension_id) -> <a href="./src/steel/types/extension_delete_response.py">ExtensionDeleteResponse</a></code>
- <code title="delete /v1/extensions">client.extensions.<a href="./src/steel/resources/extensions.py">delete_all</a>() -> <a href="./src/steel/types/extension_delete_all_response.py">ExtensionDeleteAllResponse</a></code>
- <code title="get /v1/extensions/{extensionId}">client.extensions.<a href="./src/steel/resources/extensions.py">download</a>(extension_id) -> str</code>
- <code title="post /v1/extensions">client.extensions.<a href="./src/steel/resources/extensions.py">upload</a>(\*\*<a href="src/steel/types/extension_upload_params.py">params</a>) -> <a href="./src/steel/types/extension_upload_response.py">ExtensionUploadResponse</a></code>

# Profiles

Types:

```python
from steel.types import ProfileCreateResponse, ProfileListResponse
```

Methods:

- <code title="post /v1/profiles">client.profiles.<a href="./src/steel/resources/profiles.py">create</a>(\*\*<a href="src/steel/types/profile_create_params.py">params</a>) -> <a href="./src/steel/types/profile_create_response.py">ProfileCreateResponse</a></code>
- <code title="get /v1/profiles">client.profiles.<a href="./src/steel/resources/profiles.py">list</a>() -> <a href="./src/steel/types/profile_list_response.py">ProfileListResponse</a></code>
