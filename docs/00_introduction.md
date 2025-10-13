---
outline: deep
---

# 🌍 Climweb Portal Product Configuration

This document describes the configuration of product data sources used in the **Climweb MapViewer**.

# Climweb Portal — MapViewer Data Sources (English fields)

**Source:** Data Sources List.pdf fileciteturn0file0

## Web Map Service Datasets

### 1. Natural Colour Enhanced RGB

**Dataset**

- **Title:** Natural Color Enhanced RGB
- **Category:** Satellite
- **Subcategory:** Near Realtime
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** EUMETSAT, Updated every 15 minutes
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Check
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Check
  - **Current time method:** Latest available date from source
  - **Auto Update interval in minutes:** 15
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Natural Color Enhanced RGB
- **Title:** Natural Color Enhanced RGB
- **Default:** Check
- **Display Format for DateTime Selector:** Hour minute:second - (E.g 2023-01-01 00:00)

**WMS GetMap Configuration**

- **Base url for WMS:** https://view.eumetsat.int/geoserver/wms
- **WMS Version:** 1.3.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857
- **Output Format:** PNG

**WMS Request Layers**

- **WMS Request Layer 1 Name:** msg_fes:rgb_naturalenhncd
- **WMS Request Styles:**
- **WMS Request Additional Parameters:**
- **WMS Query Params with Selectable Options:**

**WMS GetCapabilities Configuration**

- **Request Time from capabilities:** Check
- **Get Capabilities URL:** https://view.eumetsat.int/geoserver/msg_fes/rgb_naturalenhncd/ows
- **Get Capabilities Layer Name:** rgb_naturalenhncd
- **Arrange Param Selectors side by Side:** Uncheck

**Legend:**

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://data.eumetsat.int/product/EO:EUM:DAT:MSG:NCL_ENH
- **Short description text:** The Natural Colour Enhanced product is an RGB which utilises three SEVIRI solar channels: NIR1.6, VIS0.8 and VIS0.6.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

### 2. Dust RGB

**Dataset**

- **Title:** Dust RGB
- **Category:** Environment
- **Subcategory:** Dust - Environment
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** EUMETSAT, Updated every 15 minutes
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Check
  - **Current time method:** Latest available date from source
  - **Auto Update interval in minutes:** 15
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Dust RGB
- **Title:** Dust RGB
- **Default:** Check
- **Display Format for DateTime Selector:** Hour minute:second - (E.g 2023-01-01 00:00)

**WMS GetMap Configuration**

- **Base url for WMS:** https://view.eumetsat.int/geoserver/wms
- **WMS Version:** 1.3.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857
- **Output Format:** PNG

**WMS Request Layers**

- **WMS Request Layer 1 Name:** msg_fes:rgb_dust
- **WMS Request Styles:**
- **WMS Request Additional Parameters:**
- **WMS Query Params with Selectable Options:**

**WMS GetCapabilities Configuration**

- **Request Time from capabilities:** Check
- **Get Capabilities URL:** https://view.eumetsat.int/geoserver/msg_fes/rgb_dust/ows
- **Get Capabilities Layer Name:** rgb_dust
- **Arrange Param Selectors side by Side:** Uncheck

**Legend:**

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://data.eumetsat.int/product/EO:EUM:DAT:MSG:DUST
- **Short description text:** The Dust product is an RGB (Red, Green, Blue) composite based upon infrared channel data from the Meteosat Second Generation satellite.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

### 3. Precipitation Rate at Ground

**Dataset**

- **Title:** Precipitation Rate at Ground
- **Category:** Satellite
- **Subcategory:** Near Realtime
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** EUMETSAT, Updated every 15 minutes
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Check
  - **Current time method:** Latest available date from source
  - **Auto Update interval in minutes:** 15
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Precipitation Rate at Ground
- **Title:** Precipitation Rate at Ground
- **Default:** Check
- **Display Format for DateTime Selector:** Hour minute:second - (E.g 2023-01-01 00:00)

**WMS GetMap Configuration**

- **Base url for WMS:** https://view.eumetsat.int/geoserver/wms
- **WMS Version:** 1.3.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857
- **Output Format:** PNG

**WMS Request Layers**

- **WMS Request Layer 1 Name:** msg_fes:h60b
- **WMS Request Styles:**
- **WMS Request Additional Parameters:**
- **WMS Query Params with Selectable Options:**

