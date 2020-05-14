---
title: "Supervised Learning: Donor Classification"
last_modified_at: 2020-05-13T21:50:02-04:00
categories:
  - Project
tags:
  - Machine Learning
  - Python
---
# Summary:
In this project, I help CharityML maximize the likelihood of receiving donations through constructing a model that predicts if a person receives income exceeding 50k/yr; a level known to indicate being a good candidate for donations.

* [Full writeup with code](https://quantchris.com/assets/ml/sup_charity/class_code.html)
* [Full writeup without code](https://quantchris.com/assets/ml/sup_charity/class_no_code.html)
* [Slides without code](https://quantchris.com/assets/ml/sup_charity/class_slides.html)

## Project Organization
1. Exploratory Data Analysis
2. Data Engineering
3. Metrics
4. Machine Learning Models
5. Summary

## Models
* Naive Bayes
* Logistic Regression
* Random Forest
* AdaBoost
* **Gradient Boost**
* Extreme Gradient Boost
* K-Nearest Neighbors

### Performance
* Accuracy: 87.26%
* F-0.5 Score: 76.05% (high precision model)

## Technologies
`Python` inside of an `IPython Notebook` and published with `Reveal.js`<br>
Employed libraries:
* [Pandas](https://pandas.pydata.org/docs/#)`==1.0.1`
* [Numpy](https://numpy.org/doc/1.18/)`==1.18.1`
* [Scikit-learn](https://scikit-learn.org/stable/)`==0.22.1`
* [Scipy](https://docs.scipy.org/doc/scipy/reference/index.html)`==1.4.1`
* [Statsmodels](https://www.statsmodels.org/stable/index.html)`==0.11.0`
* [Plotly](https://plotly.com/python/)`==4.6.0`
* [Seaborn](https://seaborn.pydata.org)`==0.10.0`
* [Matplotlib](https://matplotlib.org/3.2.1/contents.html)`==3.1.3`
* [dython](http://shakedzy.xyz/dython/)`==0.5.0.post2`
* [Custom Module: visualization.py](https://quantchris.com/assets/ml/sup_charity/visualization.py)
* [Custom Module: modeling.py](https://quantchris.com/assets/ml/sup_charity/modeling.py)
* [Custom Module: visuals.py](https://quantchris.com/assets/ml/sup_charity/visuals.py)
