from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_party.linkedin import scrape_linkedin_profile
from third_party.linkedin import scrape_linkedin_profile_gist

information = """
William Henry Gates III (born October 28, 1955) is an American billionaire, philanthropist, and investor best known for co-founding the software giant Microsoft, along with his childhood friend Paul Allen.[2][3] During his career at Microsoft, Gates held the positions of chairman, chief executive officer (CEO), president, and chief software architect, while also being its largest individual shareholder until May 2014.[4] He was a major entrepreneur of the microcomputer revolution of the 1970s and 1980s.

Gates was born and raised in Seattle, Washington. In 1975, he and Allen founded Microsoft in Albuquerque, New Mexico. It later became the world's largest personal computer software company.[5][a] Gates led the company as its chairman and chief executive officer until stepping down as CEO in January 2000, succeeded by Steve Ballmer, but he remained chairman of the board of directors and became chief software architect.[8] During the late 1990s, he was criticized for his business tactics, which were considered anti-competitive. This opinion has been upheld by numerous court rulings.[9] In June 2008, Gates transitioned into a part-time role at Microsoft and full-time work at the Bill & Melinda Gates Foundation, the private charitable foundation he and his then-wife Melinda had established in 2000.[10] He stepped down as chairman of the Microsoft board in February 2014 and assumed the role of technology adviser to support newly appointed CEO Satya Nadella.[11] In March 2020, Gates left his board positions at Microsoft and Berkshire Hathaway to focus on his philanthropic efforts on climate change, global health and development, and education.[12]

Since 1987, Gates has been included in the Forbes list of the world's billionaires.[13][14] From 1995 to 2017, he held the Forbes title of the richest person in the world every year except in 2008 and from 2010 to 2013.[15] In October 2017, he was surpassed by Amazon founder and CEO Jeff Bezos, who had an estimated net worth of US$90.6 billion compared to Gates's net worth of US$89.9 billion at the time.[16] As of September 2023, Gates has an estimated net worth of US$123 billion, making him the fourth-richest person in the world according to Bloomberg Billionaires Index.[17]

Later in his career and since leaving day-to-day operations at Microsoft in 2008, Gates has pursued other business and philanthropic endeavors. He is the founder and chairman of several companies, including BEN, Cascade Investment, TerraPower, bgC3, and Breakthrough Energy. He has donated sizable amounts of money to various charitable organizations and scientific research programs through the Bill & Melinda Gates Foundation, reported to be the world's largest private charity.[18] Through the foundation, he led an early 21st century vaccination campaign that significantly contributed to the eradication of the wild poliovirus in Africa.[19][20] In 2010, Gates and Warren Buffett founded The Giving Pledge, whereby they and other billionaires pledge to give at least half of their wealth to philanthropy.[21]
"""

if __name__ == "__main__":
    print("Person Profile")

    summary_template = """
        given the information {information} about a person from I want you to create: 
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # temperature -> creativity
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # linkedin_data = scape_linkedin_profile("https://www.linkedin.com/in/williamhgates/")
    linkedin_data = scrape_linkedin_profile_gist()

    print(chain.run(information=linkedin_data))
