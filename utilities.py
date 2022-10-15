import os
import re
import subprocess
import json
from typing import List, Dict


def generate_prisma_client():
    """Generates the Prisma Client and loads it
    """
    print(f'GENERATING PRISMA CLIENT')
    subprocess.call(["prisma", "generate"])
    print(f'GENERATED PRISMA CLIENT')

generate_prisma_client()
try:
    from prisma import Prisma
except RuntimeError:
    print(f'GOT RUNTIME ERROR')
    generate_prisma_client()
    from prisma import Prisma


class Movies:
    """Movies class with methods to search and list movies
    """
    def __init__(self):
        self.db = Prisma()
        self.db.connect()

    def to_dict(self, obj: object):
        """Converts an Object to Dictionary

        Args:
            obj (object): Object to convert to dictionary

        Returns:
            Dict: Values of object in a dictionary
        """
        return json.loads(json.dumps(obj, default=lambda o: o.__dict__))

    def list_movies_by_title(self, title):
        """Returns list of movies based on the title

        Args:
            title (str): Title or part of title

        Returns:
            List[Dict]: List of movies matching the title
        """
        matches = self.db.movies.find_many(where={
            "meta": {
                "every": {
                    "title": {
                        "contains": title,
                        "mode": "insensitive"
                    }
                }
            }
        },
                                           include={
                                               "meta": True,
                                               "cast": True,
                                               "poster": {
                                                   "take": 3
                                               }
                                           })
        matches = list(map(lambda m: self.to_dict(m), matches))
        return matches


if __name__ == "__main__":
    import json
    movies = Movies()
    srch = movies.list_movies_by_title("harry")
    # print(movies.list_movies_by_title("harry"))
    with open("op.json", "w") as fp:
        json.dump(srch, fp)
#     generate_prisma_client()