# REACT :

## 1. **useCallback**: 
This is a React hook used for memoizing functions. It memoizes the provided function so that it will only be recreated if any of its dependencies change. This can help optimize performance by preventing unnecessary re-renders of components that depend on this function.

[filters]: This is the dependency array passed to useCallback. It specifies that the memoized function should be re-created if the filters variable changes.

 This function will be recreated only if the filters variable changes.
 
   const isActiveFilterValue = useCallback(
    function isActiveFilterValue(key: string, val: DataRecordValue) {
      return !!filters && filters[key]?.includes(val);
    },
    [filters],
  );

--------------------------------------------------------------------------------------------------------------------------------------------------------------

## 2. **There are some libs and imports to explore about it**

import React, {
  useCallback,
  useRef,
  ReactNode,
  HTMLProps,
  MutableRefObject,
  CSSProperties,
} from 'react';
import {
  useTable,
  usePagination,
  useSortBy,
  useGlobalFilter,
  useColumnOrder,
  PluginHook,
  TableOptions,
  FilterType,
  IdType,
  Row,
} from 'react-table';
import { matchSorter, rankings } from 'match-sorter';


--------------------------------------------------------------------------
## 3. const paginationRef = useRef<HTMLDivElement>(null);

paginationRef: This creates a ref object using the useRef hook to reference a HTMLDivElement element. This ref is presumably intended to be associated with the pagination UI elements of the table.

--------------------------------------------------------------------------
 ## 4. UseState hook : Here we retrived the getters and setters
 
  const [favoriteStatus, setFavoriteStatus] = useState<FavoriteStatus>({});

  const updateFavoriteStatus = (update: FavoriteStatus) =>
    setFavoriteStatus(currentState => ({ ...currentState, ...update }));

----------------------------------------------------------------------------
## 5. React Fragments

A React Fragment is a way to group multiple children elements without adding extra nodes to the DOM. It's particularly useful when you need to return multiple elements from a component's render method but don't want to introduce additional nodes into the DOM hierarchy.

In JSX, when you return multiple elements from a component's render method, you must wrap them in a single parent element. This is because JSX expressions must have a single root element. However, sometimes you may not want to introduce an extra DOM node just for the purpose of wrapping multiple elements.

React Fragments solve this problem by allowing you to group multiple children elements without adding an extra DOM node. Fragments look like empty JSX tags <></> or <React.Fragment></React.Fragment>. Here's how you can use them:

<React.Frgments>
</React.Fragments>

---------------------------------------------------------------------------------
## 6. W3C Learnings

Class 
FunctionalComponent
JSX
Conditional-Rendering
Pure-Function
Controlled Compoenent & Uncontrolled
Props
State
LifeCycle
Input Form, list,map,
Event Handling
Do not use "" with {} we can use js in jsx
React Router
MEMO
STate
Effect
useContext
useRef
useCallback
useReducer : not understood the use-case.
CustomHooks
-----------------------------------------------------------------------
ChartRenderer.jsx

Apache ECharts for mainly for pie and other vis used , D3


Aditya sir want's that we would feach the data from superset throw api and on apps side we can show the data whatever way we want.

Yes very much.Bat can touch the table while serving or any normal stroke.Your body can touch the table until you are not dragging the whole table with your touch force.
Suppose you have to return a stroke which is very close to the the net then you can very much lay down on the table and make the return but remember table should not be moving.
The only condition is that your PALM of the free hand should not touch the surface of the table while making the shot.


REACT :

useCallback: This is a React hook used for memoizing functions. It memoizes the provided function so that it will only be recreated if any of its dependencies change. This can help optimize performance by preventing unnecessary re-renders of components that depend on this function.

[filters]: This is the dependency array passed to useCallback. It specifies that the memoized function should be re-created if the filters variable changes.

 This function will be recreated only if the filters variable changes.
 
   const isActiveFilterValue = useCallback(
    function isActiveFilterValue(key: string, val: DataRecordValue) {
      return !!filters && filters[key]?.includes(val);
    },
    [filters],
  );
  

import React from 'react';
import { SuperChart, getChartTransformPropsRegistry } from '@superset-ui/core';
import { withKnobs } from '@storybook/addon-knobs';
import {
  EchartsGaugeChartPlugin,
  GaugeTransformProps,
} from '@superset-ui/plugin-chart-echarts';
import { withResizableChartDemo } from '../../../../shared/components/ResizableChartDemo';
import { speed } from './data';

new EchartsGaugeChartPlugin().configure({ key: 'echarts-gauge' }).register();

getChartTransformPropsRegistry().registerValue(
  'echarts-gauge',
  GaugeTransformProps,
);

export default {
  title: 'Chart Plugins/plugin-chart-echarts/Gauge',
  decorators: [withKnobs, withResizableChartDemo],
};

