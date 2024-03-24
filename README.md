# Free Magazines downloader

Current spider only supports `freemagazines.top` by extracting download urls host on `vk.com`.

## Install 

If you're in PyCharm, create a virtual env.

If you're in Terminal, run

``` 
python3 -m venv venv
source venv/bin/activate
pip install -U -r requirements.txt
 
```

You'll see command prompt like 
```
(.venv) USER@hostname freemagazines %
```


## Run

Make sure you are under `freemagazines` directory, if not, switch by `cd`.


``` 
scrapy crawl myspider
```

`myspider` is file name of `freemagazines/spiders/myspider.py`

Output will be saved to `vk_links.txt`.

## New Magazine

Edit `freemagazines/spiders/myspider.py`, you'll see 
``` 
start_urls = [
    'URL...'
]

```

Change to any **LIST** url or **Search** URL.

