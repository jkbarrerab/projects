# Citation Metrics
## Introduction

The goal of this project is to build citation metrics for an astronomer (or a group of astronomers) using data from the [adsabs](https://ui.adsabs.harvard.edu/) website in SQL format. 

In this project we use the adsabs APIs designed to load the data that required to build SQL tables and subsequent queries. We follow the instructions from [Dmitry Savransky's notes](https://gist.github.com/dsavransky). 

In the notebook ```biblio_JBB.ipynb``` we use the ads API to request for the bibliographic information from all the articles where `'Jorge Barrera-Ballesteros'` is the (co-)author. We note that this 
