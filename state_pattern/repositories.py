import abc
import json
from typing import List, Dict, Optional

from project.core import Base, service


class AbstractRepository(Base, abc.ABC):
    db = None
    table = None

    async def find_all(self) -> List[Dict]:
        f = open(self.db, "r")
        return json.load(f).get(self.table, [])

    async def find_by_id(self, id: int) -> Optional[Dict]:
        f = open(self.db, "r")
        obj_opt = list(filter(lambda d: d["id"] == id, json.load(f)[self.table]))
        if obj_opt:
            return obj_opt[0]
        else:
            return None

    async def save(self, obj: Dict) -> Dict:
        f = open(self.db, "r")
        session = json.load(f)
        obj_opt = list(filter(lambda doc: doc["id"] == obj.get("id", 0), session[self.table]))
        return await self.__update(obj) if obj_opt else await self.__insert(obj)

    async def __insert(self, obj: Dict) -> Dict:
        f = open(self.db, "r")
        session = json.load(f)
        prev_id = (await self.find_last())["id"]
        obj.update({"id": prev_id + 1})
        session[self.table].append(obj)
        json.dump(session, open(self.db, "w"))
        return obj

    async def __update(self, obj: Dict) -> Dict:
        f = open(self.db, "r")
        session = json.load(f)
        obj_opt = list(filter(lambda doc: doc["id"] == obj.get("id", 0), session[self.table]))
        old_obj = obj_opt[0]
        session[self.table].remove(old_obj)
        old_obj.update(obj)
        session[self.table].insert(old_obj["id"] - 1, old_obj)
        json.dump(session, open(self.db, "w"))
        return obj

    async def find_last(self) -> Optional[Dict]:
        f = open(self.db, "r")
        session = json.load(f)
        obj_opt = list(sorted(session[self.table], key=lambda d: d["id"], reverse=True))
        if obj_opt:
            return obj_opt[0]
        else:
            return None


@service
class DocumentRepository(AbstractRepository):
    db = "../simple_database.json"
    table = "documents"


@service
class UserRepository(AbstractRepository):
    db = "../simple_database.json"
    table = "users"
