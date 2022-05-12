<br/>
<div align="center">
  <h1 align="center">Spam Classifier - From Scratch to Deploy</h1>
</div>



<!-- TABLE OF CONTENTS -->
<details>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The main goal of this project is to build a spam classifier with Naive Bayes Classifier and put it into a container.

We are going to:
* Create a Naive Bayes Classifier
* Create a simple Flask application
* Create a Docker container to run our classifier


### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python](https://nextjs.org/)
* [Sklearn](https://nextjs.org/)
* [Flask](https://nextjs.org/)
* [Pandas](https://nextjs.org/)
* [Numpy](https://nextjs.org/)
* [Pickle](https://nextjs.org/)
* [Docker](https://nextjs.org/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The first step is create a virtual environment
```sh
  virtualenv venv
  ```
  
### Prerequisites
There are two ways to install the project:
* Running a container 
* Installing the dependencies

#### Running a container
To run it with Docker just build the Dockerfile as follows:
```
  docker build -t "name of your image" .
  ```
And then, run:
```
  docker run -i -d -p 5000:5000 "name of your image"
  ```
  
#### Running a container
If you want to run it locally instead, do the following:
```
  git clone https://github.com/nicholascomuni/Spam-Classifier
  cd Spam-Classifier
  pip install -r requirements.txt
  ```
  
Run the flask application:
  ```
  flask run --host 0.0.0.0
  ```

