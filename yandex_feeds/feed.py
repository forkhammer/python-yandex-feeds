from pydantic_xml import BaseXmlModel, attr, element

class Category(BaseXmlModel, tag="category"):
    id: str = attr()
    name: str

class Categories(BaseXmlModel, tag="categories"):
    categories: list[Category] = element(tag="category", default=[])


class Offer(BaseXmlModel, tag="offer"):
    id: str = attr()
    name: str = element()
    vendor: str = element()
    price: str = element()
    currencyId: str = element()
    categoryId: str = element()
    picture: str = element()
    description: str = element()
    shortDescription: str = element()
    url: str = element()


class Offers(BaseXmlModel, tag="offers"):
    offers: list[Offer] = element(tag="offer", default=[])


class Shop(BaseXmlModel, tag="shop"):
    categories: Categories = element(tag="categories")
    offers: Offers = element(tag="offers")


class YmlCatalog(BaseXmlModel, tag="yml_catalog"):
    shop: Shop


class YandexProductFeed:

    def __init__(self) -> None:
        super().__init__()
        self._root = YmlCatalog(shop=Shop(categories=Categories(), offers=Offers()))

    def add_category(self, category_id: str, category_name: str) -> None:
        self._root.shop.categories.categories.append(Category(id=category_id, name=category_name))

    def add_offer(
        self,
        offer_id: str,
        offer_name: str,
        vendor: str,
        price: str,
        currency_id: str,
        category_id: str,
        picture: str,
        description: str,
        short_description: str,
        url: str
    ) -> None:
        self._root.shop.offers.offers.append(
            Offer(
                id=offer_id,
                name=offer_name,
                vendor=vendor,
                price=price,
                currencyId=currency_id,
                categoryId=category_id,
                picture=picture,
                description=description,
                shortDescription=short_description,
                url=url
            )
        )

    def to_xml(self) -> str:
        return self._root.to_xml(encoding='UTF-8')