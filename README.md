<h1 align="center">Rio de Janeiro Airbnb Machine Learning Model</h1>
<p align="center">
  <i>This machine learning model utilizes supervised learning to predict the daily rental price for Airbnb properties!</i>
  <br/><br/>
  <img width="130" alt="Mafl" src="https://revistaazul.voeazul.com.br/wp-content/uploads/2023/03/muito-alem-da-praia-saiba-o-que-fazer-no-rio-de-janeiro.jpeg"/>
  <br/><br/>
  <b><a href="https://drive.google.com/drive/folders/1q_4X9UAha5WXrZVSjj4235ktvcQOZNx6?usp=sharing">Download .exe folder</a></b> | <b><a href="https://airbnb-rio-de-janeiro.onrender.com/">Wikipedia</a></b> | <b><a href="https://github.com/Dante-Navaza2005">My profile</a></b> | <b><a href="https://www.linkedin.com/in/dante-navaza/">LinkedIn</a></b>
  <br/><br/>
  <a href="https://github.com/hywax/mafl/blob/main/CHANGELOG.md"><img src="https://img.shields.io/github/package-json/v/hywax/mafl?loo=hackthebox&color=609966&logoColor=fff" alt="Current Version"/></a>
  <a target="_blank" href="https://github.com/hywax/mafl"><img src="https://img.shields.io/github/last-commit/hywax/mafl?logo=github&color=609966&logoColor=fff" alt="Last commit"/></a>
  <a target="_blank" href="https://hub.docker.com/r/hywax/mafl"><img src="https://img.shields.io/docker/pulls/hywax/mafl?logo=docker&color=609966&logoColor=fff" alt="Docker pulls"/></a>
  <a href="https://github.com/hywax/mafl/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-609966?logo=opensourceinitiative&logoColor=fff" alt="License MIT"/></a>
  <br/><br/>
  <img src="image\README\Airbnb-Deployment-Brave-2024-04-23-00-58-16.gif" alt="Mafl" width="100%"/>
</p>

<details>
  <summary><b>Table of Contents</b></summary>

