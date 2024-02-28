# Citation Metrics
## Introduction

The goal of this project is to build citation metrics for an astronomer (or a group of astronomers) using data from the [adsabs](https://ui.adsabs.harvard.edu/) website in SQL format. 

In this project we use the adsabs APIs designed to load the data that required to build SQL tables and subsequent queries. We follow the instructions from [Dmitry Savransky's notes](https://gist.github.com/dsavransky). 

In the notebook ```biblio_JBB.ipynb``` we use the adsabs API to request for the bibliographic information from all the articles where `'Jorge Barrera-Ballesteros'` is the (co-)author. The `request.get` function returns, among others a json file where the metadata of the articles is retrived. In this case we obatin the information of 122 articles. We note that the number of entries (i.e., articles) vary depending on the string used for the name. For example using the string `'Jorge Barrera'` yields a total of 1602 entries.  
