from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Catalog Page",
        "goods": [
            {
                "image": "deps/images/goods/redfizz.jpg",
                "name": "Red Dragon Fizz",
                "description": "Игровая 60% клавиатура от бренда Red Dragon",
                "price": 99.3,
            },
            {
                "image": "deps/images/goods/royelkl.jpg",
                "name": "Royal Kludge RK84 RGB",
                "description": "Игровая 75% клавиатура от бренда Royal Kludge",
                "price": 219.0,
            },
            {
                "image": "deps/images/goods/darkproject.jpg",
                "name": "Dark Project KD87A",
                "description": "Игровая 75% клавиатура от бренда Dark Project",
                "price": 594.6,
            },
            {
                "image": "deps/images/goods/G435.jpg",
                "name": "Logitech G435 Lightspeed",
                "description": "Абсолютно на всех этапах разработки, изготовления и доставки гарнитуры G435 был использован (по мере возможности) переработанный пластик.",
                "price": 239.2,
            },
            {
                "image": "deps/images/goods/HyperXCloud.jpeg",
                "name": "HyperX Cloud II",
                "description": "Наушники с микрофоном, мониторные (охватывающие), геймерские, 15-25000 Гц, кабель 1 м",
                "price": 319.0,
            },
            {
                "image": "deps/images/goods/logitech superlight.jpg",
                "name": "Logitech G Pro Wireless",
                "description": "полноразмерная игровая мышь для ПК, проводная USB/беспроводная радио, сенсор оптический 25000 dpi, 7 кнопок, колесо с нажатием, цвет черный",
                "price": 294.9,
            },
            {
                "image": "deps/images/goods/LogitechProX.jpg",
                "name": "Logitech Pro X Superlight 2",
                "description": "полноразмерная игровая мышь для ПК, проводная USB/беспроводная радио, сенсор оптический 32000 dpi, 5 кнопок, колесо с нажатием, цвет черный",
                "price": 512.2,
            },
            {
                "image": "deps/images/goods/razerv2.jpg",
                "name": "Razer Viper V2 Pro",
                "description": "полноразмерная игровая мышь для ПК/для Microsoft Xbox, проводная USB/беспроводная радио, сенсор оптический 30000 dpi, 6 кнопок, колесо с нажатием, цвет черный",
                "price": 246.1,
            },
            {
                "image": "deps/images/goods/logmat.jpg",
                "name": "Logitech Desk Mat",
                "description": "оптические мыши/лазерные мыши, ткань, прошитые края, 300x700 мм, цвет серый",
                "price": 112.8,
            },
            {
                "image": "deps/images/goods/RazerGigantusV2.jpg",
                "name": "Razer Gigantus V2 3XL",
                "description": "оптические мыши/лазерные мыши, ткань, 550x1200 мм, цвет черный",
                "price": 210.7,
            },
            {
                "image": "deps/images/goods/Razer Pro Glide XXL.jpg",
                "name": "Razer Pro Glide XXL",
                "description": "оптические мыши/лазерные мыши, ткань, 410x940 мм, цвет серый",
                "price": 189.0,
            },
            {
                "image": "deps/images/goods/rykav.jpg",
                "name": "Рукав игровой",
                "description": "для киберспорта",
                "price": 15.3,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
