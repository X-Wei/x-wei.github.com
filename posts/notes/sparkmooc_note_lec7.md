Title: [Spark MOOC note] Lec7. Data Quality
Date: 2015-06-22
Slug: sparkmooc_note_lec7
Tags: spark

DATA CLEANING
-------------
ex. 
deal with missing data, entity resolution, unit mismatch, ... 

deal with non-ideal samples ⇒ tradeoff between simplicity and accuracy. 

DATA QUALITY PROBLEMS
---------------------
data quality problems: 

* Conversions in complex pipelines can mess up data 
* Combining multiple datasets can result in errrors
* Data degrades in accuracy or loses value over time


还提供了一些工具帮助cleaning data: <http://vis.stanford.edu/wrangler/>

EXAMPLE: AGES OF STUDENTS IN THIS COURSE
----------------------------------------
(students' ages are self-reported...)  
![](sparkmooc_note_lec7/pasted_image.png)

DATA CLEANING MAKES EVERYTHING OKAY?
------------------------------------
ex. the appearance of a hole in the ozone layer. 

DIRTY DATA PROBLEMS
-------------------
![](sparkmooc_note_lec7/pasted_image001.png)

Data Quality Continuum:  
![](sparkmooc_note_lec7/pasted_image002.png)

DATA GATHERING
--------------
solutions in the data gathering stage: 

* re-emptive (先发制人) 

integrity checks

* retrospective

duplicate removal


DATA DELIVERY
-------------
solutions:   
![](sparkmooc_note_lec7/pasted_image003.png)

DATA STORAGE
------------
physical pb: storage is cheap → use data redundancy 
logical pb: poor metadata, etc

⇒ solutions:

* publish *data specifications*
* data mining tools



DATA RETRIEVAL
--------------
...总之就是各种方面都会引起data quality pb... 

DATA QUALITY CONSTRAINTS
------------------------
static constraints: 
ex. nulls not allowed, field domains

data constraints follow a 80-20 rule:   
![](sparkmooc_note_lec7/pasted_image004.png)

**Data quality metrics**: ...
ex. in lab2, examine log lines that are not correctly parsed.

TECHNICAL APPROACHES TO DATA QUALITY
------------------------------------
ex. entity resolution in lab3

EXAMPLE: DEDUP/CLEANING
-----------------------
bing shopping被黑了
convert to *canonical form *(ex. mailing address)

