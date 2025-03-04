from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import tool
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import initialize_agent,Tool
from langchain.agents import AgentType
from langchain_community.utilities import SerpAPIWrapper


class DomainIntelligenceAgent:

    def __init__(self,):
        print("Vertical Agent Initialized✅")
        self.models = {
            "google": ChatGoogleGenerativeAI,
            "openai": ChatOpenAI
        }
        self.output_parser = {
            "str": StrOutputParser,
            "json": JsonOutputParser,
            "pydantic": PydanticOutputParser
        }


    # Set Up Web Search Tool using SerpAPI
    def _search_website_content(self):
        serpapi = SerpAPIWrapper()
        web_search_tool = Tool(
                name="Web Search Tool",
                func=serpapi.run,
                description="This tool allows the agent to perform real-time web searches to retrieve relevant and up-to-date information from the internet. It is useful for answering queries that require external knowledge or the latest data."
            )
        return web_search_tool
    
    
    def _classify_business_domain(self,system_input,user_input,model_name,model_variant,verbose=False,output_parser="str"):
        if model_name not in self.models:
            raise ValueError(f"Invalid model '{model_name}'. Available models: {list(self.models.keys())}")
        
        # defining llm model
        llm = self.models[model_name](model=model_variant)

        # propmt template
        prompt_template = ChatPromptTemplate([
        ("system", system_input),
        ("user", user_input)
        ])
        # tool
        web_search_tool = self._search_website_content()
        tools = [web_search_tool]

        # ✅ Initialize the Agent
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=verbose
        )

        # formating prompt
        formated_prompt=prompt_template.invoke({})

        # generating responce
        content = agent.run(formated_prompt)

        # Initialize output parser
        output_parser = self.output_parser[output_parser]

        # parsing output by llm to get the final responce
        parsed_output = output_parser().parse(content)

        return parsed_output

    def model_list(self):
        return list(self.models.keys())
    
    def output_parser_list(self):
        return list(self.output_parser.keys())
    