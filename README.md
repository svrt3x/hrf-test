# hrf-test

This is a Scrapy project to crawl  HRForecast’s  job  vacancies  (https://www.hrforecast.de/career/)
and  Gazprom’s  job  vacancies  (https://www.gazpromvacancy.ru/jobs/) and save information into xslx file.

This project is only meant for educational purposes.


## Dependencies

- Python 3.7
- Scrapy
- opnpyxl

## Installing

To install **Scrapy** use these installations guide 
https://docs.scrapy.org/en/latest/intro/install.html

To install **opnpyxl** use these instructions 
https://openpyxl.readthedocs.io/en/stable/#installation

If you use Anaconda, you don't need to install **opnpyxl**.


## Running

To run spiders just execute script **crawl.sh**
or run comands below in the project directory

```
scrapy crawl hrforecast
scrapy crawl gazprom
```
The program will append data to result file. If you want to get new result file, you should delete **jobs.xlsx** from project directory.

## Output data
You can find result data in file **jobs.xlsx** in project directory
