# LangChain版本的旅游规划机器人
> [Github](https://github.com/kbmjj123/travel_planning_robot_langchain)
> 初次模仿一AI应用，尝试使用LangChain来开发一旅游规划机器人，感受关于AI开发的流程

## 项目介绍
> 项目模仿并改写网络上的旅游规划机器人，使用纯LangChain开发，借助于LangChain中的`create_react_agent`方法，快速创建一个agent，
> 并将agent转交给AgentExecutor来执行，期间也踩了不少了坑

## 目录结构
travel_planning_robot_langchain/
├── agents/
│   ├── __init__.py
│   └── index.py    公共的agent智能体的入口
├── models/
│   ├── __init__.py
│   └── llm_factory.py  公共的模型工厂
├── prompts/
│   ├── __init__.py
│   ├── constants.py    静态化提示词模版
│   └── index.py        对外提供统一访问入口
├── tools/
│   ├── __init__.py     工具包的入口
│   ├── attractions.py  获取景点信息tool
│   ├── index.py        将所有的工具包整合到统一的一个方法入口，在该模块中仅识别此入口方法
│   ├── locations.py    获取景点位置信息
│   ├── nearby.py       搜索景点周边好玩的地方
│   ├── save.py         保存景点信息
│   ├── static_map.py   保存景点的静态地图信息
│   ├── transportation.py   搜索静定的路径规划
│   └── web_search.py   搜索网页信息
├── utils/
│   ├── __init__.py
│   └── helper.py
├── LICENSE
├── README.md
├── app.py
└── requirements.txt

项目按照最基本的python项目的模块管理(提供__init__.py，将需要对外暴露的元素定义在__init__.py中)，
模块管理采用python的包管理工具pip，项目依赖包在requirements.txt文件中。

### 项目存在的问题
1. 项目依赖于`LangChain`的`create_react_agent`，导致必须使用带有英文标识的提示词(这边目前采用的英文版本的提示词)，否则直接报错；
2. 项目采用一个提示词，然后由agent自行决定接下来应该做什么，提示词的生成逻辑比较复杂，需要结合项目实际需求进行修改；
3. 由于采用的agent+AgentExecutor，因此无法流式输出，而是阶段性chunked输出；
4. 有一些tool应该需要支持同时调用，但是目前的react_agent并不能实现到。