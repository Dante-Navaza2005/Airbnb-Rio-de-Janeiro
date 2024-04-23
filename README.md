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
  * [Video demonstration]()
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

3. The compressed file size is relatively large due to the extensive data used by the prediction model and the inclusion of all necessary modules and libraries whithin the executable
4. After downloading the folder, extract it on your computer.

![1713872396966](image/README/1713872396966.png)

### Executing the file

1. Open the extracted dist folder
2. Inside it there will be another dist folder, open it until you see a executable file called "run"

![1713872730244](image/README/1713872730244.png)

3. Double click the run file to execute it.
4. When done so, a empty terminal screen will appear, **wait** until the file automatically opens the project app into your browser. (If it doesnt automatically open for you, click on the Local URL displayed on the terminal after it finished executing)

![1713872988867](image/README/1713872988867.png)    

5. On the first launch, the terminal might prompt you to enter your email address. If it does, you can safely provide it. This step is only for bot verification and you won't receive any spam.
6. When entering the app page, you **NEED** to upload the final_model.joblib file into the specified box as it is the file that contains the prediction model. It should already be located inside the downlaoded dist folder, but in case it isn't a link to download it will be shown on the app page.
7. That's it! You can now customize the property characteristics by adjusting the parameters on the page to match your desired case. Once you're ready, click the "View the predicted value" button at the bottom of the page to see the estimated daily rental price. (**Note:** The results may take a few seconds to appear, depending on your machine's performance.)

### Video demonstration

Here's a video that walks you through the entire process, from opening the executable to adjusting the parameters and running the model:


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
