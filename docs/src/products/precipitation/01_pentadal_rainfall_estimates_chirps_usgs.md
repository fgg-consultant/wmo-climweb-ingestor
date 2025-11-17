---
outline: deep
---

# Pentadal Rainfall Estimates - CHIRPS (USGS)

## Dataset

| **Input**                               |              **Value**               |
| --------------------------------------- | :----------------------------------: |
| **Title**                               | Pentadal Rainfall Estimates - CHIRPS |
| **Category**                            |            Precipitation             |
| **Subcategory**                         |             Observations             |
| **Layer Type**                          |     Web Map Service – WMS Layer      |
| **Summary**                             |     CHIRPS, updated every 5 days     |
| **Published**                           |                  ✅                  |
| **Public**                              |                  ✅                  |
| **Initially Visible on Map by default** |                  ❌                  |
| **Multi-temporal**                      |                  ✅                  |
| **Multi-layer**                         |                  ❌                  |
| **Near realtime**                       |                  ❌                  |
| **Current time method**                 |  Latest available date from source   |
| **Enable Clipping by shape**            |                  ❌                  |

## Layer

| **Input**                                |                  **Value**                  |
| ---------------------------------------- | :-----------------------------------------: |
| **Dataset**                              | Pentadal Rainfall Estimates - CHIRPS (USGS) |
| **Title**                                |    Pentadal Rainfall Estimates - CHIRPS     |
| **Default**                              |                     ✅                      |
| **Display Format for DateTime Selector** |                  Pentadal                   |

## WMS GetMap Configuration

| **Input**                    |                                             **Value**                                              |
| ---------------------------- | :------------------------------------------------------------------------------------------------: |
| **Base url for WMS**         | https://dmsdata.cr.usgs.gov/geoserver/fews_chirps_global_pentad_data/chirps_global_pentad_data/wms |
| **WMS Version**              |                                               1.3.0                                                |
| **Pixel Width**              |                                                256                                                 |
| **Pixel Height**             |                                                256                                                 |
| **Transparency**             |                                                 ✅                                                 |
| **Spatial Reference System** |                                             EPSG:3857                                              |

## WMS Request Layers

| **Input**                             |                **Value**                |
| ------------------------------------- | :-------------------------------------: |
| **WMS Request Layer 1 Name**          |        chirps_global_pentad_data        |
| **WMS Request Styles**                | fews_chirps_pentad_data_raster_ngviewer |
| **WMS Request Additional Parameters** |  jsonLayerId: africaChirpsPentadalData  |

## More Info

- [Source URL](https://earlywarning.usgs.gov/fews/mapservices)
