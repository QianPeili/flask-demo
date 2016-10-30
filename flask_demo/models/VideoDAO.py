import gridfs

from bson.objectid import ObjectId


class VideoDAO(object):

    def __init__(self, database):
        self.db = database.videos
        self.videos = self.db.video_list
        self.grid = gridfs.GridFS(self.db, "video_meta")

    def save_video(self, video_obj, video_name):
        self.grid.put(video_obj, filename=video_obj.filename, title=video_name)
        video_obj.close()

    def load_video(self, grid_id):
        video = self.grid.find_one({'_id': ObjectId(grid_id)})
        print(dir(video))
        print(video)
        return video



