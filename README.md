<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://i.ibb.co/njkqjW7/17984.png" alt="Logo" width="180" height="80">
  </a>

  <h3 align="center">Shopium Reviews Sentiment Analysis</h3>

  <p align="center">
    The Following is a general presentaion of our project 
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>

<div>
<br />
<br />
<br />
</div>

<!-- TABLE OF CONTENTS -->
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>


<a name="about-the-project"></a>
<!-- ABOUT THE PROJECT -->
## About The Project

* Shopium Reviews Sentiment Analysis is a python API developped for [Shopium][shopium-url] for a more accurate recommendation system.


* This module is being developped based [Vader][shopium-url] using **Python** to perform an opinion mining concerning certain offers.


* This project was designed to run on  **Shopium**'s fake database generated by [Shopium Faker][Next-url]


* This project was developed to support **Shopium**'s [Shopium Customer Behavior Prediction][Next-url] project to obtain solid recommendations

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<a name="built-with"></a>
### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
<br />
<br />
* [Vader][Next-url]
* [Flask][Next-url]
* [MongoDB][Vue-url]





<p align="right">(<a href="#readme-top">back to top</a>)</p>


<a name="getting-started"></a>
<!-- GETTING STARTED -->
## Getting Started

* This project was designed to analyze each review made on a certain offer to calculate a sentiment polarity score (positive,negative,neutral).


* A general polarity scores is assigned to each offer by calculating the average of scores on different reviews.



<a name="installation"></a>
### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/firas122/SentimentAnalysis 
   ```

2. Install **pip** packages
   ```sh
   pip install -r requirements.txt
   ```

3. Run the API using command above :
   ```js
   python /project_directory_path/sentiment analysis/api.py
   ```
   

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<br />

<a name="usage"></a>
## Usage
<br />

* Terminal output will include an url by default **127.0.0.1** (localhost) running on port **3000** using the path **/analyze**


* Send a `POST` request to that url with two variables ``DB_url`` which contains the url to your mongo database and `offer_id` that represents the offer we want to analyze it's reviews .



* And the returning JSON Object should include an array contains reviews made on offer with each one scores and an average score for the whole offer:
<br /><br />

  
<!-- CONTACT -->
<a name="contact"></a>
## Contact

Shopium - [@Shopium](https://twitter.com/Shopium) - shopium.local@gmail.com

Project Link: [https://github.com/firas122/SentimentAnalysis](https://github.com/firas122)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-url]: https://linkedin.com/in/othneildrew
[Next-url]: https://github.com/firas122/ShopiumFake/tree/master
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://github.com/firas122/ShopiumFake/tree/master 
[shopium-url]: https://www.shopium.tn/
