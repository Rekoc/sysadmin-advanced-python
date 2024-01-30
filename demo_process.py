from multiprocessing import Process, Queue
import requests

def get_website_html(url: str, q: Queue):
    q.put(requests.get(url=url))

def main():
    urls = {
        "https://google.com/", "https://google.fr",
    }
    q = Queue()
    processes = []
    for url in urls:
        p = Process(target=get_website_html, args=(url, q,))
        p.start()
        processes.append(p)

    for process in processes:
        # Attend la fin de chaque thread
        process.join()

    while not q.empty():
        # Affiche le contenu des requêtes
        print(q.get().text)

if __name__ == '__main__':
    main()