**WMS GetCapabilities Configuration**

- **Request Time from capabilities:** Check
- **Get Capabilities URL:** https://view.eumetsat.int/geoserver/msg_fes/h60b/ows
- **Get Capabilities Layer Name:** h60b
- **Arrange Param Selectors side by Side:** Uncheck

**Legend:** Custom Image (see PDF for image link)

- **Image download link:** https://wmoomm-my.sharepoint.com/:i:/g/personal/gochieng_wmo_int/EZ3vsTsrTeJEoWkeJhoov60B0lHMpa6NuVGJH7Yht-N04g?e=GfDChw

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://data.eumetsat.int/product/EO:EUM:DAT:0620
- **Short description text:** Instantaneous precipitation maps generated combining geostationary (GEO) IR images from operational geostationary satellites.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

### 4. Rapidly Developing Thunderstorms

**Dataset**

- **Title:** Rapidly Developing Thunderstorms
- **Category:** Satellite
- **Subcategory:** Near Realtime
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** EUMETSAT, Updated every 15 minutes
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Check
  - **Current time method:** Latest available date from source
  - **Auto Update interval in minutes:** 15
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Rapidly Developing Thunderstorms
- **Title:** Rapidly Developing Thunderstorms
- **Default:** Check
- **Display Format for DateTime Selector:** Hour minute:second - (E.g 2023-01-01 00:00)

**WMS GetMap Configuration**

- **Base url for WMS:** https://view.eumetsat.int/geoserver/wms
- **WMS Version:** 1.3.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857
- **Output Format:** PNG

**WMS Request Layers**

- **WMS Request Layer 1 Name:** msg_fes:rdt
- **WMS Request Styles:**
- **WMS Request Additional Parameters:**
- **WMS Query Params with Selectable Options:**

**WMS GetCapabilities Configuration**

- **Request Time from capabilities:** Check
- **Get Capabilities URL:** https://view.eumetsat.int/geoserver/msg_fes/rdt/ows
- **Get Capabilities Layer Name:** rdt
- **Arrange Param Selectors side by Side:** Uncheck

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://data.eumetsat.int/product/EO:EUM:DAT:0023
- **Short description text:** Rapidly Developing Thunderstorms is a geostationary meteorological product for nowcasting applications. Using mainly MSG satellite data, it provides information on clouds related to significant convective systems.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

### 5. Infrared Imagery

**Dataset**

- **Title:** Infrared Imagery
- **Category:** Satellite
- **Subcategory:** Near Realtime
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** EUMETSAT, Updated every 15 minutes
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Check
  - **Current time method:** Latest available date from source
  - **Auto Update interval in minutes:** 15
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Infrared Imagery
- **Title:** Infrared Imagery
- **Default:** Check
- **Display Format for DateTime Selector:** Hour minute:second - (E.g 2023-01-01 00:00)

**WMS GetMap Configuration**

- **Base url for WMS:** https://view.eumetsat.int/geoserver/wms
- **WMS Version:** 1.3.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857
- **Output Format:** PNG

**WMS Request Layers**

- **WMS Request Layer 1 Name:** msg_fes:ir108
- **WMS Request Styles:**
- **WMS Request Additional Parameters:**
- **WMS Query Params with Selectable Options:**

**WMS GetCapabilities Configuration**

- **Request Time from capabilities:** Check
- **Get Capabilities URL:** https://view.eumetsat.int/geoserver/msg_fes/ir108/ows
- **Get Capabilities Layer Name:** ir108
- **Arrange Param Selectors side by Side:** Uncheck

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://data.eumetsat.int/product/EO:EUM:DAT:0156
- **Short description text:** Rectified (level 1.5) Meteosat SEVIRI image data. The data is transmitted as High Rate transmissions in 12 spectral channels.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

### 6. Active Fire Monitoring

**Dataset**

- **Title:** Active Fire Monitoring
- **Category:** Satellite
- **Subcategory:** Near Realtime
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** EUMETSAT, Updated every 15 minutes
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Check
  - **Near realtime:** (blank)
  - **Current time method:** Latest available date from source
  - **Auto Update interval in minutes:** 15
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Active Fire Monitoring
- **Title:** Active Fire Monitoring
- **Default:** Check
- **Display Format for DateTime Selector:** Hour minute:second - (E.g 2023-01-01 00:00)

**WMS GetMap Configuration**

