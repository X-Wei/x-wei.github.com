Title: [Spark MOOC note] Lec5. Semi-structured Data
Date: 2015-06-17
Slug: sparkmooc_note_lec5
Tags: spark
Series: spark MOOC
 
[TOC]  

KEY DATA MANAGEMENT CONCEPTS
----------------------------
data model: collection of concepts for describing data
schema: a description of a particular collection of data using a given data model

structure spectrum:   
![](../images/sparkmooc_note_lec5/pasted_image.png)
semi-structured data: apply schema **after** creating data. 

FILES
-----
files: named collection of bytes, in hierarchical namespace (but: In a Content-Addressable Storage system files are stored, arranged, and accessed based on their content or metadata, not in hierarchy)

SEMI-STRUCTURED TABULAR DATA
----------------------------
table: a collection of rows and columns, each row has an *index*, each column has a *name*. 
cell: by a pair (row, col), values can be missing, types are *inffered* from content

CSV:  
![](../images/sparkmooc_note_lec5/pasted_image002.png)

PDB:(filed name can be repeated on multuple lines)    
![](../images/sparkmooc_note_lec5/pasted_image001.png) 


CHALLENGES WITH TABULAR DATA
----------------------------
challenges:   
![](../images/sparkmooc_note_lec5/pasted_image003.png)

challenges for tabular data *from multiple source*:   
![](../images/sparkmooc_note_lec5/pasted_image004.png)

challenges for tabular data *from sensors*:   
![](../images/sparkmooc_note_lec5/pasted_image005.png)


PANDAS AND SEMI-STRUCTURED DATA IN PYSPARK
------------------------------------------
pandas ``DataFrame``: represented as python dict (colname → series)
pandas ``Series``: 1D labeled array capable of holding any data type

**spark DataFrame**: *Distributed* collection of data organized into named columns. 
types of columns are inferred from values. 

![](../images/sparkmooc_note_lec5/pasted_image006.png)

Using dataframes can be 5 times faster than using RDDs:   
![](../images/sparkmooc_note_lec5/pasted_image007.png)

SEMI-STRUCTURED LOG FILES
-------------------------
ex. Apache web server log format

EXPLORING A WEB SERVER ACCESS LOG
---------------------------------
NASA http server access log  
<http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html>

DATA MINING LOG FILES
---------------------
Data mining log files is a data exploration process that often involves searching through the data for unusual events, a task that can be done using dashboards for visualizing anomalies. The data being analyzed usually includes machine resource usage data and application queue information.

FILE PERFORMANCE
----------------
binary/text performance benchmark:  
![](../images/sparkmooc_note_lec5/pasted_image008.png)  
⇒

* read and write times are comparable 
* binary files are mach faster than palin text files


compression performance benchmark:  
![](../images/sparkmooc_note_lec5/pasted_image009.png)  
⇒ 

* write times are much larger than read times 
* small range of compressed file size
* binary still much faster than text 
* LZ4 compression ~= raw IO speed




