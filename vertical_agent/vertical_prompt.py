class VerticalPrompt:
    def __init__(self):
        pass
    
    def user_prompt(self, client_name,client_description,website_url=None):
        user_input = f"""
    Identify the primary business domain for the following client:
    Client Name: {client_name}
        Client Description: {client_description}
        Website url: {website_url if website_url else 'No website url available'}

    Based on this information, classify the client into one of the following business domains:
        - List your predefined business domains here, e.g., Healthcare, Finance, Retail, Manufacturing, Technology, Education, etc.
        - Search on the internet if needed to gather information releted to domian or speecific industry or try to search the link or url provided above to get the information.
        
        Provide the following in your response in JSON format:
    
            "domain_name": "Identified Business Domain Name",
            "domain_description": "A brief description of the identified domain based on the client info",
            "keywords": "list", "of", "relevant", "keywords",  
            "confidence_score": 0.95; Confidence score between 0.0 and 1.0

        ***Instructions***:
        - Domain Name: domain should be specific example: Healthcare, Finance, Retail, Manufacturing, Technology, Education, etc. are the higher level domain but you need to be more specific like: "Healthcare: Medical Devices", "Finance: Investment Banking", "Retail: E-commerce", etc.
        - Domain Description: A brief description of the identified domain based on the client info make sure that description expalin it well.
        - Keywords: List of relevant keywords that helped you identify the domain and data releted that domain.
        - Confidence Score: A confidence score between 0.0 and 1.0 indicating how confident you are in your classification. 0.0 means no confidence, 1.0 means full confidence.
    
        If you cannot confidently classify the domain, return null or an empty JSON.
"""
        return user_input
    
    def system_prompt(self):
        system_input = f"""
        Your a helpful AI assistancee that gives meaaning  full verticals of business:
    """
        return system_input
    
    