- **Base url for WMS:** https://view.eumetsat.int/geoserver/wms
- **WMS Version:** 1.3.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857
- **Output Format:** PNG

**WMS Request Layers**

- **WMS Request Layer 1 Name:** msg_fes:fire
- **WMS Request Styles:**
- **WMS Request Additional Parameters:**
- **WMS Query Params with Selectable Options:**

**WMS GetCapabilities Configuration**

- **Request Time from capabilities:** Check
- **Get Capabilities URL:** https://view.eumetsat.int/geoserver/msg_fes/fire/ows
- **Get Capabilities Layer Name:** fire
- **Arrange Param Selectors side by Side:** Uncheck

**Legend:** Custom Image (see PDF)
**Image download link:** (present in PDF)

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://data.eumetsat.int/product/EO:EUM:DAT:MSG:FIR
- **Short description text:** The active fire monitoring product is a fire detection product indicating the presence of fire within a pixel.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

### 7. Pentadal Rainfall Estimates - CHIRPS

**Dataset**

- **Title:** Pentadal Rainfall Estimates - CHIRPS
- **Category:** Rainfall
- **Subcategory:** Observation
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** CHIRPS, from 1981 to recent, updated every 5 days
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Uncheck
  - **Current time method:** Latest available date from source
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Pentadal Rainfall Estimates - CHIRPS
- **Title:** Pentadal Rainfall Estimates - CHIRPS
- **Default:** Check
- **Display Format for DateTime Selector:** Pentadal

**WMS GetMap Configuration**

- **Base url for WMS:** http://20.56.94.119/gsky/ows/rainfall-estimates
- **WMS Version:** 1.3.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857
- **Output Format:** PNG

**WMS Request Layers**

- **WMS Request Layer 1 Name:** pentadal_chirps_rainfall_estimate
- **WMS Request Styles:**
- **WMS Request Additional Parameters:**
- **WMS Query Params with Selectable Options:**

**WMS GetCapabilities Configuration**

- **Request Time from capabilities:** Check
- **Get Capabilities URL:** (see PDF)
- **Get Capabilities Layer Name:** (see PDF)
- **Arrange Param Selectors side by Side:** Uncheck

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://www.chc.ucsb.edu/data/chirps
- **Short description text:** CHIRPS was created in collaboration with scientists at the USGS Earth Resources Observation and Science (EROS) Center in order to deliver complete, reliable, up-to-date data sets for a number of early warning objectives, like trend analysis and seasonal drought monitoring.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

### 8. Pentadal Rainfall Anomalies - CHIRPS

**Dataset**

- **Title:** Pentadal Rainfall Anomalies - CHIRPS
- **Category:** Rainfall
- **Subcategory:** Observation
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** CHIRPS, from 1981 to recent, updated every 5 days
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Uncheck
  - **Current time method:** Latest available date from source
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Pentadal Rainfall Anomalies - CHIRPS
- **Title:** Pentadal Rainfall Anomalies - CHIRPS
- **Default:** Check
- **Display Format for DateTime Selector:** Pentadal

**WMS GetMap Configuration**

- **Base url for WMS:** http://20.56.94.119/gsky/ows/rainfall-estimates
- **WMS Version:** 1.3.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857

**WMS Request Layers**

- **WMS Request Layer 1 Name:** pentadal_chirps_rainfall_anomaly
- **WMS Request Styles:**
- **WMS Request Additional Parameters:**
- **WMS Query Params with Selectable Options:**

**WMS GetCapabilities Configuration**

- **Request Time from capabilities:** Check
- **Get Capabilities URL:** (see PDF)
- **Get Capabilities Layer Name:** (see PDF)
- **Arrange Param Selectors side by Side:** Uncheck

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://www.chc.ucsb.edu/data/chirps
- **Short description text:** CHIRPS was created in collaboration with scientists at the USGS Earth Resources Observation and Science (EROS) Center in order to deliver complete, reliable, up-to-date data sets for a number of early warning objectives.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

### 9. Monthly Rainfall Estimates - CHIRPS

**Dataset**

- **Title:** Monthly Rainfall Estimates - CHIRPS
- **Category:** Rainfall
- **Subcategory:** Observation
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** CHIRPS, from 1981 to recent, updated monthly
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Uncheck
  - **Current time method:** Latest available date from source
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Monthly Rainfall Estimates - CHIRPS
- **Title:** Monthly Rainfall Estimates - CHIRPS
- **Default:** Check
- **Display Format for DateTime Selector:** Month name

