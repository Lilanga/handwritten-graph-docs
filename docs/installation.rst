Installation
============

The Handwritten Graph Library can be installed in several ways depending on your project setup and preferences.

Package Managers
----------------

npm
~~~

.. code-block:: bash

   npm install handwritten-graph

yarn
~~~~

.. code-block:: bash

   yarn add handwritten-graph

pnpm
~~~~

.. code-block:: bash

   pnpm add handwritten-graph

CDN
---

For quick prototyping or when you don't want to set up a build process:

.. code-block:: html

   <!-- Latest version -->
   <script src="https://unpkg.com/handwritten-graph@latest/dist/handwritten-graph.js"></script>

   <!-- Specific version (recommended for production) -->
   <script src="https://unpkg.com/handwritten-graph@1.0.5/dist/handwritten-graph.js"></script>

   <!-- With D3.js dependency -->
   <script src="https://d3js.org/d3.v7.min.js"></script>
   <script src="https://unpkg.com/handwritten-graph@1.0.5/dist/handwritten-graph.js"></script>

Requirements
------------

Dependencies
~~~~~~~~~~~~

The library has the following peer dependencies:

- **D3.js v7.0.0+** - Used for data visualization and DOM manipulation
- **Modern browser** - Supports ES2020+ features

.. note::
   D3.js is listed as a peer dependency, so you'll need to install it separately if it's not already in your project.

System Requirements
~~~~~~~~~~~~~~~~~~~

**Node.js**: Version 16.0.0 or higher (for development)

**Browsers**:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Modern mobile browsers

TypeScript Support
------------------

The library includes full TypeScript definitions out of the box. No additional type packages are needed.

.. code-block:: typescript

   import { LineChart, LineChartData, LineChartConfig } from 'handwritten-graph';

Verification
------------

After installation, you can verify everything is working correctly:

.. tabs::

   .. tab:: Node.js/Webpack

      .. code-block:: javascript

         // test.js
         import { LineChart } from 'handwritten-graph';
         
         console.log('Handwritten Graph Library loaded successfully!');
         console.log(LineChart);

   .. tab:: Browser/CDN

      .. code-block:: html

         <!DOCTYPE html>
         <html>
         <head>
             <title>Test Installation</title>
         </head>
         <body>
             <div id="test-chart"></div>
             
             <script src="https://d3js.org/d3.v7.min.js"></script>
             <script src="https://unpkg.com/handwritten-graph@latest/dist/handwritten-graph.js"></script>
             <script>
                 console.log('HandwrittenGraph:', typeof HandwrittenGraph);
                 console.log('Available charts:', Object.keys(HandwrittenGraph));
             </script>
         </body>
         </html>

Troubleshooting
---------------

Common Installation Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Module not found errors**:

.. code-block:: bash

   # Clear npm cache
   npm cache clean --force
   
   # Delete node_modules and reinstall
   rm -rf node_modules package-lock.json
   npm install

**TypeScript errors**:

Make sure your ``tsconfig.json`` includes the appropriate settings:

.. code-block:: json

   {
     "compilerOptions": {
       "moduleResolution": "node",
       "esModuleInterop": true,
       "allowSyntheticDefaultImports": true
     }
   }

**D3.js version conflicts**:

Ensure you're using D3.js v7.0.0 or later:

.. code-block:: bash

   npm list d3
   # If outdated, update:
   npm update d3

Webpack Configuration
~~~~~~~~~~~~~~~~~~~~~

If you're using Webpack, you might need to configure externals for D3:

.. code-block:: javascript

   // webpack.config.js
   module.exports = {
     externals: {
       d3: 'd3'
     }
   };

Next Steps
----------

Once installed, check out the :doc:`quick-start` guide to create your first chart!