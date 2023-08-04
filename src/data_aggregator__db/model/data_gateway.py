from db_utils.model.base_user_log_model import BaseUserLogModel
from db_utils.modules.db import db


class DataGateway(BaseUserLogModel):
    __tablename__ = 'data_gateway'

    name = db.Column(db.String(255), unique=True, nullable=False)
