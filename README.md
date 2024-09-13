# When do Balance Energy Prices Skyrocket?

Presented at [Energy Data Hackdays 2024](https://hack.energy.opendata.ch/project/124)

Fachhochschule Nordwestschweiz, September 12 - 13, 2024

_The original slides can be found in [CHALLENGE.md](CHALLENGE.md)_

# Results

Working in an open source data science environment, we created several [Jupyter Notebooks](https://jupyter.org) to dive into the challenge of understanding and modelling national energy balancing with Python. In our presentation you can see the key outputs, or browse our notebooks and other sources shared on [GitHub](https://github.com/SFOE-Hackathons/EnergyDataHackdays2024-BalanceEnergyPrices/).

https://github.com/SFOE-Hackathons/EnergyDataHackdays2024-BalanceEnergyPrices/

We started mocking up a basic dashboard using [Marimo](https://marimo.io), which could include the read-outs above as well as a [Timeline of April 22 events](https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=18jdhZQgIdU4FcwuW5Rif82PitmR3abKi2VNdCQOxnnY&font=Default&lang=en&initial_zoom=2&height=650) that we started collecting in a spreadsheet. The goal is better understanding of the subject matter through clear presentation of the data. Our [data sources](#data), as well as further [literature and links](#notes) can be found in the section below.

![Screenshot from 20240913 144310.png](https://bucketeer-036aa605-c047-4623-8610-f1764b90cf98.s3.amazonaws.com/openenergydata/1/VW9PO8PG6F9K7CSG4A799B9A/Screenshot_from_20240913_144310.png)

_Prediction of load levels created with [Chronos forecasting](https://github.com/amazon-science/chronos-forecasting?tab=readme-ov-file), one of the tools we used._

# Data

| Dataset | File | Source |
| ------- | ---- | ------ |
| Day-ahead prices, hourly | auction\_spot\_prices\_switzerland\_2024.csv | EPEX |
| Day-ahead traded volumes, hourly | auction\_spot\_volumes\_switzerland\_2024.csv | EPEX |
| Balancing prices for BGs short/long, 15min | balancing\_prices\_2024.csv | Swissgrid |
| Day-ahead prices, hourly | day\_ahead\_prices\_CH\_2024.csv | ENTSO-E |
| Swiss power generation per type, hourly | generation\_per\_type.csv | ENTSO-E |
| Swiss power generation per type (staging), hourly | generation\_per\_type\_staging.csv | ENTSO-E |
| Yearly calendar of events | kalender\_2024\_ch.csv | - |
| Legend of Meteoschweiz columns | legende meteoschweiz.csv | Meteoschweiz |
| Consumption schedule, hourly | load.csv | ENTSO-E |
| Consumption Schedule (staging), hourly | load\_staging.csv | ENTSO-E |
| Weather data | staging\_ms\_6120.csv | Meteoschweiz |
| Weather data (unprocessed) | staging\_ms\_6121.csv | Meteoschweiz |
| Problems reported in power supply | unavailability\_of\_generation\_units.csv | ENTSO-E |

---

Join our [Data Expedition](https://hack.energy.opendata.ch/project/15) to help efforts to catalog and support open data for projects like this one. Further links can be found in the [Resources](https://hack.energy.opendata.ch/event/2/stages) section of the Hackdays.

# Notes

Since it is not possible for the market participants to have all the information we have, we have to reconstruct the probable situation from the available sources - and if we recognize patterns, find out in which combination the variables become important. To learn about pricing models for power trading, see this [With The Grid blog post](https://withthegrid.com/energy-pricing-epex-day-ahead-and-imbalance-prices/).

Swissgrid has to pay the current balancing price, and there is little to counter speculation and mispredictions. Few understand the background about the schedules and how Swissgrid organizes the grid operation. The [Swissgrid website](https://www.swissgrid.ch/de/home/customers/topics/bgm/balance-energy.html) has various documents that illustrate the matter.

For a brief intro to statistical forecasting with Python, see [SARIMAX at Statsmodels.org](https://www.statsmodels.org/stable/examples/notebooks/generated/statespace_sarimax_faq.html)

We used [Etherpad](https://pad.okfn.de/) (hosted at OKFN DE) to collect notes.

## In the Media

These articles on the events in April were mentioned in the Challenge presentation:

- [NZZ 30.04.2024](https://www.nzz.ch/wirtschaft/fehlprognose-beim-solarstrom-ploetzlich-fehlte-der-schweiz-die-produktion-eines-grossen-kernkraftwerkes-ld.1828058)
- [NZZ 16.05.2024](https://www.nzz.ch/wirtschaft/wie-angespannt-ist-die-lage-am-strommarkt-ld.1697374)
- [Bluewin 30.04.2024](https://www.bluewin.ch/de/news/schweiz/schweiz-drohte-letzte-woche-ploetzlich-ein-strom-blackout-2185652.html)
- [Infosperber 13.05.2024](https://www.infosperber.ch/umwelt/energieproduktion/der-fast-blackout-den-es-nicht-gab/)

## Projects

We found these prior Hackday and other projects inspirational:

- [Visistrom (2019)](https://hack.energy.opendata.ch/project/27)
- [Electricity Maps (2020)](https://hack.energy.opendata.ch/project/67)
- [Trends in tertiary energy prices (2021)](https://hack.energy.opendata.ch/project/86)
- [Experimental Statistics ML_SoSi BFS (2023)](https://www.experimental.bfs.admin.ch/expstat/de/home/projekte/ml-sosi.html)
- [Füllungsgrad der Speicherseen BFE (2024)](https://www.uvek-gis.admin.ch/BFE/storymaps/AP_FuellungsgradSpeicherseen/?lang=de)
- [DataHub - Brent and WTI Spot Prices](https://datahub.io/@Daniellappv/oil-prices-this)
- [UK Energy Dashboard](https://www.energydashboard.co.uk/live) ([Source](https://github.com/1tang/Energy-Dashboard), [Data](https://www.nationalgrideso.com/data-portal))
- [Visualization of the European transmission network with Plotly and the PyPSA-Eur package](https://github.com/zoltanmaric/coppersushi)

## Simulation as Game

Inspired by Koboldgames, who supported [previous Energy Hackdays](https://koboldgames.ch/blog/2021-01-13?lang=eng) and have developed [serious games](https://koboldgames.ch/games) involving environmental and economics models, we researched whether games are being used to simulate and teach power systems.

- [Barrios-O’Neill, Hook](https://www.sciencedirect.com/science/article/pii/S001632871630088X) (2016)
- [Fate of the World](https://store.steampowered.com/app/901776/Fate_of_the_World_Tipping_Point/) (2011)
- [Green with Energy](https://store.steampowered.com/app/890890/Green_With_Energy/) (2024)
- [How video games prepared me for energy modelling](https://www.linkedin.com/pulse/how-video-games-prepared-me-energy-modelling-10-avgerinopoulos/) (LinkedIn)

