# Link Gopher

## Description

Clone of link gopher browser extension written in Python programming language for educational purposes. For more info see: 
- [Google Chrome Link Gopher](https://chrome.google.com/webstore/detail/link-gopher/bpjdkodgnbfalgghnbeggfbfjpcfamkf)
- [Mozzila Firefox Link Gopher](https://addons.mozilla.org/en-US/firefox/addon/link-gopher/)

As part of installation, CLI tool is provided which can be used to fetch all links from webpages without duplicates.

## Installation

To install cli tool you need:
- Latest version of [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/download/thanks/)
- [Gecko Driver](https://github.com/mozilla/geckodriver/releases) for your OS 
- [Python](https://www.python.org/downloads/release/python-394/) version 3.9.4 or more

After installation follow these steps
- Clone this repository on your local machine
- Change directory to cloned repository
- Run ```pip install -e .``` command

## CLI usage

After installation you can use CLI tool.

Basic usage is

```link-gopher run --browser=b --src=s --dst=d --in=in --out=out --filter_type=ftype --filter_values=fvalues```

Command options have following meanings:
- ```browser``` chooses type of browser for scraping, with only option supported now being ```firefox``` which is a default option
- ```src``` determines type of source for urls to gopher. Two possible options are:
    - ```mem``` which loads links from memory (default)
    - ```txt``` which loads links from txt file
- ```dst``` determines where to store fetched links from pages. Two possible options are:
    - ```mem``` writes links to stdout (default)
    - ```txt``` writes linkts to txt file
- ```in``` is used for input path and depends of type of source chosen
    - For ```mem``` source it is comma separated list of values
    - For ```txt``` source it is path to txt file
- ```out``` is used for ouput path and depends of type of destination chosen
    - For ```mem``` nothing has to be specified
    - For ```txt``` this is path to destination file
- ```filter-type``` determines type of filter, currently only ```basic``` filter is supported
- ```filter-values``` determines values for filter as comma separated list of values

## CLI usage examples


Link gopher for Python and Github websites which writes into stdout

```link-gopher run --src=mem --dst=mem --in=https://python.org,https://github.com```

Link gopher which reads from txt file and writes into stdout

```link-gopher run --src=text --dst=mem --in=test.txt```

Link gopher which reads from txt file and writes to new txt file

```link-gopher run --src=mem --dst=mem --in=test.txt --out=test2.txt```

Link gopher which filters results

```link-gopher run --src=mem --dst=mem --in=test.txt --out=test2.txt --filter-type=basic --filter-values=filter```