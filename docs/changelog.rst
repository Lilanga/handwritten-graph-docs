Changelog
=========

All notable changes to the Handwritten Graph Library are documented here.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

v1.0.5 - 2025-05-XX
--------------------

**Added**

🎯 **BarChart Support**
   - New ``BarChart`` class with vertical and horizontal orientations
   - Multi-series support for grouped bar charts
   - Value labels on bars with ``showValues`` option
   - Configurable bar spacing and grouping

🎨 **Enhanced Visual Features**
   - Area fill support for LineCharts with ``showArea`` option
   - Improved scribble fill patterns for all chart types
   - Better responsive design and styling
   - Seamless pie chart borders matching slice colors

**Improved**

- Enhanced type definitions with stricter typing
- Better error handling for invalid data
- Improved performance for large datasets
- More robust data validation and processing

**Fixed**

- Fixed tooltip positioning issues on mobile devices
- Resolved memory leaks in chart destruction
- Fixed color generation for charts without explicit colors
- Improved accessibility features

v1.0.4 - 2025-05-XX
--------------------

**Added**

- Comprehensive test suite with Jest
- Test coverage reporting
- Type checking in build scripts
- Type definition validation in publishing

**Changed**

- Updated build process to include type validation
- Improved CI/CD pipeline for better quality assurance

**Fixed**

- Fixed issue with TypeScript definitions not being properly exported
- Resolved test environment configuration issues

v1.0.3 - 2025-04-XX
--------------------

**Added**

- Complete test suite for all chart types
- Test setup with D3 mocks for better testing
- Example HTML file to preview built library
- Coverage reporting and thresholds

**Improved**

- Better test organization and structure
- Enhanced mock implementations for D3 functions
- Improved build validation process

v1.0.2 - 2025-04-XX
--------------------

**Added**

🎨 **Enhanced Styling System**
   - Text elements with proper SVG property handling
   - Comprehensive axes and grid styling
   - Enhanced line chart visual elements
   - Improved pie chart rendering
   - Legend and tooltip styling improvements

🖋️ **Hand-Drawn Effects**
   - Refined hand-drawn path generation
   - Better stroke rendering with configurable line caps and joins
   - Improved randomization algorithms for more natural appearance

📱 **Responsive Design**
   - Mobile-friendly touch interactions
   - Responsive layout adjustments
   - Improved scaling for different screen sizes

🖨️ **Print Compatibility**
   - Print-specific CSS styles
   - Optimized rendering for print media

**Fixed**

- Resolved SVG rendering issues in different browsers
- Fixed tooltip positioning edge cases
- Improved performance on mobile devices

v1.0.1 - 2025-04-XX
--------------------

**Enhanced**

- Improved TypeScript type definitions for better IDE support
- Enhanced performance optimization for large datasets
- Better error handling and validation

**Fixed**

- Fixed issues with legend positioning in certain configurations
- Resolved tooltip flickering in some browsers
- Improved memory management for chart cleanup

v1.0.0 - 2025-04-XX
--------------------

**🎉 Initial Release**

Complete TypeScript rewrite of the original `handwritten-graph <https://github.com/Lilanga/handwritten-graph>`_ library.

**Core Features**

📊 **Chart Types**
   - LineChart with multi-series support
   - PieChart with donut chart capability
   - Interactive tooltips and legends

🎨 **Visual Features**
   - Hand-drawn aesthetic with configurable jitter
   - Scribble fill patterns (directional and oil paint styles)
   - XKCD-style visual effects
   - Customizable color schemes

🔧 **Technical Features**
   - Full TypeScript support with comprehensive type definitions
   - Modern ES6+ class-based architecture
   - D3.js v7 integration
   - UMD build for browser compatibility
   - Factory functions for backward compatibility

🎯 **Developer Experience**
   - IntelliSense support in TypeScript and modern JavaScript editors
   - Comprehensive documentation and examples
   - Clean OOP design with proper separation of concerns
   - Extensive configuration options

**Architecture**

- **Object-Oriented Design**: Charts are classes with proper encapsulation
- **Type Safety**: Full TypeScript definitions with strict typing
- **Composition**: Modular utilities and components
- **Inheritance**: Base chart class with shared functionality
- **Factory Pattern**: Backward-compatible factory functions
- **Strategy Pattern**: Pluggable fill styles and effects

Migration Guide
===============

Migrating from v1.0.4 to v1.0.5
--------------------------------

**New BarChart Features**

If you're upgrading to use the new BarChart functionality:

.. code-block:: typescript

   // Before: Only LineChart and PieChart were available
   import { LineChart, PieChart } from 'handwritten-graph';

   // After: BarChart is now available
   import { LineChart, BarChart, PieChart } from 'handwritten-graph';

   // New BarChart usage
   const barChart = new BarChart('#chart', {
     labels: ['Q1', 'Q2', 'Q3', 'Q4'],
     datasets: [{
       label: 'Sales',
       data: [100, 150, 200, 180],
       barColor: '#3498db'
     }]
   }, {
     orientation: 'vertical', // or 'horizontal'
     showValues: true
   });

**LineChart Area Fill**

New area fill feature for LineCharts:

