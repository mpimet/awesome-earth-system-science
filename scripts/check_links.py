# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
# ]
# ///
import re
import requests


def check_links():
    # Captures all markdown links starting with http(s)
    re_link = re.compile(r"\[.*?\]\((https?://[^\s)]+)\)")

    # Add a timeout, and use headers to avoid blocks from some servers
    headers = {"User-Agent": "curl/8.7.1"}
    timeout = 5

    broken_links = []
    with open("README.md", "r", encoding="utf-8") as fp:
        for lineno, line in enumerate(fp, start=1):
            urls = re_link.findall(line)
            for url in urls:
                try:
                    response = requests.get(url, headers=headers, timeout=timeout)
                    if response.status_code >= 400:
                        broken_links.append(
                            f"{url} (line {lineno}, status {response.status_code})"
                        )
                except requests.RequestException as e:
                    broken_links.append(f"{url} (line {lineno}, error: {str(e)})")

    if broken_links:
        message = "The following links are broken:\n" + "\n".join(broken_links)
        raise Exception(message)


if __name__ == "__main__":
    check_links()
