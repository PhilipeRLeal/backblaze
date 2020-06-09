from datetime import datetime


class BucketTypes:
    public = "allPublic"
    private = "allPrivate"


class FileModel:
    def __init__(self, data):
        self.account_id = data["accountId"]
        self.action = data["action"]
        self.bucket_id = data["bucketId"]
        self.content_length = data["contentLength"]
        self.content_sha1 = data["contentSha1"]
        self.content_md5 = data["contentMd5"]
        self.content_type = data["contentType"]
        self.file_id = data["fileId"]
        self.file_info = data["fileInfo"]
        self.file_name = data["fileName"]
        self.timestamp = datetime.utcfromtimestamp(
            data["uploadTimestamp"]
        )


class FileVersionModel:
    def __init__(self, data):
        self.next_file_name = data["nextFileName"]
        self.next_file_id = data["nextFileId"]


class BucketModel:
    def __init__(self, data):
        self.account_id = data["accountId"]
        self.bucket_id = data["bucketId"]
        self.bucket_name = data["bucketName"]

        if data["bucketType"] == "allPrivate":
            self.bucket_type = BucketTypes.private
        else:
            self.bucket_type = BucketTypes.public

        self.bucket_info = data["bucketInfo"]
        self.cors_rules = data["corsRules"]
        self.lifecycle_rules = data["lifecycleRules"]
        self.revision = data["revision"]
        self.options = data["options"]
