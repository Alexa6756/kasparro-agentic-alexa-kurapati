import json
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

def parser_node(state):
    def parse_tool(data: str) -> str:
        d = json.loads(data)
        return json.dumps({
            "name": d["Product Name"],
            "concentration": d["Concentration"],
            "skin_type": d["Skin Type"].split(", "),
            "ingredients": d["Key Ingredients"].split(", "),
            "benefits": d["Benefits"].split(", "),
            "usage": d["How to Use"],
            "side_effects": d["Side Effects"],
            "price": d["Price"]
        })

    tools = [Tool(
        name="parse_product",
        func=parse_tool,
        description="Parse raw product JSON into structured fields"
    )]

    prompt = PromptTemplate.from_template(
        """You are a parsing agent.

Tools:
{tools}

Tool names:
{tool_names}

Question: {input}
Thought:{agent_scratchpad}"""
    )

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    agent = create_react_agent(llm, tools, prompt)
    executor = AgentExecutor(agent=agent, tools=tools)

    result = executor.invoke({"input": state["raw_product_data"]})
    state["parsed_product"] = json.loads(result["output"])
    return state
