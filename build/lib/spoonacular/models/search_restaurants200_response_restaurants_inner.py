# coding: utf-8

"""
    spoonacular API

    The spoonacular Nutrition, Recipe, and Food API allows you to access over thousands of recipes, thousands of ingredients, 800,000 food products, over 100,000 menu items, and restaurants. Our food ontology and semantic recipe search engine makes it possible to search for recipes using natural language queries, such as \"gluten free brownies without sugar\" or \"low fat vegan cupcakes.\" You can automatically calculate the nutritional information for any recipe, analyze recipe costs, visualize ingredient lists, find recipes for what's in your fridge, find recipes based on special diets, nutritional requirements, or favorite ingredients, classify recipes into types and cuisines, convert ingredient amounts, or even compute an entire meal plan. With our powerful API, you can create many kinds of food and especially nutrition apps.  Special diets/dietary requirements currently available include: vegan, vegetarian, pescetarian, gluten free, grain free, dairy free, high protein, whole 30, low sodium, low carb, Paleo, ketogenic, FODMAP, and Primal.

    The version of the OpenAPI document: 1.1
    Contact: mail@spoonacular.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from spoonacular.models.search_restaurants200_response_restaurants_inner_address import SearchRestaurants200ResponseRestaurantsInnerAddress
from spoonacular.models.search_restaurants200_response_restaurants_inner_local_hours import SearchRestaurants200ResponseRestaurantsInnerLocalHours
from typing import Optional, Set
from typing_extensions import Self

class SearchRestaurants200ResponseRestaurantsInner(BaseModel):
    """
    SearchRestaurants200ResponseRestaurantsInner
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, alias="_id")
    name: Optional[StrictStr] = None
    phone_number: Optional[StrictInt] = None
    address: Optional[SearchRestaurants200ResponseRestaurantsInnerAddress] = None
    type: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    local_hours: Optional[SearchRestaurants200ResponseRestaurantsInnerLocalHours] = None
    cuisines: Optional[List[StrictStr]] = None
    food_photos: Optional[List[StrictStr]] = None
    logo_photos: Optional[List[StrictStr]] = None
    store_photos: Optional[List[Dict[str, Any]]] = None
    dollar_signs: Optional[StrictInt] = None
    pickup_enabled: Optional[StrictBool] = None
    delivery_enabled: Optional[StrictBool] = None
    is_open: Optional[StrictBool] = None
    offers_first_party_delivery: Optional[StrictBool] = None
    offers_third_party_delivery: Optional[StrictBool] = None
    miles: Optional[Union[StrictFloat, StrictInt]] = None
    weighted_rating_value: Optional[Union[StrictFloat, StrictInt]] = None
    aggregated_rating_count: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["_id", "name", "phone_number", "address", "type", "description", "local_hours", "cuisines", "food_photos", "logo_photos", "store_photos", "dollar_signs", "pickup_enabled", "delivery_enabled", "is_open", "offers_first_party_delivery", "offers_third_party_delivery", "miles", "weighted_rating_value", "aggregated_rating_count"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SearchRestaurants200ResponseRestaurantsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of local_hours
        if self.local_hours:
            _dict['local_hours'] = self.local_hours.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchRestaurants200ResponseRestaurantsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_id": obj.get("_id"),
            "name": obj.get("name"),
            "phone_number": obj.get("phone_number"),
            "address": SearchRestaurants200ResponseRestaurantsInnerAddress.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "type": obj.get("type"),
            "description": obj.get("description"),
            "local_hours": SearchRestaurants200ResponseRestaurantsInnerLocalHours.from_dict(obj["local_hours"]) if obj.get("local_hours") is not None else None,
            "cuisines": obj.get("cuisines"),
            "food_photos": obj.get("food_photos"),
            "logo_photos": obj.get("logo_photos"),
            "store_photos": obj.get("store_photos"),
            "dollar_signs": obj.get("dollar_signs"),
            "pickup_enabled": obj.get("pickup_enabled"),
            "delivery_enabled": obj.get("delivery_enabled"),
            "is_open": obj.get("is_open"),
            "offers_first_party_delivery": obj.get("offers_first_party_delivery"),
            "offers_third_party_delivery": obj.get("offers_third_party_delivery"),
            "miles": obj.get("miles"),
            "weighted_rating_value": obj.get("weighted_rating_value"),
            "aggregated_rating_count": obj.get("aggregated_rating_count")
        })
        return _obj


