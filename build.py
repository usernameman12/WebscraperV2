import dns.resolver
import socket
import requests
from bs4 import BeautifulSoup

# Existing function definitions...

def get_dns_record(domain):
    """Get the A record (IP address) of a domain."""
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return [answer.to_text() for answer in answers]
    except Exception as e:
        print(f"Error resolving DNS for {domain}: {e}")
        return []

def reverse_dns_lookup(ip):
    """Find domains hosted on the same IP using reverse DNS lookup."""
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return [hostname]
    except Exception as e:
        print(f"Error performing reverse DNS lookup for {ip}: {e}")
        return []

def search_code_snippet(domain, snippet):
    """Search for a code snippet in the HTML of the given domain."""
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return snippet in soup.prettify()
    except Exception as e:
        print(f"Error fetching or parsing HTML for {domain}: {e}")
        return False

# New soupboot function
def soupboot():
    print("Running soupboot...")
    # Add the desired functionality for soupboot here
    # For example, you can call existing functions or add new logic
    # Example:
    domain = "example.com"
    snippet = "<title>Example Domain</title>"
    ips = get_dns_record(domain)
    if ips:
        for ip in ips:
            print(f"IP address for {domain}: {ip}")
            hosted_domains = reverse_dns_lookup(ip)
            for hosted_domain in hosted_domains:
                print(f"Hosted domain: {hosted_domain}")
                if search_code_snippet(hosted_domain, snippet):
                    print(f"Snippet found in {hosted_domain}")
                else:
                    print(f"Snippet not found in {hosted_domain}")
    else:
        print(f"No IP addresses found for {domain}")

def main():
    domain = input("Enter the domain: ").strip()
    snippet = input("Enter the code snippet to search for: ").strip()
    # Step 1: Get the DNS record (A record)
    ips = get_dns_record(domain)
    if not ips:
        print("No IPs found for the domain.")
        return
    print(f"Found IPs: {ips}")
    # Step 2: Find domains hosted on the same IP(s)
    hosted_domains = set()
    for ip in ips:
        hosted_domains.update(reverse_dns_lookup(ip))
    if not hosted_domains:
        print("No hosted domains found.")
        return
    print(f"Domains hosted on the same IP(s): {hosted_domains}")
    # Step 3: Search for the code snippet in the hosted domains
    for hosted_domain in hosted_domains:
        print(f"Searching {hosted_domain} for the snippet...")
        if search_code_snippet(hosted_domain, snippet):
            print(f"Snippet found in {hosted_domain}!")
        else:
            print(f"Snippet not found in {hosted_domain}.")

if __name__ == "__main__":
    print("Initializing soupboot...")
    soupboot()
    main()
