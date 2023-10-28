from pydantic.v1 import BaseModel


class WriteHtmlReportArgsSchema(BaseModel):
    file_name: str
    html_report: str
