# import enum

# from sqlalchemy.dialects.postgresql import UUID

# from db_utils.model.base_user_log_model import BaseUserLogModel
# from db_utils.modules.db import db


# class FileTypeEnum(enum.Enum):
#     full = "full"
#     partial = "partial"
#     segment = "segment"


# class FirmwareFile(BaseUserLogModel):
#     __tablename__ = 'firmware_file'

#     file_url = db.Column(db.String(1000))
#     version_name = db.Column(db.String(255))
#     sha2_hashsum = db.Column(db.String(255))
#     type = db.Column(db.Enum(FileTypeEnum))

#     firmware_id = db.Column(UUID(as_uuid=True), db.ForeignKey("firmware.id"))
