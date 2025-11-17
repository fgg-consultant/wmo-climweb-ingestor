---
outline: deep
---

# Dust Warning Advisory

## Dataset

| **Input**                               |              **Value**              |
| --------------------------------------- | :---------------------------------: |
| **Title**                               |        Dust Warning Advisory        |
| **Category**                            |               Alerts                |
| **Subcategory**                         |            Dust Warnings            |
| **Layer Type**                          |        XYZ Vector Tile Layer        |
| **Summary**                             |      Multi-Model, North Africa      |
| **Published**                           |                 ✅                  |
| **Public**                              |                 ✅                  |
| **Initially Visible on Map by default** |                 ❌                  |
| **Multi-temporal**                      |                 ✅                  |
| **Multi-layer**                         |                 ❌                  |
| **Near realtime**                       |                 ❌                  |
| **Current time method**                 | Earliest available date from source |

## Layer

| **Input**                                       |                                  **Value**                                   |
| ----------------------------------------------- | :--------------------------------------------------------------------------: |
| **Title**                                       |                            Dust Warning Advisory                             |
| **Base Tile Url**                               | http://20.56.94.119/pg4w/tileserv/public.aemet_dust_warnings/{z}/{x}/{y}.pbf |
| **Time Settings — Get Time from tile Json Url** |                                      ✅                                      |
| **Tile JSON Url**                               |     http://20.56.94.119/api/aemet-warnings/available-forecast-dates.json     |
| **Timestamps response object key**              |                                  timestamps                                  |
| **Time Parameter Name**                         |                                forecast_date                                 |
| **Display Format for DateTime Selector**        |                                     Day                                      |
| **Static Query Params Key**                     |                                     iso                                      |
| **Value**                                       |                      See country table in introduction                       |

## Legend

| **Value**      | **Color** |
| -------------- | :-------: |
| Normal         |  #008000  |
| High           |  #ffd700  |
| Very High      |  #ff8c00  |
| Extremely High |  #ff0000  |

## More Info

- [More Details](https://dust.aemet.es/products): Dust Warning Advisory System shows categorical qualitative information about the warning levels of sand and dust concentration, from Normal to Extremely High for 3 days for some of the most vulnerable countries in the Sahel region.
