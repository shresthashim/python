import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all article titles (you may need to adjust the selector based on the site)
        titles = soup.find_all('h3')  # Example selector, change as needed
        
        # Extract and print the text of each title
        if titles:
            print("Article Titles:")
            for title in titles:
                print(title.get_text())
        else:
            print("No titles found on this page.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

def main():
    # Ask the user for a website URL
    url = input("Enter the URL of the website to scrape: ")
    
    # Call the scrape_titles function with the user-provided URL
    scrape_titles(url)

# Run the main function
if __name__ == '__main__':
    main()
