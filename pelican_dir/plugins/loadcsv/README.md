# pelican-loadcsv

CSV loader in Python Pelican's templates.

## Usage

Within a pelican template:

    {% csv 'data-sbp.csv' %}

or 

    {% csv '''
    a,b,c,d,e
    1,1,1,1,1
    2,2,2,2,2
    3,3,3,3,3
    4,4,4,4,4
    5,5,5,5,5
    '''%}
