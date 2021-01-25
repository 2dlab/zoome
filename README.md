# zoome

### Getting Started

`$ pip install zoome`

#### create ZoomClient object
```python
from zoome.api import ZoomClient

zc = ZoomClient(api_key='<api_key>', secret_api_key='<secret_api_key>')
```

##### or

```python
from zoome.api import ZoomClient

zc = ZoomClient(jwt_token='<jwt_token>')
```

#### get meetings list

```python
meetings = zc.get_meetings_list()
```

#### download file

```python
zc.download_file(full_path='<full_path>', url='<url>')
```

----

### Utils

#### get download urls from list of meetings

```python
from zoome.api import ZoomClient
from zoome.utils import get_meetings_download_urls

zc = ZoomClient(jwt_token='<jwt_token>')
meetings = zc.get_meetings_list()

links = get_meetings_download_urls(meetings)
```
##### links:
```json
[
  [
    {
      "download_url": "<download_url>",
      "recording_type": "<recording_type>",
      "file_type": "<file_type>"
    },
    ...
  ],
  ...
]
```

#### get download links from one meeting

```python
from zoome.api import ZoomClient
from zoome.utils import get_download_urls_from_meeting

zc = ZoomClient(jwt_token='<jwt_token>')
meetings = zc.get_meetings_list()

links = get_download_urls_from_meeting(meetings[0])
```
##### links:
```json
[
  {
    "download_url": "<download_url>",
    "recording_type": "<recording_type>",
    "file_type": "<file_type>"
  },
  ...
]
```

