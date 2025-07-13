import os
from langchain_core.tools import tool
from typing import Annotated
import requests
from dotenv import load_dotenv, find_dotenv

@tool
def search_nearby_poi(
    location: Annotated[str, "中心点坐标，以“,”分割，经度在前，纬度在后，如117.500244,40.417801"],
    city: Annotated[str, "查询中心点所在的城市编码。"],
    types: Annotated[str, "查询POI类型。多个类型用“|”分割。如果查询住宿，只能填写以下类型：“宾馆酒店”“旅馆招待所”。如果查询餐饮，只能填写以下类型：“中餐厅”“外国餐厅”“快餐厅”。关键字和POI类型二者至少填写一个。"] = "",
    keyword: Annotated[str, "要搜索的关键字。除非用户有特别指定具体的地点名称时才填写，如“星巴克”“希尔顿”等，否则不要填写！一次只能搜索一个关键字。关键字和POI类型二者至少填写一个。"] = "",
    radius: Annotated[int, "查询半径，单位米。"] = 5000,
    offset: Annotated[int, "每页搜索结果数目。"] = 10,
    page: Annotated[int, "当前页数。"] = 1
):
    """周边搜索工具。根据中心点坐标和关键字或POI类型搜索周边POI。返回结果中，距离的单位都是米，费用的单位都是元。"""
    _ = load_dotenv(find_dotenv())
    
    if keyword == "" and types == "":
        raise ValueError("关键字和POI类型至少填写一个。")
    
    amap_key = os.getenv("AMAP_API_KEY")
    base_url = "https://apis.map.qq.com/ws/place/v1/explore?"
    url = f"{base_url}key={amap_key}&boundary=nearby({location},1000,1)&policy=1&keywords={keyword}&filter=category={types}&city={city}&radius={radius}&page_size={offset}&page_index={page}"
    r = requests.get(url)
    result = r.json()
    print('result:',result)

    poi = keyword or types
    if result['status'] != 0:
        raise ValueError(f"在{location}周边搜索{poi}失败。请检查中心点、城市编码、POI类型填写是否正确。错误信息: {result['info']}")
    if len(result['data']) == 0:
        return f"在{location}周边没有搜索到{poi}相关结果。尝试扩大搜索半径或者更换关键字或POI类型。"

    nearby_search_result = {
        "center_point": location,
        "search_result_count": result['count'],
        "data": []
    }

    for item in result['data']:
        nearby_search_result['data'].append({
            "name": item['title'],
            "type": item['category'],
            "address": item['address'],
            "distance": item['_distance'],
            "location": item['location'],
            "rating": item['biz_ext']['rating'] if 'biz_ext' in item else "not available",
            "cost": item['biz_ext']['cost'] if 'biz_ext' in item else "not available",
        })
    return nearby_search_result

# test the tool
if __name__ == "__main__":
    print(search_nearby_poi.args_schema.model_json_schema())
    a=search_nearby_poi.invoke({
        "location": "29.371356,113.129362",
        "city": "0730",
        # "keyword": "酒店",
        "types": "旅馆招待所,中餐厅",
        })
    print(a)