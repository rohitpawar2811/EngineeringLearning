# Importing Dashboard POC

1. helpers.py : It contains helper function which takes the input-date and insert into models. like chartMaking from import
2. database/api.py : 
3. dashboard.api.py : here @expose("/import/", methods=("POST",)) is implemented which is called for importing the dashboard.
3. superset/commands/imports.py  : Here Commands are written for database, dashboard ,chart.

### superset/commands/* : 
This will contains the All generic functionality executing cmd. why here reason is that we can operate it from the cmdline also and these cmd can be directly reffered from the apis.

## Noticing Points: 

1. UUID auto generation if user doesn't want ovveride:  Here Check the validation api that imported content already existed or not.
2. I have top check that how it parse the the .yml file 

------------------------------------------------------------------------------------------------------------------------------------------------------
## Knowlege points:

### Why yaml yml file used for import/export?

Here's why YAML (YAML Ain't Markup Language) or .yaml/.yml files are commonly used for configuration:

Human-readable: YAML files use a simple and human-readable syntax, making them easy to write and understand without specialized tools.

Structured data: YAML supports complex data structures like lists, dictionaries, and nested structures. This makes it suitable for representing configurations that may have hierarchical or nested properties.

Support for comments: YAML allows comments, which can be useful for providing additional context or explanations within configuration files.

Language-independent: YAML is not tied to any specific programming language, making it easy to use in a variety of environments and with different programming languages.

Widely supported: YAML is supported by many programming languages through various libraries, making it a versatile choice for configuration files in a multi-language ecosystem.

---------------------------------------------------------------------------------------------------------------------------------------------------------
## Flow Tracking
1. **dict returned by get_contents_from_bundle**
{
    'config1.txt': 'Contents of config1.txt',
    'config2.txt': 'Contents of config2.txt',
    'data/config3.txt': 'Contents of config3.txt',
    'data/config4.txt': 'Contents of config4.txt'
}

2. ImportDatabaseCommand()

-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Here is the geo-code json matintained in the superset


superset/superset-frontend/plugins/legacy-plugin-chart-country-map/src/countries/uk.geojson
https://github.com/apache/superset/blob/master/superset-frontend/plugins/legacy-plugin-chart-country-map/src/countries/india.geojson?short_path=9f708a9

-----------------------------------------------------------------------------------------------------------------------------------------------------------

1st stepes is to fix them at framework level 

from flask_appbuilder import Model
from sqlalchemy.orm import backref, relationship

from superset import security_manager
from superset.columns.models import Column
from superset.models.core import Database
from superset.models.helpers import (
    AuditMixinNullable,
    ExtraJSONMixin,
    ImportExportMixin,
)
from superset.tables.models import Table

