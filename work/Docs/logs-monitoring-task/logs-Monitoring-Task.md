## Capturing Patterns :

1. DB got some problem Here

requests.exceptions.ConnectionError: HTTPSConnectionPool(host='dev-oms.hotwax.io', port=443): Max retries exceeded with url: /search/instance1Details/select (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7ff6e2dede80>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))


requests.exceptions.ConnectionError: HTTPSConnectionPool(host='dev-oms.hotwax.io', port=443): Max retries exceeded with url: /search/instance1Details/select (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7ff6e2dede80>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))
logging was configured successfully

requests.exceptions.ConnectionError: HTTPSConnectionPool(host='dev-oms.hotwax.io', port=443): Max retries exceeded with url: /search/instance1Details/select (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7ff6e2dede80>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))
logging was configured successfully

2. When someone has the chart on dashboard but doesn't have access for that. and hit a error that datasource not allowed

3. DNS like of error 

4. Report execution failed error

5. If superset shift to another instance then we can set something no-data configuration, because of which when no data came then we got nofitication for that.


    raise SupersetErrorsException(errors) from ex
superset.exceptions.SupersetErrorsException: [SupersetError(message='Either the username "kreweoms" or the password is incorrect.', error_type=<SupersetErrorType.CONNECTION_ACCESS_DENIED_ERROR: 'CONNECTION_ACCESS_DENIED_ERROR'>, level=<ErrorLevel.ERROR: 'error'>, extra={'invalid': ['username', 'password'], 'engine_name': 'MySQL', 'issue_codes': [{'code': 1014, 'message': 'Issue 1014 - Either the username or the password is wrong.'}, {'code': 1015, 'message': 'Issue 1015 - Either the database is spelled incorrectly or does not exist.'}]})]


6. DBAPIError(ex_str or None, None, None)
sqlalchemy.exc.DBAPIError: (builtins.NoneType) None
[SQL: (MySQLdb._exceptions.OperationalError) (1044, "Access denied for user 'kreweoms'@'%' to database 'kreweoms1'")
(Background on this error at: https://sqlalche.me/e/14/e3q8)]
(Background on this error at: https://sqlalche.me/e/14/dbapi)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 1823, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 1799, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
  File "/usr/local/lib/python3.9/site-packages/flask_appbuilder/security/decorators.py", line 95, in wraps
    return f(self, *args, **kwargs)
  File "/app/superset/views/base_api.py", line 127, in wraps
    raise ex
  File "/app/superset/views/base_api.py", line 121, in wraps
    duration, response = time_function(f, self, *args, **kwargs)
  File "/app/superset/utils/core.py", line 1526, in time_function
    response = func(*args, **kwargs)
  File "/app/superset/utils/log.py", line 255, in wrapper
    value = f(*args, **kwargs)
  File "/app/superset/views/base_api.py", line 93, in wraps
    return f(self, *args, **kwargs)
  File "/app/superset/databases/api.py", line 908, in test_connection
    TestConnectionDatabaseCommand(item).run()
  File "/app/superset/databases/commands/test_connection.py", line 192, in run
    raise SupersetErrorsException(errors) from ex
superset.exceptions.SupersetErrorsException: [SupersetError(message='Either the username "kreweoms" or the password is incorrect.', error_type=<SupersetErrorType.CONNECTION_ACCESS_DENIED_ERROR: 'CONNECTION_ACCESS_DENIED_ERROR'>, level=<ErrorLevel.ERROR: 'error'>, extra={'invalid': ['username', 'password'], 'engine_name': 'MySQL', 'issue_codes': [{'code': 1014, 'message': 'Issue 1014 - Either the username or the password is wrong.'}, {'code': 1015, 'message': 'Issue 1015 - Either the database is spelled incorrectly or does not exist.'}]})]
logging was configured successfully


mysql+mysqldb://kreweoms:Ht5#nkreweoms@54.163.241.153:3306/kreweoms

startsWith -> 

==================================================================================================
## Intraday allows you to short sell

1. Short sell means that you can sell shares before buying them. In this case margin amount will be on hold till the position is squared off.

2. Intraday let’s you buy a stock “on margin”.
      If the margin is 20%, you can buy 5x shares for the same amount.
      Hence trading on margin magnifies not just profits but also losses by 5x.

3. Intraday orders get squared off when the market closes. Which means a buy/sell position opened during the day is reversed (sell/buy) before the market closes.
You can place these orders on margin i.e. you pay fraction of the total price. But it is risky.
==================================================================================================
## Multi-Threading

Multi-Threading will process the whole content in the in memory, so this will cause spike, so now we are finding a way that it will process the data from a pyhsical file not from inmemory.

still it make system processing slow but we would get advantage for stability .

kubernetes will deploy another container when because of something one container goes down. It will cause the re-run of same bulk jobs schedule which.
========================================================================================================

1. DB got some problem Here

requests.exceptions.ConnectionError: HTTPSConnectionPool(host='dev-oms.hotwax.io', port=443): Max retries exceeded with url: /search/instance1Details/select (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7ff6e2dede80>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))


requests.exceptions.ConnectionError: HTTPSConnectionPool(host='dev-oms.hotwax.io', port=443): Max retries exceeded with url: /search/instance1Details/select (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7ff6e2dede80>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))
logging was configured successfully

requests.exceptions.ConnectionError: HTTPSConnectionPool(host='dev-oms.hotwax.io', port=443): Max retries exceeded with url: /search/instance1Details/select (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7ff6e2dede80>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))
logging was configured successfully