export const Gauge = ({ width, height }) => (
  <SuperChart
    chartType="echarts-gauge"
    width={width}
    height={height}
    queriesData={[{ data: speed }]}
    formData={{
      columns: [],
      groupby: ['name'],
      metric: 'value',
    }}
  />
);

https://frank-and-oak-dev-v2.myshopify.com/collections/women-sale


1. Find the entry-point of application.
2. when there is change in the component because of the property. what if it is previouly called from another function, (so what is happening then all parent chain will re-render, ideally this should has to be happen)

SetState() function is change aware 



-----------------------------------------------------------------------------------------------------
## Named Import and default import

import React, { lazy } from 'react'

React: In the react module, React is exported as the default export. When you import a default export, you can name it whatever you want. In this case, it's named React, but you could name it anything you like.

lazy: The lazy function, on the other hand, is not the default export of the react module. It is a named export, which means it has to be imported using its exact name. When importing named exports, you need to wrap the name in curly braces to specify the exact exported entity you want to import.

### NOTE: Here then a question comes that default export just only one in a module or it can be multiple.

-------------------------------------------------------------------------------------------------------
## Lazy, Dynamic WebChunk


const Chart = lazy(
  () => import(/* webpackChunkName: "Chart" */ 'src/pages/Chart'),
);

- lazy is used to asynchronously import the Chart component.
- The import() function inside lazy is a dynamic import statement, which means it tells webpack to split the Chart component code into a separate chunk.
- The comment webpackChunkName: "Chart" is a webpack-specific comment that names the chunk that will be created for the imported module. This name can be useful for debugging and optimizing your webpack bundles.
- So, using lazy in this context allows the Chart component to be loaded lazily (i.e., on-demand) instead of being included in the main bundle, thereby improving the initial loading performance of your application.

loads, reducers, redux, store.js -> where we have created the middleware, reducers, inti() what all this is . 

----------------------------------------------------------------------------------------------------------------
## CORS Related ISsue

Here when I request api from oms then jettey server will request to another server, and even cors enabled it will not call the OPTIONS preflight request unlike chrome browser.

When we hit request api from axios by using React-JS, it will call through the browser, and Browser inforced as in case of cross-origin api call ,that before api-call browser will make a OPTION preflight request and this must be handled by requested Server otherwise it would not request the actual request.

In case of React JS axios hit superset with option it will not respond with 200, it will send 308 by which browser send error or block request.

```
127.0.0.1 - - [20/Feb/2024:13:17:21 +0000] "GET /health HTTP/1.1" 200 2 "-" "curl/7.88.1"
172.20.20.21 - - [20/Feb/2024:13:17:30 +0000] "POST /api/v1/security/login HTTP/1.1" 200 412 "-" "Jetty/9.4.51.v20230217"
172.20.20.21 - - [20/Feb/2024:13:17:30 +0000] "GET /api/v1/chart/3981/data/ HTTP/1.1" 200 4490 "-" "Jetty/9.4.51.v20230217"
127.0.0.1 - - [20/Feb/2024:13:17:51 +0000] "GET /health HTTP/1.1" 200 2 "-" "curl/7.88.1"
172.20.20.21 - - [20/Feb/2024:13:18:13 +0000] "OPTIONS /api/v1/security/login HTTP/1.1" 200 1 "http://localhost:3000/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
172.20.20.21 - - [20/Feb/2024:13:18:13 +0000] "OPTIONS /api/v1/security/guest_token HTTP/1.1" 308 299 "http://localhost:3000/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
172.20.20.21 - - [20/Feb/2024:13:18:13 +0000] "OPTIONS /api/v1/security/guest_token HTTP/1.1" 308 299 "http://localhost:3000/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
172.20.20.21 - - [20/Feb/2024:13:18:13 +0000] "OPTIONS /api/v1/security/login HTTP/1.1" 200 1 "http://localhost:3000/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
172.20.20.21 - - [20/Feb/2024:13:18:13 +0000] "POST /api/v1/security/login HTTP/1.1" 200 411 "http://localhost:3000/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
172.20.20.21 - - [20/Feb/2024:13:18:13 +0000] "POST /api/v1/security/login HTTP/1.1" 200 409 "http://localhost:3000/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

```

https://www.dhiwise.com/post/cors-in-react-essential-techniques-for-web-developers

https://stackoverflow.com/questions/26022794/how-do-i-configure-embedded-jetty-to-handle-options-preflight-requests



1. We can use Proxy to solve this problem 
2. We can enable the Cors on the Connecting side.
3. We can disable core-checking from the browser side by enabling some credential thing. It will solve the problem while devloping an app.
--------------------------------------------------------------------------------------------------------------------------------------------
