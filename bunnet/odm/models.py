from typing import List

from pydantic import BaseModel

from bunnet.odm.enums import InspectionStatuses
from bunnet.odm.fields import PydanticObjectId


class InspectionError(BaseModel):
    """
    Inspection error details
    """

    document_id: PydanticObjectId
    error: str


class InspectionResult(BaseModel):
    """
    Collection inspection result
    """

    status: InspectionStatuses = InspectionStatuses.OK
    errors: List[InspectionError] = []