.. code-block:: typescript

   // New in v1.0.5: Area fill support
   const lineChart = new LineChart('#chart', data, {
     showArea: true,        // Enable area fill
     useScribbleFill: true, // Use artistic fill patterns
     fillStyle: 'directional' // or 'oilpaint'
   });

Migrating from JavaScript Library to TypeScript
------------------------------------------------

**Before (Original JavaScript)**

.. code-block:: javascript

   // Old JavaScript library usage
   HandwrittenGraph.createGraph('#chart', {
     xLabel: 'Months',
     yLabel: 'Sales',
     data: [
       { x: 'Jan', y: 65 },
       { x: 'Feb', y: 59 },
       { x: 'Mar', y: 80 }
     ]
   });

**After (TypeScript Rewrite)**

.. code-block:: typescript

   // New TypeScript library usage
   import { LineChart } from 'handwritten-graph';

   const chart = new LineChart('#chart', {
     labels: ['Jan', 'Feb', 'Mar'],
     datasets: [{
       label: 'Sales',
       data: [65, 59, 80],
       lineColor: '#3498db'
     }]
   });

**Key Changes**

1. **Data Structure**: Changed from array of {x, y} objects to separate labels and datasets arrays
2. **Import Style**: Now uses ES6 imports instead of global object
3. **Class-Based**: Charts are now instantiated as classes
4. **Configuration**: More structured configuration object
5. **TypeScript**: Full type safety and IntelliSense support

Breaking Changes
================

v1.0.0 Breaking Changes
-----------------------

**Data Format Changes**

.. code-block:: typescript

   // ❌ Old format (not supported)
   const oldData = [
     { x: 'Jan', y: 10 },
     { x: 'Feb', y: 20 }
   ];

   // ✅ New format
   const newData = {
     labels: ['Jan', 'Feb'],
     datasets: [{
       label: 'Series 1',
       data: [10, 20]
     }]
   };

**API Changes**

.. code-block:: typescript

   // ❌ Old API (not supported)
   HandwrittenGraph.createGraph('#chart', data, options);

   // ✅ New API
   const chart = new LineChart('#chart', data, options);

**Configuration Changes**

.. code-block:: typescript

   // ❌ Old configuration
   const oldOptions = {
     xLabel: 'Time',
     yLabel: 'Value',
     showDots: true,
     dotRadius: 5
   };

   // ✅ New configuration
   const newOptions = {
     pointRadius: 5,
     // Axis labels are automatically generated from data
     // or can be customized through margin and CSS
   };

Deprecation Notices
===================

**Factory Functions**

While factory functions are still supported for backward compatibility, the class-based approach is recommended:

.. code-block:: typescript

   // ⚠️ Deprecated (but still works)
   const cleanup = createGraph('#chart', data);

   // ✅ Recommended
   const chart = new LineChart('#chart', data);
   // ... later
   chart.destroy();

**Global Object Usage**

When using CDN, the global object approach is maintained but class usage is preferred:

.. code-block:: javascript

   // ⚠️ Still supported but consider using classes
   HandwrittenGraph.createGraph('#chart', data);

   // ✅ Preferred even with CDN
   new HandwrittenGraph.LineChart('#chart', data);

Upgrade Paths
=============

Minor Version Updates (1.0.x)
-----------------------------

Minor updates are backward compatible. Simply update your package:

.. code-block:: bash

   npm update handwritten-graph

Major Version Updates (Future)
------------------------------

For future major version updates, check this changelog for breaking changes and follow the migration guide.

Version Support Policy
======================

- **Current Version (1.0.5)**: Full support with new features and bug fixes
- **Previous Minor (1.0.4)**: Security fixes only
- **Older Versions**: Not supported - please upgrade

Browser Compatibility Timeline
==============================

.. list-table::
   :header-rows: 1

   * - Version
     - Chrome
     - Firefox
     - Safari
     - Edge
   * - 1.0.5
     - 90+
     - 88+
     - 14+
     - 90+
   * - 1.0.0-1.0.4
     - 85+
     - 85+
     - 13+
     - 85+

Node.js Support Timeline
========================

.. list-table::
   :header-rows: 1

   * - Version
     - Node.js
     - TypeScript
     - D3.js
   * - 1.0.5
     - 16.0.0+
     - 4.5+
     - 7.0.0+
   * - 1.0.0-1.0.4
     - 14.0.0+
     - 4.0+
     - 7.0.0+

Security Updates
================

No security vulnerabilities have been reported for this library. We follow responsible disclosure practices and will promptly address any security issues.

Contributing to Changelog
=========================

When contributing to the project, please:

1. **Add entries** to the "Unreleased" section at the top
2. **Follow the format**: Use the established categories (Added, Changed, Deprecated, Removed, Fixed, Security)
3. **Be descriptive**: Include enough detail for users to understand the impact
4. **Reference issues**: Link to relevant GitHub issues or pull requests

Example entry format:

.. code-block:: rst

   **Added**

   - New feature description with usage example (#123)

   **Fixed**

   - Bug fix description and impact (#456)

See Also
--------

- :doc:`installation` - Installation and setup guide
- `GitHub Releases <https://github.com/Lilanga/handwritten-graph-ts/releases>`_ - Full release notes