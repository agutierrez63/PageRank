# PageRank
A simple page rank algorithm for ranking urls. I built this page rank
script for my Senior Project. It ranks any any url by parsing the url
as an argument. The script was then called from an API that would rank
a crawled list of urls and score each url indivdually.

## Getting Started
Theses instruction will help you get a copy of the project and running
on your local machine for development and testing puposes. See 
deployment for notes on how to deploy the proejct on a live system.

### Prequisites
NOTICE: Brefore, you get started, I must let you know that I built
this in the WSL Environment System using Ubuntu; therefore, some of
the commands will look a little different from other Operating
Systems. 
In order to run the program, you will first need to have installed
Python 3 and pip 3 in order to install some of the python libraries
before you get started. Once installed the only libary you will
need to install will be 
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

### Installing
How to install:
1. Install Python3
```bash
sudo apt-get update
sudo apt-get install python3
```

2. Install pip3
```
sudo apt-get install python3-pip3
```

3. Install BeautifulSoup4
```bash
sudo apt-get install python3-bs4
```
or you can use pip3:

```bash
pip3 install beautifulsoup4
```

## Running a test
Once everything is installed you can now pagerank any url simply 
copy and pasting. Below I will show you how to run the program.

### Example
```bash
python3 pageranke.py <url>
```

Once you run it, you should be able to get a page score for the
url you parsed onto the command line.

### Example Output
```bash
Score: [page_score]
```
## Authors
 - Adrian Gutierrez

### License
This project is licensed under the apache License - see the
[LICENCSE.md](https://github.com/agutierrez63/PageRank/blob/master/LICENSE)
file for details.
