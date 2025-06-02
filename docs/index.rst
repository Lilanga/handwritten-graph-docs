Handwritten Graph Library Documentation
========================================

A modern TypeScript library for creating hand-drawn style charts inspired by comics and sketches. Built with D3.js and designed with type safety and excellent developer experience in mind.

.. image:: https://img.shields.io/npm/v/handwritten-graph.svg
   :target: https://www.npmjs.com/package/handwritten-graph
   :alt: npm version

.. image:: https://img.shields.io/npm/dt/handwritten-graph.svg
   :target: https://www.npmjs.com/package/handwritten-graph
   :alt: npm downloads

.. image:: https://img.shields.io/github/license/Lilanga/handwritten-graph-ts.svg
   :target: https://github.com/Lilanga/handwritten-graph-ts/blob/main/LICENSE
   :alt: License

.. image:: https://img.shields.io/badge/TypeScript-Ready-blue.svg
   :target: https://www.typescriptlang.org/
   :alt: TypeScript Ready

Features
--------

✨ **Hand-drawn/sketched visual style** - Authentic comic-book aesthetic

📊 **Multiple chart types** - Line graphs, bar charts, and pie charts

🔧 **TypeScript support** - Full type definitions and IntelliSense

🎯 **Multi-series support** - Handle complex datasets with ease

🎭 **Interactive tooltips** - Hover effects with detailed information

🎪 **Directional scribble fills** - Artistic fill patterns for charts

🎨 **Oil paint textures** - Rich watercolor-like effects

⚙️ **Highly configurable** - Extensive customization options

🧩 **Modern architecture** - Clean OOP design with proper separation of concerns

Quick Start
-----------

Installation
~~~~~~~~~~~~

.. tabs::

   .. tab:: npm

      .. code-block:: bash

         npm install handwritten-graph

   .. tab:: yarn

      .. code-block:: bash

         yarn add handwritten-graph

   .. tab:: CDN

      .. code-block:: html

         <script src="https://unpkg.com/handwritten-graph@latest/dist/handwritten-graph.js"></script>

Basic Usage
~~~~~~~~~~~

.. tabs::

   .. tab:: TypeScript

      .. code-block:: typescript

         import { LineChart, BarChart, PieChart } from 'handwritten-graph';

         // Sample data
         const chartData = {
           labels: ["Q1", "Q2", "Q3", "Q4"],
           datasets: [{
             label: "Revenue",
             data: [65, 59, 80, 81],
             lineColor: "rgb(75, 192, 192)"
           }]
         };

         // Create line chart
         const lineChart = new LineChart("#chart-container", chartData, {
           showArea: true,
           useScribbleFill: true
         });

   .. tab:: JavaScript

      .. code-block:: javascript

         // Using factory functions
         const cleanup = HandwrittenGraph.createGraph("#chart-container", chartData);
         
         // Clean up when done
         cleanup();

Live Demo
~~~~~~~~~

Check out the `interactive demo <https://p7wc4d.csb.app>`_ to see the library in action!

Documentation Contents
----------------------

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   installation
   quick-start

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/line-chart-api
   api/bar-chart-api
   api/pie-chart-api
   api/configuration
   api/types

.. toctree::
   :maxdepth: 2
   :caption: Advanced Topics

   advanced/styling

.. toctree::
   :maxdepth: 2
   :caption: Additional Resources

   changelog

Browser Support
---------------

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Modern mobile browsers

License
-------

MIT License - see `LICENSE <https://github.com/Lilanga/handwritten-graph-ts/blob/main/LICENSE>`_ file for details.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`