**WMS GetMap Configuration**

- **Base url for WMS:** http://20.56.94.119/gsky/ows/rainfall-estimates
- **WMS Version:** 1.3.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857

**WMS Request Layers**

- **WMS Request Layer 1 Name:** monthly_chirps_rainfall_estimate
- **WMS Request Styles:**
- **WMS Request Additional Parameters:**

**WMS GetCapabilities Configuration**

- **Request Time from capabilities:** Check
- **Get Capabilities URL:** (see PDF)
- **Get Capabilities Layer Name:** (see PDF)
- **Arrange Param Selectors side by Side:** Uncheck

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://www.chc.ucsb.edu/data/chirps
- **Short description text:** CHIRPS was created in collaboration with scientists at the USGS EROS Center to provide data for early warning objectives.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

### 10. Monthly Rainfall Anomalies - CHIRPS

**Dataset**

- **Title:** Monthly Rainfall Anomalies - CHIRPS
- **Category:** Rainfall
- **Subcategory:** Observation
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** CHIRPS, from 1981 to recent, updated monthly
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Uncheck
  - **Current time method:** Latest available date from source
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Monthly Rainfall Anomalies - CHIRPS
- **Title:** Monthly Rainfall Anomalies - CHIRPS
- **Default:** Check
- **Display Format for DateTime Selector:** Month name

**WMS GetMap Configuration**

- **Base url for WMS:** http://20.56.94.119/gsky/ows/rainfall-estimates
- **WMS Version:** 1.3.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857

**WMS Request Layers**

- **WMS Request Layer 1 Name:** monthly_chirps_rainfall_anomaly
- **WMS Request Styles:**
- **WMS Request Additional Parameters:**

**WMS GetCapabilities Configuration**

- **Request Time from capabilities:** Check
- **Get Capabilities URL:** (see PDF)
- **Get Capabilities Layer Name:** (see PDF)
- **Arrange Param Selectors side by Side:** Uncheck

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://www.chc.ucsb.edu/data/chirps
- **Short description text:** CHIRPS was created in collaboration with scientists at the USGS EROS Center.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

### 11. Pentadal Rainfall Estimates - TAMSAT

**Dataset**

- **Title:** Pentadal Rainfall Estimates - TAMSAT
- **Category:** Rainfall
- **Subcategory:** Observation
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** TAMSAT, from 1983 to recent, updated every 5 days
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Uncheck
  - **Current time method:** Latest available date from source
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Pentadal Rainfall Estimates - TAMSAT
- **Title:** Pentadal Rainfall Estimates - TAMSAT
- **Default:** Check
- **Display Format for DateTime Selector:** Pentadal

**WMS GetMap Configuration**

- **Base url for WMS:** http://20.56.94.119/gsky/ows/rainfall-estimates
- **WMS Version:** 1.3.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857

**WMS Request Layers**

- **WMS Request Layer 1 Name:** tamsat_pentadal_rainfall_estimate_rfe
- **WMS Request Styles:**
- **WMS Request Additional Parameters:**

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://research.reading.ac.uk/tamsat
- **Short description text:** TAMSAT produces daily rainfall estimates for all of Africa at different resolutions. Applications of the data include famine early warning, drought insurance and agricultural decision support.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

### 12. Pentadal Rainfall Anomalies - TAMSAT

**Dataset**

- **Title:** Pentadal Rainfall Anomalies - TAMSAT
- **Category:** Rainfall
- **Subcategory:** Observation
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** TAMSAT, from 1983 to recent, updated every 5 days
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Uncheck
  - **Current time method:** Latest available date from source
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Pentadal Rainfall Anomalies - TAMSAT
- **Title:** Pentadal Rainfall Anomalies - TAMSAT
- **Default:** Check
- **Display Format for DateTime Selector:** Pentadal

**WMS GetMap Configuration**

- **Base url for WMS:** http://20.56.94.119/gsky/ows/rainfall-estimates
- **WMS Version:** 1.3.0
- **Pixel Width:** 256
- **Pixel Height:** 256

**WMS Request Layers**

- **WMS Request Layer 1 Name:** tamsat_pentadal_rainfall_anomaly_rfe
- **WMS Request Styles:**
- **WMS Request Additional Parameters:**

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://research.reading.ac.uk/tamsat
- **Short description text:** TAMSAT produces daily rainfall estimates for all of Africa at different resolutions.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

