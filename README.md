# Autogidas.lt spider

This spider scrapes cars' ads from https://autogidas.lt/ 

The spider will get car's make, model, manufactured date, fuel type, body type, gearbox type, mileage, price and image's url.

# Running spider

Run a spider by using `scrapy crawl` command like that:
```
$ scrapy crawl autogidas
```
Spider will save ads to jsonlines file `ads.jl` and ads will look like that:
```
{"make": "Mercedes-Benz", "model": "SL 320", "mfd_date": "1997", "fuel_type": "Benzinas", "body_type": "Kabrioletas", "gearbox_type": "Automatinė", "mileage": "124600", "price": "8200", "img_url": "https://img.autogidas.lt/4_15_182269987/mercedes-benz-sl-320-kabrioletas-1997.jpg"}
```
Happy using!
