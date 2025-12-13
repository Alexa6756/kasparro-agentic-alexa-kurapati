from typing import TypedDict, Dict, Any, List, Optional

class AgentState(TypedDict):
    raw_product_data: str
    parsed_product: Optional[Dict[str, Any]]
    questions: Optional[List[Dict[str, Any]]]
    outputs: Dict[str, Any]
