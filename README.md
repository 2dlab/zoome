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

#### get conferences list

```python
conferences = zc.get_conferences_list()
```

#### download file

```python
zc.download_file(full_path='<full_path>', url='<url>')
```

----

### Utils

#### get download urls from list of conferences

```python
from zoome.api import ZoomClient
from zoome.utils import get_conferences_download_urls

zc = ZoomClient(jwt_token='<jwt_token>')
conferences = zc.get_conferences_list()

links = get_conferences_download_urls(conferences)
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

#### get download links from one conference

```python
from zoome.api import ZoomClient
from zoome.utils import get_download_urls_from_meeting

zc = ZoomClient(jwt_token='<jwt_token>')
conferences = zc.get_conferences_list()

links = get_download_urls_from_meeting(conferences[0])
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

