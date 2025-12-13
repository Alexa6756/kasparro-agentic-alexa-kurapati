import json
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

def question_node(state):
    def generate_questions(data: str) -> str:
        product = json.loads(data)
        categories = ["Usage", "Safety", "Benefits", "Purchase", "Comparison"]
        questions = [
            {
                "question": f"What should I know about {product['name']}?",
                "category": categories[i % len(categories)]
            }
            for i in range(15)
        ]
        return json.dumps(questions)

    tools = [Tool(
        name="generate_questions",
        func=generate_questions,
        description="Generate categorized user questions"
    )]

    prompt = PromptTemplate.from_template(
        """Generate questions using the tool.

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

    result = executor.invoke({"input": json.dumps(state["parsed_product"])})
    state["questions"] = json.loads(result["output"])
    return state