### 13. Monthly Rainfall Estimates - TAMSAT

**Dataset**

- **Title:** Monthly Rainfall Estimates - TAMSAT
- **Category:** Rainfall
- **Subcategory:** Observation
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** TAMSAT, from 1983 to recent, updated monthly
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Uncheck
  - **Current time method:** Latest available date from source
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Monthly Rainfall Estimates - TAMSAT
- **Title:** Monthly Rainfall Estimates - TAMSAT
- **Default:** Check
- **Display Format for DateTime Selector:** Month name

**WMS GetMap Configuration**

- **Base url for WMS:** http://20.56.94.119/gsky/ows/rainfall-estimates
- **WMS Version:** 1.3.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857

**WMS Request Layers**

- **WMS Request Layer 1 Name:** tamsat_monthly_rainfall_estimate_rfe
- **WMS Request Styles:**
- **WMS Request Additional Parameters:**

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://research.reading.ac.uk/tamsat
- **Short description text:** TAMSAT produces daily rainfall estimates for all of Africa at different resolutions.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

### 14. Monthly Rainfall Anomalies - TAMSAT

**Dataset**

- **Title:** Monthly Rainfall Anomalies - TAMSAT
- **Category:** Rainfall
- **Subcategory:** Observation
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** TAMSAT, from 1983 to recent, updated monthly
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Uncheck
  - **Current time method:** Latest available date from source
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Monthly Rainfall Anomalies - TAMSAT
- **Title:** Monthly Rainfall Anomalies - TAMSAT
- **Default:** Check
- **Display Format for DateTime Selector:** Month name

**WMS GetMap Configuration**

- **Base url for WMS:** http://20.56.94.119/gsky/ows/rainfall-estimates
- **WMS Version:** 1.3.0
- **Pixel Width:** 256
- **Pixel Height:** 256

**WMS Request Layers**

- **WMS Request Layer 1 Name:** tamsat_monthly_rainfall_anomaly_rfe
- **WMS Request Styles:**
- **WMS Request Additional Parameters:**

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://research.reading.ac.uk/tamsat
- **Short description text:** TAMSAT produces daily rainfall estimates for all of Africa.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

### 15. Pentadal Rainfall Estimates - CHIRPS (USGS)

**Dataset**

- **Title:** Pentadal Rainfall Estimates - CHIRPS
- **Category:** Precipitation
- **Subcategory:** Observations
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** CHIRPS, updated every 5 days
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Uncheck
  - **Current time method:** Latest available date from source
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Pentadal Rainfall Estimates - CHIRPS (USGS)
- **Title:** Pentadal Rainfall Estimates - CHIRPS
- **Default:** Check
- **Display Format for DateTime Selector:** Pentadal

**WMS GetMap Configuration**

- **Base url for WMS:** https://dmsdata.cr.usgs.gov/geoserver/fews_chirps_global_pentad_data/chirps_global_pentad_data/wms
- **WMS Version:** 1.3.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857

**WMS Request Layers**

- **WMS Request Layer 1 Name:** chirps_global_pentad_data
- **WMS Request Styles:** fews_chirps_pentad_data_raster_ngviewer
- **WMS Request Additional Parameters:**
  - **Name:** jsonLayerId
  - **Value:** africaChirpsPentadalData

**More Info**

- **Link Text:** Source URL
- **Link URL:** https://earlywarning.usgs.gov/fews/mapservices

---

### 16. Pentadal NDVI

**Dataset**

- **Title:** Normalised Difference Vegetation Index (NDVI) - Pentadal
- **Category:** Environment
- **Subcategory:** Vegetation Indices
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** eVIIRS, updated every 5 days
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Uncheck
  - **Current time method:** Latest available date from source
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Normalised Difference Vegetation Index (NDVI) - Pentadal
- **Title:** Normalised Difference Vegetation Index (NDVI) - Pentadal
- **Default:** Check
- **Display Format for DateTime Selector:** Pentadal

**WMS GetMap Configuration**

- **Base url for WMS:** https://dmsdata.cr.usgs.gov/geoserver/fews_eviirsndvi_africa_pentad_data/eviirsndvi_africa_pentad_data/wms
- **WMS Version:** 1.1.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857

**WMS Request Layers**

- **WMS Request Layer 1 Name:** eviirsndvi_africa_pentad_data

**More Info**

