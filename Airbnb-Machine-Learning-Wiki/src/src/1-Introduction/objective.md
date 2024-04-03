# Context and Objective

Airbnb allows anyone with a spare room or property of any type (apartment, house, chalet, inn, etc.) to list their property for rent on a daily basis.

As a host, you create your profile and list your property. In this listing, hosts should provide a comprehensive description of the property to assist renters/travelers in choosing the best accommodation and to make their listing more appealing.

There are numerous customizations available in the listing, ranging from minimum stay requirements, pricing, number of rooms, to cancellation policies, extra guest fees, identity verification requirements for renters, etc.

### Our Objective

To build a price prediction model that enables property owners to determine the appropriate daily rate for their property. Additionally, to assist renters in evaluating whether a listed property offers a competitive price compared to similar properties with similar characteristics.

### Available Resources, Inspirations, and Credits

The datasets were sourced from Kaggle: [https://www.kaggle.com/datasets/allanbruno/airbnb-rio-de-janeiro](https://www.kaggle.com/datasets/allanbruno/airbnb-rio-de-janeiro). Data spans from April 2018 to May 2020, with the exception of June 2018, which lacks data.

Given the 50MB per file space restriction in GitHub Repositories, the datasets utilized in this project are accessible for download via this link: [https://drive.google.com/file/d/1_RtxDTXtF3CGvioFi1_ophzLNmyguEHl/view?usp=sharing](https://drive.google.com/file/d/1_RtxDTXtF3CGvioFi1_ophzLNmyguEHl/view?usp=sharing). Alternatively, you may procure the datasets directly from Kaggle. However, it's noteworthy that discrepancies may arise in results if the datasets have been updated subsequent to the project's inception.

- File names are in brazilian portuguese
- The datasets contain property prices and their respective characteristics for each month.
- Prices are listed in Brazilian Real (R$).

### Initial Expectations

- Seasonality is expected to be a significant factor, as months like December tend to have higher prices in Rio de Janeiro.
- Property location is likely to have a substantial impact on pricing, given that location can drastically alter the characteristics of a place (e.g., safety, natural beauty, proximity to tourist attractions).
- Additional amenities may have a significant impact, considering the prevalence of older buildings and houses in Rio de Janeiro.

We aim to explore the extent to which these factors influence pricing and identify any less intuitive yet crucial factors.
