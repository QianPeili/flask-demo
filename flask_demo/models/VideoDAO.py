import gridfs


class VideoDAO(object):

    def __init__(self, database):
        self.db = database.videos
        self.videos = self.db.video_list

    def save_video(self, video_obj, video_name):
        grid = gridfs.GridFS(self.db, "video_meta")
        _id = grid.put(video_obj)
        video_obj.close()

        self.videos.insert({'grid_id': _id, 'name': video_name})

    def get_video(self, name):

        doc = self.videos.find_one({'name': name})
        if doc is None:
            return False



