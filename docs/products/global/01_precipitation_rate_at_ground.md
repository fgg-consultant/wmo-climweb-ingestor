---
outline: deep
---

# Precipitation Rate at Ground

![WMS Layer](/wms/msg_fes_h60b.png)

## Dataset

| **Input**                               |             **Value**              |
| --------------------------------------- | :--------------------------------: |
| **Title**                               |    Precipitation Rate at Ground    |
| **Category**                            |             Satellite              |
| **Subcategory**                         |           Near Realtime            |
| **Layer Type**                          |    Web Map Service – WMS Layer     |
| **Summary**                             | EUMETSAT, Updated every 15 minutes |
| **Published**                           |                 ✅                 |
| **Public**                              |                 ✅                 |
| **Initially Visible on Map by default** |                 ❌                 |
| **Multi-temporal**                      |                 ✅                 |
| **Multi-layer**                         |                 ❌                 |
| **Near realtime**                       |                 ✅                 |
| **Current time method**                 | Latest available date from source  |
| **Auto Update interval in minutes**     |                 15                 |
| **Enable Clipping by shape**            |                 ❌                 |

## Layer

| **Input**                                |          **Value**           |
| ---------------------------------------- | :--------------------------: |
| **Dataset**                              | Precipitation Rate at Ground |
| **Title**                                | Precipitation Rate at Ground |
| **Default**                              |              ✅              |
| **Display Format for DateTime Selector** |      Hour minute:second      |

## WMS GetMap Configuration

| **Input**                    |                **Value**                |
| ---------------------------- | :-------------------------------------: |
| **Base url for WMS**         | https://view.eumetsat.int/geoserver/wms |
| **WMS Version**              |                  1.3.0                  |
| **Pixel Width**              |                   256                   |
| **Pixel Height**             |                   256                   |
| **Transparency**             |                   ✅                    |
| **Spatial Reference System** |                EPSG:3857                |
| **Output Format**            |                   PNG                   |

## WMS Request Layers

| **Input**                    |  **Value**   |
| ---------------------------- | :----------: |
| **WMS Request Layer 1 Name** | msg_fes:h60b |

## WMS GetCapabilities Configuration

| **Input**                          |                      **Value**                       |
| ---------------------------------- | :--------------------------------------------------: |
| **Request Time from capabilities** |                          ✅                          |
| **Get Capabilities URL**           | https://view.eumetsat.int/geoserver/msg_fes/h60b/ows |
| **Get Capabilities Layer Name**    |                         h60b                         |

## Legend

Custom Image (see PDF for image link)

## More Info

- [Learn More](https://data.eumetsat.int/product/EO:EUM:DAT:0620): Instantaneous precipitation maps generated combining geostationary (GEO) IR images from operational geostationary satellites.
