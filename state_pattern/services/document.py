from project.core import Service, service
from state_pattern.repositories import DocumentRepository
from state_pattern.schemas.simple_doc import SimpleDoc
from fastapi import Depends


@service
class DocumentService(Service):
    document_repos: DocumentRepository = Depends(DocumentRepository)

    async def save(self, id, document: SimpleDoc) -> SimpleDoc:
        document.id = id
        return SimpleDoc.parse_obj(await self.document_repos.save(document.dict()))

    async def apply_control(self, id):
        ...

    async def apply_approve(self, id):
        ...

    async def approve(self, id):
        ...

    async def return_init(self, id):
        ...

    async def close(self, id):
        ...