2. When someone has the chart on dashboard but doesn't have access for that. and hit a error that datasource not allowed

3.DNS like of error 

4.Report execution failed error

5. If superset shift to another instance then we can set something no-data configuration, because of which when no data came then we got nofitication for that.


    raise SupersetErrorsException(errors) from ex
superset.exceptions.SupersetErrorsException: [SupersetError(message='Either the username "kreweoms" or the password is incorrect.', error_type=<SupersetErrorType.CONNECTION_ACCESS_DENIED_ERROR: 'CONNECTION_ACCESS_DENIED_ERROR'>, level=<ErrorLevel.ERROR: 'error'>, extra={'invalid': ['username', 'password'], 'engine_name': 'MySQL', 'issue_codes': [{'code': 1014, 'message': 'Issue 1014 - Either the username or the password is wrong.'}, {'code': 1015, 'message': 'Issue 1015 - Either the database is spelled incorrectly or does not exist.'}]})]


6. DBAPIError(ex_str or None, None, None)
sqlalchemy.exc.DBAPIError: (builtins.NoneType) None
[SQL: (MySQLdb._exceptions.OperationalError) (1044, "Access denied for user 'kreweoms'@'%' to database 'kreweoms1'")
(Background on this error at: https://sqlalche.me/e/14/e3q8)]
(Background on this error at: https://sqlalche.me/e/14/dbapi)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 1823, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 1799, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
  File "/usr/local/lib/python3.9/site-packages/flask_appbuilder/security/decorators.py", line 95, in wraps
    return f(self, *args, **kwargs)
  File "/app/superset/views/base_api.py", line 127, in wraps
    raise ex
  File "/app/superset/views/base_api.py", line 121, in wraps
    duration, response = time_function(f, self, *args, **kwargs)
  File "/app/superset/utils/core.py", line 1526, in time_function
    response = func(*args, **kwargs)
  File "/app/superset/utils/log.py", line 255, in wrapper
    value = f(*args, **kwargs)
  File "/app/superset/views/base_api.py", line 93, in wraps
    return f(self, *args, **kwargs)
  File "/app/superset/databases/api.py", line 908, in test_connection
    TestConnectionDatabaseCommand(item).run()
  File "/app/superset/databases/commands/test_connection.py", line 192, in run
    raise SupersetErrorsException(errors) from ex
superset.exceptions.SupersetErrorsException: [SupersetError(message='Either the username "kreweoms" or the password is incorrect.', error_type=<SupersetErrorType.CONNECTION_ACCESS_DENIED_ERROR: 'CONNECTION_ACCESS_DENIED_ERROR'>, level=<ErrorLevel.ERROR: 'error'>, extra={'invalid': ['username', 'password'], 'engine_name': 'MySQL', 'issue_codes': [{'code': 1014, 'message': 'Issue 1014 - Either the username or the password is wrong.'}, {'code': 1015, 'message': 'Issue 1015 - Either the database is spelled incorrectly or does not exist.'}]})]
logging was configured successfully

7. Exception: Error while executing SQL: The specified TABLE-NAME is incorrect.





mysql+mysqldb://kreweoms:Ht5#nkreweoms@54.163.241.153:3306/kreweoms

startsWith -> ke saat regex pattern banana hai, perpare it and take it as is the logs

and now here's different thing happend is that 

==================================================================================================

==================================================================================================

Multi-Threading will process the whole content in the in memory, so this will cause spike, so now we are finding a way that it will process the data from a pyhsical file not from inmemory.

still it make system processing slow but we would get advantage for stability .

kubernetes will deploy another container when because of something one container goes down. It will cause the re-run of same bulk jobs schedule which.







requests.exceptions.ConnectionError


SupersetErrorException




(?P<superset_line>.*requests.exceptions.ConnectionError.*)
==================================================================================================	
================================================================================================

2024-02-26 18:13:04	
       `API Request Body` AS `API Request Body`
       
       
       
       
       
       
       
       
       
       count_over_time({job="nifi-uat.hotwax.io"} |~ `\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+ ERROR \[Timer-Driven Process Thread-\d] .*` [15m])
       
       Return log lines that match regex
       
       
-------------------------------------------------------------

{job="nifi-uat.hotwax.io"} |~ `\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+ ERROR .*`
Return log lines that match regex
Fetch all log lines matching label filters.


1. SupersetErrorsException

.*SupersetErrorsException.*

.*SupersetError.*

.*superset.exceptions.SupersetErrorsException.*

------------------------------------------------------------

//While doing Query
Exception: Error while executing SQL: The specified TABLE-NAME is incorrect.

------------------------------------------------------------
//While email Got the same error.

Query SELECT `instanceUrl` AS `instanceUrl`,
       `builtOn` AS `builtOn`,
       branch AS branch,
       `systemInfo.instanceName` AS `systemInfo.instanceName`,
       `systemInfo.javaVersion` AS `systemInfo.javaVersion`,
       `systemInfo.serverTimezone` AS `systemInfo.serverTimezone`,
       `searchServer.searchHost` AS `searchServer.searchHost`,
       `systemInfo.uniqueInstanceId` AS `systemInfo.uniqueInstanceId`,
       `searchServer.cloudEnabled` AS `searchServer.cloudEnabled`,
       `searchServer.searchServerVersion` AS `searchServer.searchServerVersion`,
       revision AS revision,
       `docType` AS `docType`
FROM
  (Select *
   from instanceDetails) AS virtual_table
LIMIT 1000 on schema default failed
Traceback (most recent call last):
  File "/app/superset/connectors/sqla/models.py", line 1212, in query
    df = self.database.get_df(sql, self.schema, mutator=assign_column_label)
  File "/app/superset/models/core.py", line 611, in get_df
    self.db_engine_spec.execute(cursor, sqls[-1])
  File "/app/superset/db_engine_specs/solr.py", line 153, in execute
    raise cls.get_dbapi_mapped_exception(ex) from ex
  File "/app/superset/db_engine_specs/solr.py", line 151, in execute
    cursor.execute(query)
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy_solr/solrdbapi/_solrdbapi.py", line 73, in func_wrapper
    return func(self, *args, **kwargs)  # pylint: disable=not-callable
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy_solr/solrdbapi/_solrdbapi.py", line 148, in execute
    raise Exception(rows[0]["EXCEPTION"])
Exception: Error while executing SQL: The specified TABLE-NAME is incorrect.

-----------------------------------------------------------------------------------
3.

Traceback (most recent call last):
  File "/app/superset/databases/commands/test_connection.py", line 163, in run
    raise DBAPIError(ex_str or None, None, None)
sqlalchemy.exc.DBAPIError: (builtins.NoneType) None
[SQL: HTTPSConnectionPool(host='-oms.hotwax.io', port=443): Max retries exceeded with url: /search/instance1Details/select (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f8a1b757040>: Failed to establish a new connection: [Errno -2] Name or service not known'))]
(Background on this error at: https://sqlalche.me/e/14/dbapi)

---------------

1. zip mai can we change the name of reports and details of pre-existed reports.
2. we can maintain somewhere, form that we can get the zip data and transformation code will change the 

1. .*SupersetError\(message="\(builtins\.NoneType\) None\\n\[SQL: .*
2. .*superset.exceptions.SupersetErrorsException.*

3. .*SupersetError\(message=["']\(builtins\.NoneType\) None\\n\[SQL: .*

Combined one Shot to match all necceary part 




<!-- -------------------------------------------------------------------------------------------------------------------------- -->
## ERROR Findings For Monitoring:

1. In case of Solr URI wrong configured this error will come

**Error** : 

 [SupersetError(message='(builtins.NoneType) None\n[SQL: Error 404 (Not Found) in response to GET to https://search-uat.hotwax.io:8983/solr/dev-oms-instance1Details/sql?stmt=SELECT+1+FROM+%28values%281%29%29]\n(Background on this error at: https://sqlalche.me/e/14/dbapi)', error_type=<SupersetErrorType.GENERIC_DB_ENGINE_ERROR: 'GENERIC_DB_ENGINE_ERROR'>, level=<ErrorLevel.ERROR: 'error'>, extra={'engine_name': 'Apache Solr', 'issue_codes': [{'code': 1002, 'message': 'Issue 1002 - The database returned an unexpected error.'}]})]

**Regex** : SupersetError\(message=["']\(builtins\.NoneType\) None\\n\[SQL: .*


2. In case of krewe oms host not reached got this error

**Error** :

Query SELECT `ORDER_ID` AS `ORDER_ID`,
       `ORDER_TYPE_ID` AS `ORDER_TYPE_ID`,
       `ORDER_NAME` AS `ORDER_NAME`,
       `EXTERNAL_ID` AS `EXTERNAL_ID`,
       `SALES_CHANNEL_ENUM_ID` AS `SALES_CHANNEL_ENUM_ID`,
       `ORDER_DATE` AS `ORDER_DATE`,
       `PRIORITY` AS `PRIORITY`,
       `ENTRY_DATE` AS `ENTRY_DATE`,
       `PICK_SHEET_PRINTED_DATE` AS `PICK_SHEET_PRINTED_DATE`,
       `VISIT_ID` AS `VISIT_ID`,
       `STATUS_ID` AS `STATUS_ID`,
       `CREATED_BY` AS `CREATED_BY`,
       `FIRST_ATTEMPT_ORDER_ID` AS `FIRST_ATTEMPT_ORDER_ID`,
       `CURRENCY_UOM` AS `CURRENCY_UOM`,
       `SYNC_STATUS_ID` AS `SYNC_STATUS_ID`,
       `BILLING_ACCOUNT_ID` AS `BILLING_ACCOUNT_ID`,
       `ORIGIN_FACILITY_ID` AS `ORIGIN_FACILITY_ID`,
       `WEB_SITE_ID` AS `WEB_SITE_ID`,
       `PRODUCT_STORE_ID` AS `PRODUCT_STORE_ID`,
       `TERMINAL_ID` AS `TERMINAL_ID`,
       `TRANSACTION_ID` AS `TRANSACTION_ID`,
       `AUTO_ORDER_SHOPPING_LIST_ID` AS `AUTO_ORDER_SHOPPING_LIST_ID`,
       `NEEDS_INVENTORY_ISSUANCE` AS `NEEDS_INVENTORY_ISSUANCE`,
       `IS_RUSH_ORDER` AS `IS_RUSH_ORDER`,
       `INTERNAL_CODE` AS `INTERNAL_CODE`,
       `REMAINING_SUB_TOTAL` AS `REMAINING_SUB_TOTAL`,
       `GRAND_TOTAL` AS `GRAND_TOTAL`,
       `IS_VIEWED` AS `IS_VIEWED`,
       `INVOICE_PER_SHIPMENT` AS `INVOICE_PER_SHIPMENT`,
       `LAST_UPDATED_STAMP` AS `LAST_UPDATED_STAMP`,
       `LAST_UPDATED_TX_STAMP` AS `LAST_UPDATED_TX_STAMP`,
       `CREATED_STAMP` AS `CREATED_STAMP`,
       `CREATED_TX_STAMP` AS `CREATED_TX_STAMP`,
       `EXPIRE_DATE` AS `EXPIRE_DATE`,
       `LOCALE_STRING` AS `LOCALE_STRING`,
       `CUSTOMER_CLASSIFICATION_ID` AS `CUSTOMER_CLASSIFICATION_ID`
FROM
  (select *
   from order_header) AS virtual_table
LIMIT 1000 on schema None failed
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 3280, in _wrap_pool_connect
    return fn()
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 310, in connect
    return _ConnectionFairy._checkout(self)
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 868, in _checkout
    fairy = _ConnectionRecord.checkout(pool)
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 476, in checkout
    rec = pool._do_get()
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy/pool/impl.py", line 256, in _do_get
    return self._create_connection()
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 256, in _create_connection
    return _ConnectionRecord(self)
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 371, in __init__
    self.__connect()
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 666, in __connect
    pool.logger.debug("Error on connect(): %s", e)
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy/util/langhelpers.py", line 70, in __exit__
    compat.raise_(
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
    raise exception
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 661, in __connect
    self.dbapi_connection = connection = pool._invoke_creator(self)
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy/engine/create.py", line 590, in connect
    return dialect.connect(*cargs, **cparams)
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 597, in connect
    return self.dbapi.connect(*cargs, **cparams)
  File "/usr/local/lib/python3.9/site-packages/MySQLdb/__init__.py", line 123, in Connect
    return Connection(*args, **kwargs)
  File "/usr/local/lib/python3.9/site-packages/MySQLdb/connections.py", line 185, in __init__
    super().__init__(*args, **kwargs2)
MySQLdb._exceptions.OperationalError: (2002, "Can't connect to server on '54.163.241.158' (115)")

**Regex** : 
MySQLdb._exceptions.OperationalError: (2002.*

3. In case if Database password changed then this error came.

**Error** :

sqlalchemy.exc.DBAPIError: (builtins.NoneType) None
[SQL: (MySQLdb._exceptions.OperationalError) (1044, "Access denied for user 'kreweoms'@'%' to database 'kreweoms1'")
(Background on this error at: https://sqlalche.me/e/14/e3q8)]
(Background on this error at: https://sqlalche.me/e/14/dbapi)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 1823, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 1799, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
  File "/usr/local/lib/python3.9/site-packages/flask_appbuilder/security/decorators.py", line 95, in wraps
    return f(self, *args, **kwargs)
  File "/app/superset/views/base_api.py", line 127, in wraps
    raise ex
  File "/app/superset/views/base_api.py", line 121, in wraps
    duration, response = time_function(f, self, *args, **kwargs)
  File "/app/superset/utils/core.py", line 1526, in time_function
    response = func(*args, **kwargs)
  File "/app/superset/utils/log.py", line 255, in wrapper
    value = f(*args, **kwargs)
  File "/app/superset/views/base_api.py", line 93, in wraps
    return f(self, *args, **kwargs)
  File "/app/superset/databases/api.py", line 908, in test_connection
    TestConnectionDatabaseCommand(item).run()
  File "/app/superset/databases/commands/test_connection.py", line 192, in run
    raise SupersetErrorsException(errors) from ex
superset.exceptions.SupersetErrorsException: [SupersetError(message='Either the username "kreweoms" or the password is incorrect.', error_type=<SupersetErrorType.CONNECTION_ACCESS_DENIED_ERROR: 'CONNECTION_ACCESS_DENIED_ERROR'>, level=<ErrorLevel.ERROR: 'error'>, extra={'invalid': ['username', 'password'], 'engine_name': 'MySQL', 'issue_codes': [{'code': 1014, 'message': 'Issue 1014 - Either the username or the password is wrong.'}, {'code': 1015, 'message': 'Issue 1015 - Either the database is spelled incorrectly or does not exist.'}]})]
logging was configured successfully

**Regex** : 

superset.exceptions.SupersetErrorsException.*
.*SupersetError\(message=["']\Either the username.*

4. When someone has the chart on dashboard but doesn't have access for that. and hit a error that datasource not allowed : 

5. DNS like of error : Know way to check 

6. Report execution failed error : not possible as error not logged.

----------------------------------------------------------------------------------------------------------------------------------------

## Now we have to monitor the logs for the Ofbiz-OMS

Starting from the sm-uat

 GC
2. Connection Failure
3. Index Out of bounds
4. Solr-Failure
5. DB Failure

1. Exception related to service

\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} \|.*\|.*\|E\| Server refused connection.*

2. DB Connection one
Caused by: java\.net\.ConnectException: Connection refused \(Connection refused\).*

(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d{3} \|[\w-]+ +\|[\w.]+ +\|E\| Failure in findListIteratorByCondition operation for entity \[DynamicView\]: org\.apache\.ofbiz\.entity\.GenericDataSourceException: Unable to establish a connection with the database.*


3. OutOf Memmory Heap Space

Exception in thread "[\w-]+" java\.lang\.OutOfMemoryError: Java heap space.*

4. Concurrent-one Error

java\.util\.concurrent\.ExecutionException: java\.lang\.OutOfMemoryError: Java heap space.*

5. Natio something ERror

Exception\s+in\s+thread\s+".*?"\s+java\.lang\.OutOfMemoryError:\s+Java\s+heap\s+space



