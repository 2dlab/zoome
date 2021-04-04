def get_download_urls_from_meeting(meeting):
    recording_files = meeting["recording_files"]
    if not all([record['status'] == 'completed' for record in recording_files]):
        return []

    def get_url_obj(record):
        return {
            "download_url": record["download_url"],
            "recording_type": record["recording_type"],
            "file_type": record["file_type"],
            "recording_start": record["recording_start"],
            "recording_end": record["recording_end"]
        }

    return [get_url_obj(record) for record in recording_files]


def get_meetings_download_urls(meetings):
    return [get_download_urls_from_meeting(meeting) for meeting in meetings]


if __name__ == "__main__":
    pass
