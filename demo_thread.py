import threading, queue
import requests

def get_website_html(url: str, q: queue.Queue):
    q.put_nowait(requests.get(url=url))

def main():
    urls = {
        "https://google.com/", "https://google.fr",
        "https://reddit.com", "https://www.blogger.com",
    }
    q = queue.Queue()
    threads = []
    for url in urls:
        t = threading.Thread(target=get_website_html, args=(url, q,))
        t.start()
        threads.append(t)

    for thread in threads:
        # Attend la fin de chaque thread
        thread.join()

    while not q.empty():
        # Affiche le contenu des requêtes
        print(q.get().text)

if __name__ == '__main__':
    main()