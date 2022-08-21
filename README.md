# python-binance-stream-all-currencies-into-mssql-db

--- Do not forget to install --- Dependencies:

schedule: pip install schedule

urllib: pip install urllib3
    - should not be necessary to install, but if you don't have it, use pip to install it
    - if it doesn't work, use:

    python -m pip install urllib3

    The -m flag makes sure that you are using the pip that's tied to the active Python executable.

pyodbc: pip install pyodbc