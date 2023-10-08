import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """Scrap information from Linkedin profiles"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    # clean up data
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


def scrape_linkedin_profile_gist():
    api_endpoint = "https://gist.githubusercontent.com/khongks/15bff9c895f2f33e8ca49806dedca575/raw/865ebad5f798ac9e208e8b7f5dd56d5687c51aa8/gistfile1.txt"

    response = requests.get(api_endpoint)

    # clean up data
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