- **Link Text:** Source URL
- **Link URL:** https://earlywarning.usgs.gov/fews/mapservices

---

### 17. Pentadal NDVI Anomaly

**Dataset**

- **Title:** Normalised Difference Vegetation Index (NDVI) Anomaly - Pentadal
- **Category:** Environment
- **Subcategory:** Vegetation Indices
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** eVIIRS, updated every 5 days
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Uncheck
  - **Current time method:** Latest available date from source
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Normalised Difference Vegetation Index (NDVI) Anomaly - Pentadal
- **Title:** Normalised Difference Vegetation Index (NDVI) - Anomaly
- **Default:** Check
- **Display Format for DateTime Selector:** Pentadal

**WMS GetMap Configuration**

- **Base url for WMS:** https://dmsdata.cr.usgs.gov/geoserver/fews_eviirsndvi_africa_pentad_anom/eviirsndvi_africa_pentad_anom/wms
- **WMS Version:** 1.1.0
- **Pixel Width:** 256
- **Pixel Height:** 256

**WMS Request Layers**

- **WMS Request Layer 1 Name:** eviirsndvi_africa_pentad_anom

**More Info**

- **Link Text:** Source URL
- **Link URL:** https://earlywarning.usgs.gov/fews/mapservices

---

### 18. Dust Optical Depth Forecast (550nm)

**Dataset**

- **Title:** Dust Optical Depth Forecast (550nm)
- **Category:** Environment
- **Subcategory:** Dust Forecast
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** Multi-Model, North Africa
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** (blank)
  - **Current time method:** Latest available date from source
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Dust Optical Depth Forecast (550nm)
- **Title:** Dust Optical Depth Forecast (550nm)
- **Default:** Check
- **Display Format for DateTime Selector:** Hour minute:second

**WMS GetMap Configuration**

- **Base url for WMS:** http://20.56.94.119/gsky/ows/dust-forecast
- **WMS Version:** 1.1.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857

**WMS Request Layers**

- **WMS Request Layer 1 Name:** od550_dust
- **WMS Request Styles:**
- **WMS Request Additional Parameters:**

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://dust.aemet.es/products/daily-dust-products
- **Short description text:** Effective depth of the dust-aerosol column from the viewpoint of radiation propagation. It corresponds to the integrated extinction coefficient over a vertical column.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

### 19. Dust Surface Concentration Forecast (µg/m³)

**Dataset**

- **Title:** Dust Surface Concentration Forecast (µg/m³)
- **Category:** Environment
- **Subcategory:** Dust Forecast
- **Layer Type:** Web Map Service – WMS Layer
- **Summary:** Multi-Model, North Africa
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Uncheck
  - **Current time method:** Latest available date from source
  - **Enable Clipping by shape:** Uncheck

**Layer**

- **Dataset:** Dust Surface Concentration Forecast (µg/m³)
- **Title:** Dust Surface Concentration Forecast (µg/m³)
- **Default:** Check
- **Display Format for DateTime Selector:** Hour minute:second

**WMS GetMap Configuration**

- **Base url for WMS:** http://20.56.94.119/gsky/ows/dust-forecast
- **WMS Version:** 1.1.0
- **Pixel Width:** 256
- **Pixel Height:** 256
- **Transparency:** Check
- **Spatial Reference System:** EPSG:3857

**WMS Request Layers**

- **WMS Request Layer 1 Name:** sconc_dust

**More Info**

- **Link Text:** Learn More
- **Link URL:** https://dust.aemet.es/products/daily-dust-products
- **Short description text:** Mass concentration of dust particles in the atmosphere. By default, the dust concentration at surface level is shown.
- **Format link as action button:** Uncheck
- **Show arrow in button:** Uncheck

---

## Dust Warnings for West Africa

**Countries with warning data available:**

- Burkina Faso — BFA
- Senegal — SEN
- Chad — TCD
- Mali — MLI
- Niger — NER
- Cape Verde — CPV
- Mauritania — MRT

### 20. Dust Warning Advisory

**Dataset**

- **Title:** Dust Warning Advisory
- **Category:** Alerts
- **Subcategory:** Dust Warnings
- **Layer Type:** XYZ Vector Tile Layer
- **Summary:** Multi-Model, North Africa
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Uncheck
  - **Current time method:** Earliest available date from source

**Layer**

