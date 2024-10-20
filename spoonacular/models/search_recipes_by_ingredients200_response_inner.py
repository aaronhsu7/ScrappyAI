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

from pydantic import BaseModel, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from spoonacular.models.search_recipes_by_ingredients200_response_inner_missed_ingredients_inner import SearchRecipesByIngredients200ResponseInnerMissedIngredientsInner
from typing import Optional, Set
from typing_extensions import Self

class SearchRecipesByIngredients200ResponseInner(BaseModel):
    """
    SearchRecipesByIngredients200ResponseInner
    """ # noqa: E501
    id: StrictInt
    image: Annotated[str, Field(min_length=1, strict=True)]
    image_type: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="imageType")
    likes: StrictInt
    missed_ingredient_count: StrictInt = Field(alias="missedIngredientCount")
    missed_ingredients: Annotated[List[SearchRecipesByIngredients200ResponseInnerMissedIngredientsInner], Field(min_length=0)] = Field(alias="missedIngredients")
    title: Annotated[str, Field(min_length=1, strict=True)]
    unused_ingredients: Annotated[List[Dict[str, Any]], Field(min_length=0)] = Field(alias="unusedIngredients")
    used_ingredient_count: Union[StrictFloat, StrictInt] = Field(alias="usedIngredientCount")
    used_ingredients: Annotated[List[SearchRecipesByIngredients200ResponseInnerMissedIngredientsInner], Field(min_length=0)] = Field(alias="usedIngredients")
    __properties: ClassVar[List[str]] = ["id", "image", "imageType", "likes", "missedIngredientCount", "missedIngredients", "title", "unusedIngredients", "usedIngredientCount", "usedIngredients"]

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
        """Create an instance of SearchRecipesByIngredients200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in missed_ingredients (list)
        _items = []
        if self.missed_ingredients:
            for _item in self.missed_ingredients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['missedIngredients'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in used_ingredients (list)
        _items = []
        if self.used_ingredients:
            for _item in self.used_ingredients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['usedIngredients'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchRecipesByIngredients200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "image": obj.get("image"),
            "imageType": obj.get("imageType"),
            "likes": obj.get("likes"),
            "missedIngredientCount": obj.get("missedIngredientCount"),
            "missedIngredients": [SearchRecipesByIngredients200ResponseInnerMissedIngredientsInner.from_dict(_item) for _item in obj["missedIngredients"]] if obj.get("missedIngredients") is not None else None,
            "title": obj.get("title"),
            "unusedIngredients": obj.get("unusedIngredients"),
            "usedIngredientCount": obj.get("usedIngredientCount"),
            "usedIngredients": [SearchRecipesByIngredients200ResponseInnerMissedIngredientsInner.from_dict(_item) for _item in obj["usedIngredients"]] if obj.get("usedIngredients") is not None else None
        })
        return _obj