dataset_column_association_table = sa.Table(
    "sl_dataset_columns",
    Model.metadata,
    
    
    DASHBOARD_TEMPLATE_ID
---------------------------------------------------------------------------------------------
from superset.extensions import (
    appbuilder,
    cache_manager,
    db,
    event_logger,
    feature_flag_manager,
    manifest_processor,
    results_backend_manager,
    security_manager,
    talisman,
)
from superset.security import SupersetSecurityManager

    
__init__.py
    
#  All of the fields located here should be considered legacy. The correct way
#  to declare "global" dependencies is to define it in extensions.py,
#  then initialize it in app.create_app(). These fields will be removed
#  in subsequent PRs as things are migrated towards the factory pattern

app: Flask = current_app
cache = cache_manager.cache
conf = LocalProxy(lambda: current_app.config)
get_feature_flags = feature_flag_manager.get_feature_flags
get_manifest_files = manifest_processor.get_manifest_files
is_feature_enabled = feature_flag_manager.is_feature_enabled
results_backend = LocalProxy(lambda: results_backend_manager.results_backend)
results_backend_use_msgpack = LocalProxy(
    lambda: results_backend_manager.should_use_msgpack
)
data_cache = LocalProxy(lambda: cache_manager.data_cache)
thumbnail_cache = LocalProxy(lambda: cache_manager.thumbnail_cache)

------------------------------------------------------------------------------------------
Extentions __init__.py

import celery
from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from flask_caching.backends.base import BaseCache
from flask_migrate importcharts Migrate
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from werkzeug.local import LocalProxy

from superset.async_events.async_query_manager import AsyncQueryManager
from superset.async_events.async_query_manager_factory import AsyncQueryManagerFactory
from superset.extensions.ssh import SSHManagerFactory
from superset.extensions.stats_logger import BaseStatsLoggerManager
from superset.utils.cache_manager import CacheManager
from superset.utils.encrypt import EncryptedFieldFactory
from superset.utils.feature_flag_manager import FeatureFlagManager
from superset.utils.machine_auth import MachineAuthProviderFactory
from superset.utils.profiler import SupersetProfiler


Here we are using SqlAlchmey ORM for whole models design part in database

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Change this to your database URI
app.config['SECRET_KEY'] = 'my_secret_key'  # Change this to your secret key

# Initialize SQLAlchemy
db = SQLA(app)

# Initialize Flask-AppBuilder
appbuilder = AppBuilder(app, db.session)

# Define your models here using SQLAlchemy ORM syntax
# For example:
# from sqlalchemy import Column, Integer, String
# class MyModel(db.Model):
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))

-----------------------------------------------------------------
database-UUID
ce6fa853-d7f3-4895-8443-c03f5cef2a0c -> 85b6cacc-07ad-4f29-b027-36ee269245b2

Dataset UUID
1. ADOC HN - UPDATE POSTAL ADDRESS API REPORT
147e2575-1278-446e-933b-964eeeda2ba4 -> 3a924f86-51c4-4b4e-9888-b4e2b3d43db2

2. 
ef3d62f8-0718-43af-92ef-89ebdfc7572c -> c53a9e09-6117-44e6-8b38-3fc41d8f1c13

ADOC HN - ORDER TO INVOICE API REPORT

3. 
c1520b15-ba18-4b5b-8b07-85edb57fc4f8 ->  ebd9fc90-1862-4ee3-8538-0f37beaf24fc

ADOC HN - MANUAL SLIP API REPORT

4.ADOC HN Update Postal Address API Report

5f79a704-ec11-4f53-8fd1-8edcf88119a3 -> 6e564bd4-98f8-414f-87b5-b8745f2d5433


5.
      sliceName: ADOC HN Order to Invoice API Report
      uuid: 1a1b656f-cdc2-4d66-9891-2f71fd3d4f96
      
      799d6e2d-899d-484f-9d6e-cfa4138f19d3
      
6.
      sliceName: ADOC HN Manual Slip API Report
      uuid: d00c66f5-a815-4c6a-8ffb-b2eb7b988b84
      
      0d2c26b9-5e8e-45e6-a38d-8485e779a721
      
7.

ADOC HN logInsights API Report -> 
c0a6c103-9b2b-4215-bded-34573a316d5f ->

f62c8b2d-bb6b-40d7-a98d-d924482ef2b7

Soft Linking


1. Those who is in owner list can add another owner also.
2. But If they are not assigned already they are not able to do anything.
HotwaxBasicBAPermission
BasicBA+SqlLab 

702172812801


variable templatization
Auditing Features

1. Moqui mai code likh sakta hai kya
2. Gitlab api yet optional not to use, directly at the deployment time we would place all files.
3. Data-imports bhi hai nifi side, so we can upload the templates also. 
4. Either we can feach/export the zip directly from superset and then apply the transformations.
5. 

1. First Part : We have a template and we can deploy it for other instances also in one short. 
2. Second Part: Is that we have to maintain the UUID of all uploaded Dashboards Data and when there is a change in existing one we would call the api to update all dashboards at once.



-----