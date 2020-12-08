# Data Visualiztions
***

## CONTENT

| Project | Dataset | Tags |
| --- | --- | --- |
| [NY Airbnb Flats 2019 with Bokeh](#NY_Airbnb) | Flats for rental in NY (Airbnb) 2019 | <img src="https://img.shields.io/badge/-Interactivity-blue"> <img src="https://img.shields.io/badge/-Python-blue"> <img src="https://img.shields.io/badge/-Bokeh-green"> |

***

<a name="NY_Airbnb"></a>
### NY Airbnb

* This small project consists of an interactive visualization of a data set of flats offered for Airbnb in the city of New York in 2019. A few parameters allow to interact with the dataset and a hover tool is available for obtaining more information of each sample.

* My main goal with this project was to try the library Bokeh and the simplest ways of interacting with data by using just python.

* The data in this case is loaded from a .csv file but it could be easily extended for loading the data from other sources such as a SQL database.

* The inspiration from this project comes from [example](https://docs.bokeh.org/en/latest/docs/gallery.html) and the code can be found [here](https://github.com/bokeh/bokeh/tree/branch-2.3/examples/app/movies).

#### Instructions:

* I have been using a python virtual environment  but other systems as Docker can be used too. A '''requirements.txt''' file with the dependencies can be found on the corresponding folder. In order to create the virtual environment and install the libraries the next steps can be follow:
```
python -m venv .venv
```
```
pip install -r requirements.txt
```

* To view the app, move to the parent directory and run Bokeh serve:

```
bokeh serve --show movies
```
<p float="center">
  <img src="https://raw.githubusercontent.com/MGijon/Data-Visualizations/master/images/Bokeh_NY_giff.gif?token=AGKYMFZQCFQ4JZLV67XCJ3S72AERG">
</p>

***


<!--
Characteristics
<img src="https://img.shields.io/badge/-Interactivity-blue">
Languages
<img src="https://img.shields.io/badge/-Python-blue">
<img src="https://img.shields.io/badge/-R-green">
<img src="https://img.shields.io/badge/-C-black">
<img src="https://img.shields.io/badge/-C++-grey">
<img src="https://img.shields.io/badge/-Java-red">
<img src="https://img.shields.io/badge/-JavaScipt-yellow">
<img src="https://img.shields.io/badge/-PHP-purple">
Frameworks
<img src="https://img.shields.io/badge/-Bokeh-green">
-->
