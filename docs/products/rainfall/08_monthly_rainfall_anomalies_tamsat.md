---
outline: deep
---

# Monthly Rainfall Anomalies - TAMSAT

## Dataset

| **Input**                               |                  **Value**                   |
| --------------------------------------- | :------------------------------------------: |
| **Title**                               |     Monthly Rainfall Anomalies - TAMSAT      |
| **Category**                            |                   Rainfall                   |
| **Subcategory**                         |                 Observation                  |
| **Layer Type**                          |         Web Map Service – WMS Layer          |
| **Summary**                             | TAMSAT, from 1983 to recent, updated monthly |
| **Published**                           |                      ✅                      |
| **Public**                              |                      ✅                      |
| **Initially Visible on Map by default** |                      ❌                      |
| **Multi-temporal**                      |                      ✅                      |
| **Multi-layer**                         |                      ❌                      |
| **Near realtime**                       |                      ❌                      |
| **Current time method**                 |      Latest available date from source       |
| **Enable Clipping by shape**            |                      ❌                      |

## Layer

| **Input**                                |              **Value**              |
| ---------------------------------------- | :---------------------------------: |
| **Dataset**                              | Monthly Rainfall Anomalies - TAMSAT |
| **Title**                                | Monthly Rainfall Anomalies - TAMSAT |
| **Default**                              |                 ✅                  |
| **Display Format for DateTime Selector** |             Month name              |

## WMS GetMap Configuration

| **Input**                    |                    **Value**                    |
| ---------------------------- | :---------------------------------------------: |
| **Base url for WMS**         | http://20.56.94.119/gsky/ows/rainfall-estimates |
| **WMS Version**              |                      1.3.0                      |
| **Pixel Width**              |                       256                       |
| **Pixel Height**             |                       256                       |
| **Transparency**             |                       ✅                        |
| **Spatial Reference System** |                    EPSG:3857                    |
| **Output Format**            |                       PNG                       |

## WMS Request Layers

| **Input**                    |              **Value**              |
| ---------------------------- | :---------------------------------: |
| **WMS Request Layer 1 Name** | tamsat_monthly_rainfall_anomaly_rfe |

## More Info

- [Learn More](https://research.reading.ac.uk/tamsat): TAMSAT produces daily rainfall estimates for all of Africa at different resolutions.
