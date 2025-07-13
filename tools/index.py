from .attractions import get_attractions_information
from .locations import get_location_coordinate
from .nearby import search_nearby_poi
from .save import save_info_and_clear_history
from .static_map import  get_static_map
from .transportation import route_planning
from .web_search import web_search

def generate_tools():
    """生成当前智能体的工具列表"""
    return [
        get_location_coordinate,
        get_attractions_information,
        route_planning,
        web_search,
        search_nearby_poi,
        save_info_and_clear_history,
        get_static_map
    ]