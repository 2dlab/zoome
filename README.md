# zoome

### Getting Started

`$ pip install zoome`

#### create ZoomClient object
```python
from zoome import ZoomClient

zc = ZoomClient(api_key='<api_key>', secret_api_key='<secret_api_key>')
```

##### or

```python
from zoome import ZoomClient

zc = ZoomClient(jwt_token='<jwt_token>')
```

#### get conferences list

```python
zc.get_conferences_list()
```

#### download file

```python
zc.download_file(full_path='<full_path>', url='<url>')
```