* [Context and objective](#-Context-and-objective)
* [Features](#-features)
* [Getting started](#-Getting-started)
  * [Download](#Download)
  * [Executing the file](#Executing-the-file)
  * [Additional changes](#Additional-changes)
* [Services](#-services)
* [Themes](#-themes)
* [Icons](#-icons)
* [Languages](#-multi-language)
* [Credits](#-credits)
  * [Contributors](#contributors)
* [License](#-license)

</details>

## 🌐 Context and objective

Airbnb allows anyone with a spare room or property of any type (apartment, house, chalet, inn, etc.) to list their property for rent on a daily basis.

As a host, you create your profile and list your property. In this listing, hosts should provide a comprehensive description of the property to assist renters/travelers in choosing the best accommodation and to make their listing more appealing.

There are numerous customizations available in the listing, ranging from minimum stay requirements, pricing, number of rooms, to cancellation policies, extra guest fees, identity verification requirements for renters, etc.

Our objective is to build a price prediction model that enables property owners to determine the appropriate daily rate for their property. Additionally, to assist renters in evaluating whether a listed property offers a competitive price compared to similar properties with similar characteristics.

## 🎯 Features

* 🤖  **Machine Learning** : Employs the Extra Trees algorithm in a supervised learning model for robust property price estimation.
* ⚡  **Real-Time** : Provides instant price predictions as you input data.
* 🌎  **Multi-Language** : Offers documentation and a website in multiple languages for broader accessibility.
* 🗂️  **Customizable** : Allows you to include various property features to refine model accuracy.
* 👌  **Simple Setup** : Get started quickly by downloading an executable folder and a joblib model file.
* 🚀  **High Speed** : Delivers price calculations within seconds. You can further boost performance by adjusting the joblib file's compression level (note: higher compression reduces speed).
* 📲  **Executable Format** : Packaged as an executable file for easy sharing across different platforms and systems.

## 🚀 Getting started

**IMPORTANT NOTE: For an in-depth look at the development process behind this project, check out the comprehensive wiki available at the header of the README or click [here](https://airbnb-rio-de-janeiro.onrender.com/). It covers every aspect of the project, from initial concept to final implementation.**

### Download

1. As the dist folder was too heavy to be committed on Github, you will need to download it from google drive. Go to the header of this README file and click on "Download .exe folder", alternatevely, click [here](https://drive.google.com/drive/folders/1q_4X9UAha5WXrZVSjj4235ktvcQOZNx6?usp=sharing)
2. You will be taken to a google drive with the dist folder. Download all files in zip format by clicking on the name dist located on the top of the page then on "Make download"

![1713871827813](image/README/1713871827813.png)

```yaml
version: '3.8'

services:
  mafl:
    image: hywax/mafl
    restart: unless-stopped
    ports:
      - '3000:3000'
    volumes:
      - ./config.yml:/app/data/config.yml
```

### Executing the file

First, clone the repository:

```shell
git clone https://github.com/hywax/mafl.git
```

Then install dependencies and build the production bundle (I'm using `yarn` here, you can use `npm` or `pnpm` if you like):

```shell
yarn install
yarn build
```

Finally, run the server:

```shell
yarn preview
```

The application will start with a basic configuration, which is located in the `data` folder.

### Proxmox

To create a new Proxmox VE Mafl LXC, run the command below in the Proxmox VE Shell.

```shell
bash -c "$(wget -qLO - https://github.com/tteck/Proxmox/raw/main/ct/mafl.sh)"
```

Configure the application by editing the `config.yml` file:

```shell
nano /opt/mafl/data/config.yml
```

Many thanks to [@tteck](https://github.com/tteck) for helping me create lxc script.

## 📊 Services

The basic concept of `Mafl` is to create not just a homepage, but to create an interactive homepage page. You can combine different services with each other. You can combine different services to create the perfect customized homepage for you.

List of services:

* **[Base](https://mafl.hywax.space/services/base.html)** - The main card of the service. Other services are created on the basis of this service.
* **[IP API](https://mafl.hywax.space/services/ip-api.html)** - Shows information about your IP address.
* **[Weather](https://mafl.hywax.space/services/openweathermap.html)** - Shows weather information for your location.

## 🎨 Themes

There are several ready-made themes in `Mafl`. But nothing prevents you from creating your own design themes and sharing them with other users

<img src="https://raw.githubusercontent.com/hywax/mafl/main/docs/public/themes.png" alt="Mafl themes" width="100%"/>

## 🖼 Icons

Services can have icons. With support for several different icon packs, you can find the perfect thumbnail for any application or service.

Supported types:

* **[Iconify](https://icon-sets.iconify.design/)** - Over 200,000 open source vector icons
* **Emoji** - Any valid emoji can be used as an icon
* **URL** - Pass the URL of any matching image so that it can be found and displayed.
* **Local** - Store custom images locally and reference them by file name

## 🌎 Multi-language

`Mafl` supports multiple languages and locales. The app should automatically detect your language and set it in the settings. If not, set it in `config.yml` with the `lang` property.

Supported Languages:

* 🇬🇧 **English** - `en`
* 🇷🇺 **Russian** - `ru`
* 🇨🇳 **Chinese** - `zh`
* 🇨🇮 **Hindi** - `hi`
* 🇪🇸 **Spanish** - `es`
* 🇸🇦 **Arabic** - `ar` (by [@mohmadhabib](https://github.com/mohmadhabib))
* 🇵🇱 **Polish** - `pl` (by [@UberDudePL](https://github.com/UberDudePL))
* 🇫🇷 **France** - `fr` (by [@maxim31cote](https://github.com/maxim31cote))

If you haven't found your language, it can easily be added! Use the instructions in the section [contributing](https://mafl.hywax.space/community/contributing.html) on docs.

## 🏆 Credits

A huge thank you to everyone who is helping to improve Mafl. Thanks to you, the project can evolve!

### Contributors

To become a contributor, please follow our [contributing guide](https://mafl.hywax.space/community/contributing.html).

<img src="https://raw.githubusercontent.com/hywax/mafl/main/docs/public/contributors.svg" alt="Mafl Contributors" width="100%"/>

## 📄 License

This app is open-sourced software licensed under the [MIT license](https://github.com/hywax/mafl/blob/main/LICENSE).