- **Title:** Dust Warning Advisory
- **Base Tile Url:** http://20.56.94.119/pg4w/tileserv/public.aemet_dust_warnings/{z}/{x}/{y}.pbf
- **Time Settings — Get Time from tile Json Url:** Check
- **Tile JSON Url:** http://20.56.94.119/api/aemet-warnings/available-forecast-dates.json
- **Timestamps response object key:** timestamps
- **Time Parameter Name:** forecast_date
- **Display Format for DateTime Selector:** Day - (E.g 2023-01-01)
- **Static Query Params Key:** iso
- **Value:** See country table above

**Legend**

- **Legend Type:** Basic
- **Value color:**
  - Normal — #008000
  - High — #ffd700
  - Very High — #ff8c00
  - Extremely High — #ff0000

**More Info**

- **Link Text:** More Details
- **Link Url:** https://dust.aemet.es/products
- **Short Description Text:** Dust Warning Advisory System shows categorical qualitative information about the warning levels of sand and dust concentration, from Normal to Extremely High for 3 days for some of the most vulnerable countries in the Sahel region.

**Render / Styling**

- **Use Render Layers Json:** Checked

**Layers Configuration (JSON)**

```
[
  {
    "type": "fill",
    "paint": {
      "fill-color": [
        "match",
        [
          "get",
          "value"
        ],
        0,
        "#008000",
        1,
        "#ffd700",
        2,
        "#ff8c00",
        3,
        "#ff0000",
        "#808080"
      ]
    },
    "source-layer": "default"
  },
  {
    "type": "line",
    "paint": {
      "line-color": "#fff",
      "line-width": 1,
      "line-dasharray": [
        3,
        2
      ]
    },
    "source-layer": "default"
  }
]
```

**Map Popup Configuration**

- **Data Key:** name — **Popup Label:** Region
- **Data Key:** level — **Popup Label:** Level

---

## Exposure / Infrastructure Data Sources

**Table (as in PDF)**

- **Title:** Airports — **Download Link:** (Download Shapefile) — **Format:** Shapefile — **Primary Source:** Our airports (https://ourairports.com/data/)
- **Title:** Power plants — **Download Link:** (Download Shapefile) — **Format:** Shapefile — **Primary Source:** WRI (https://datasets.wri.org/dataset/globalpowerplantdatabase)
- **Title:** Reservoirs — **Download Link:** (Download Shapefile) — **Format:** Shapefile — **Primary Source:** GlobalDamWatch (https://www.globaldamwatch.org/directory)
- **Title:** Dams — **Download Link:** (Download Shapefile) — **Format:** Shapefile — **Primary Source:** GlobalDamWatch (https://www.globaldamwatch.org/directory)
- **Title:** Health Facilities — **Download Link:** (Download Shapefile) — **Format:** Shapefile — **Primary Source:** HealthSites IO (https://healthsites.io/map)
- **Title:** Population Density — **Download Link:** (Download GeoTIFF) — **Format:** GeoTIFF — **Primary Source:** WorldPop Hub (https://hub.worldpop.org/)
- **Title:** Boundaries — **Format:** Shapefile — **Primary Source:** OCHA Humdata / GADM (https://data.humdata.org/, https://gadm.org/download_country.html)

---

### 21. Population Density

**Dataset**

- **Title:** Population Density
- **Category:** Exposure
- **Subcategory:** Population
- **Layer Type:** Raster File – NetCDF/GeoTiff
- **Summary:** WorldPop, UN Adjusted
- **Metadata:**
  - **Published:** Check
  - **Public:** Check
  - **Initially Visible on Map by default:** Uncheck
  - **Multi-temporal:** Check
  - **Multi-layer:** Uncheck
  - **Near realtime:** Uncheck
  - **Current time method:** Latest available date from source
  - **Enable Clipping by shape:** Check

**Layer**

- **Dataset:** Population Density
- **Title:** Population Density
- **Default:** Check
- **Display Format for DateTime Selector:** Year

**Style / Analysis**

- **Use Custom Legend:** Uncheck
- **Auto ingest from directory:** Uncheck
- **Analysis — Point Analysis:** Show data for point — Check; Show timeseries data for point — Check; Data unit — (blank); Chart Type — Bar Chart
- **Analysis — Area Analysis:** Show data for area — Check; Area value type — Sum of pixel values; Data unit — (blank); Show timeseries data for point — Check; Area timeseries aggregation method — By Sum; Chart Type — Bar Chart

---
